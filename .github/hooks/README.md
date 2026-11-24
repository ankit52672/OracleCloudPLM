# Copilot hook example

Workspace Copilot hooks belong in `.github/hooks/*.json`. Hooks execute automatically at configured agent lifecycle events, so review their commands and scripts before enabling them.

The following optional diagnostic hook records only the tool name before a tool runs. It does not record tool arguments or approve the tool. Save it as `.github/hooks/audit.json` to enable it; the referenced script requires Node.js:

```json
{
  "version": 1,
  "hooks": {
    "preToolUse": [
      {
        "type": "command",
        "command": "node .github/hooks/log-tool-use.cjs",
        "timeoutSec": 10
      }
    ]
  }
}
```

Save this script as `.github/hooks/log-tool-use.cjs`:

```js
const fs = require('node:fs');
const path = require('node:path');

const event = JSON.parse(fs.readFileSync(0, 'utf8'));
if (typeof event.toolName !== 'string') {
  throw new Error('Expected a Copilot preToolUse event with toolName.');
}

fs.appendFileSync(
  path.join(__dirname, 'tool-use.log'),
  `${JSON.stringify(event.toolName)}\n`
);
process.stdout.write('{}');
```

The log path is ignored by Git. Check the current Copilot hooks documentation before adapting the example, since hook support and event formats can change.

