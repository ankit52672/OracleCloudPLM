# Oracle Cloud PLM MCP server example

This local Model Context Protocol (MCP) server exposes one read-only `get_plm_resource` tool. It sends GET requests to the HTTPS host configured in `ORACLE_PLM_BASE_URL` and authenticates with the bearer token in `ORACLE_PLM_TOKEN`.

## Requirements and setup

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/)
- An authorized Oracle Cloud PLM host and a short-lived or otherwise appropriately managed bearer token

Set `ORACLE_PLM_BASE_URL` to the tenant's HTTPS origin (for example, `https://your-tenant.example.com`, without a resource path) and set `ORACLE_PLM_TOKEN` in the environment that launches VS Code. Do not put either value in this repository. For local testing, environment variables can be set in the shell before launching VS Code.

The root `.mcp.json` references these environment variables and launches the server with `uv`. Workspace-root MCP configuration is experimental in VS Code; enable `chat.mcp.workspaceRootConfig.enabled` in VS Code settings if needed, then use the MCP Servers controls to start and review the server. Restart VS Code after changing its environment. Approve only tool calls you intend to make.

## Tool behavior

- The server only makes GET requests; it cannot create, update, or delete PLM data.
- The requested resource path must be relative to the configured host. Absolute URLs, traversal segments, and query strings in the path are rejected.
- Pass query parameters separately. Responses are limited to 2 MiB.
- The implementation does not manage OAuth token acquisition or refresh. Adapt authentication to your organization's approved flow before broader use.

Install dependencies and run focused tests:

```powershell
uv sync --project mcp-server
uv run --project mcp-server python -m unittest discover -s mcp-server/tests
```

