# ConfigLint

A small configuration linter for common project configuration files.

## Features

- Detect duplicate keys
- Validate required settings
- Flag empty values when rules require a value
- Consistent command-line diagnostics
- JSON report output
- Simple rule-file API for custom checks

## Usage

```bash
configlint config.json
configlint config.json --json
configlint config.json --rule required:port
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

Built by Medu: https://guns.lol/meduu
