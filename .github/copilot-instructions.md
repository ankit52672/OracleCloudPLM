# Repository instructions

- Organize Oracle Cloud PLM API materials by object under `api/objects/`; put genuinely shared guidance under `api/common/`.
- Verify endpoint paths, versions, fields, and behavior using current Oracle documentation or a user-provided tenant reference. Do not invent endpoint details.
- Treat API calls as tenant operations. Prefer read-only examples; clearly label any operation that creates, updates, or deletes data and require explicit user intent before running it.
- Never request, print, or commit credentials, tokens, tenant-specific secrets, or unredacted customer data. Use environment variables and placeholders in examples.
- Keep examples self-contained and document prerequisites, permissions, inputs, and expected output.
- When changing executable code, run the focused tests and report what was and was not verified.

