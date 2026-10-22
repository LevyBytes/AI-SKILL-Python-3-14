# Python 3.9.0 alpha 2 / library / provide whitespace options json formatting through json tool cli

[bpo-29636](https://bugs.python.org/issue?@action=redirect&bpo=29636): Provide whitespace options for JSON formatting through the `json.tool` CLI. These mutually exclusive options are now available: `--indent` sets the indent level in spaces; `--tab` indents using tabs; `--no-indent` drops newlines; and `--compact` strips all whitespace. By default the behavior stays identical to `--indent=4`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
