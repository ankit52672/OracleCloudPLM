# Oracle Cloud PLM REST API

A community-maintained workspace for organizing reusable Oracle Cloud PLM REST API examples, request collections, and step-by-step guides. It also includes starter customizations for AI coding agents.

## Repository layout

```text
api/
  common/                 Shared authentication, pagination, and response guidance
  objects/
    Items/
    ChangeOrders/
    ChangeRequests/
    Manufacturers/
    BOMs/
    Attachments/
    Associations/
.github/
  copilot-instructions.md
  hooks/                  Hook examples and setup guidance
  skills/
    plm-rest-api/
      SKILL.md            On-demand REST API workflow
.mcp.json                 Workspace MCP server configuration
mcp-server/               Read-only Oracle REST MCP server example
```

Keep each object's endpoints, request/response examples, and guides in its matching `api/objects/<Object>/` directory. Put shared behavior in `api/common/`; link to it rather than copying the same guidance into every object. Add new object folders as needed, using consistent PascalCase names.

## Getting started

1. Clone the repository and open its root in VS Code.
2. Read [Copilot instructions](.github/copilot-instructions.md) and the [API contribution guide](api/README.md).
3. Use the `plm-rest-api` skill for API documentation and example tasks. See [the skill](.github/skills/plm-rest-api/SKILL.md).
4. To run the optional MCP example, install Python 3.10+ and [uv](https://docs.astral.sh/uv/), set `ORACLE_PLM_BASE_URL` and `ORACLE_PLM_TOKEN` in the environment where VS Code runs, enable VS Code's `chat.mcp.workspaceRootConfig.enabled` setting, then start the server from the MCP Servers view. Restart VS Code after changing its environment. See [the MCP server guide](mcp-server/README.md).

The MCP example performs GET requests only. Review its source and the configured server before allowing an agent to use it. It is a starter, not a substitute for your organization's Oracle authentication, authorization, or data-handling policies.

## Contributing API examples

- Verify endpoints and payloads against your Oracle Cloud PLM tenant's current official documentation.
- Use placeholders for tenant URLs, IDs, and other environment-specific values.
- Never commit credentials, customer data, or unredacted production responses.
- State prerequisites, required privileges, expected results, and any known product/version constraints.
- Prefer small, focused examples and note whether an operation is read-only or changes tenant data.

