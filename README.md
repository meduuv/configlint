# ConfigLint

> Catch configuration mistakes early with deterministic diagnostics.

ConfigLint is a lightweight configuration linter for common project configuration files. It validates required settings, detects duplicate keys, and produces machine-readable findings.

## Highlights

- Detect duplicate keys
- Validate required settings
- Flag empty values when rules require a value
- Consistent command-line diagnostics
- JSON report output
- Rule-file support for custom checks

## Usage

```bash
configlint config.json
configlint config.json --json
configlint config.json --rule required:port
```

## Workflow

```text
configuration
      ↓
   parse + rules
      ↓
   diagnostics
      ↓
 fix before deploy
```

## Use Cases

- Project configuration validation
- CI checks
- Deployment preparation
- Local development tooling
- Security-conscious configuration review

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
