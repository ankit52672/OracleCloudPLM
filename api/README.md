# API content guide

Organize examples by Oracle Cloud PLM business object:

```text
api/
  common/
    authentication/
    pagination/
    errors/
  objects/
    Items/
    ChangeOrders/
    ChangeRequests/
    Manufacturers/
    BOMs/
    Attachments/
    Associations/
```

Within an object folder, group related materials by endpoint or task. For example:

```text
Items/
  README.md
  requests/
  guides/
  examples/
```

Use the following structure for each API example or guide:

1. Purpose and Oracle product/API version.
2. Required privileges and configuration.
3. HTTP method and verified endpoint path.
4. Request headers, query parameters, and body (use placeholders).
5. Redacted example response and expected result.
6. Errors, pagination, and side effects.

Keep shared conventions in `common/` and link to them from object-specific materials. Do not store live credentials, tenant exports, or unredacted customer data here.

