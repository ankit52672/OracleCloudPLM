import json
import os
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen

from mcp.server.fastmcp import FastMCP

MAX_RESPONSE_BYTES = 2 * 1024 * 1024
RESOURCE_PATH_PATTERN = re.compile(r"[A-Za-z0-9._~/-]+\Z")
mcp = FastMCP("oracle-cloud-plm-read-only")


def build_resource_url(
    base_url: str, resource_path: str, query_params: dict[str, str] | None = None
) -> str:
    base = urlsplit(base_url)
    if (
        base.scheme != "https"
        or not base.hostname
        or base.username
        or base.password
        or base.path not in ("", "/")
        or base.query
        or base.fragment
    ):
        raise ValueError("ORACLE_PLM_BASE_URL must be an HTTPS origin without a path.")

    path = urlsplit(resource_path)
    segments = resource_path.split("/")
    if (
        not resource_path
        or path.scheme
        or path.netloc
        or path.query
        or path.fragment
        or not RESOURCE_PATH_PATTERN.fullmatch(resource_path)
        or any(segment in ("", ".", "..") for segment in segments)
    ):
        raise ValueError(
            "resource_path must be a relative API path without empty or traversal segments."
        )

    return urlunsplit(
        (
            base.scheme,
            base.netloc,
            f"/{resource_path}",
            urlencode(query_params or {}),
            "",
        )
    )


@mcp.tool()
def get_plm_resource(
    resource_path: str, query_params: dict[str, str] | None = None
) -> str:
    """Fetch a JSON PLM resource with GET; resource_path is relative to the configured tenant origin."""
    base_url = os.environ.get("ORACLE_PLM_BASE_URL", "")
    token = os.environ.get("ORACLE_PLM_TOKEN", "")
    if not token:
        raise RuntimeError("ORACLE_PLM_TOKEN is required.")

    url = build_resource_url(base_url, resource_path, query_params)
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="GET",
    )
    try:
        with urlopen(request, timeout=30) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
    except HTTPError as error:
        detail = error.read(500).decode("utf-8", errors="replace")
        raise RuntimeError(f"Oracle PLM request failed with HTTP {error.code}: {detail}") from error
    except URLError as error:
        raise RuntimeError(f"Oracle PLM request could not be completed: {error.reason}") from error

    if len(body) > MAX_RESPONSE_BYTES:
        raise RuntimeError("Oracle PLM response exceeded the 2 MiB size limit.")
    try:
        return json.dumps(json.loads(body), ensure_ascii=False)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError("Oracle PLM returned a response that was not valid JSON.") from error


def main() -> None:
    mcp.run()

