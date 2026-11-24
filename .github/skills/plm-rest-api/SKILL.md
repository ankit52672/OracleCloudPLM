---
name: plm-rest-api
description: Organize, document, or implement Oracle Cloud PLM REST API examples by business object. Use when working on Items, Change Orders, Change Requests, Manufacturers, BOMs, Attachments, Associations, or shared PLM API guidance.
---

# Oracle Cloud PLM REST API workflow

1. Identify the PLM object and keep its materials under `api/objects/<Object>/`. Put shared authentication, pagination, or error-handling guidance under `api/common/`.
2. Confirm endpoint paths, API version, request fields, and behavior from current Oracle documentation or references supplied by the user. If a detail is unknown, mark it as unverified instead of guessing.
3. Document the purpose, prerequisites and privileges, inputs, example request, expected response, and relevant errors. Use placeholders for tenant URLs and record IDs.
4. Clearly distinguish read-only requests from operations that modify tenant data. Do not execute a modifying request without explicit user authorization.
5. Keep credentials and customer data out of source, logs, examples, and responses. Refer to environment variables for local configuration and redact sensitive fields from sample output.
6. Run the narrowest relevant validation and state any assumptions or unverified behavior.

