# PyConfig.pathconfig_warnings

int pathconfig_warnings

When non-zero, the path-configuration computation may emit warnings to `stderr`; a value of `0` keeps those warnings quiet.

Default: `1` in Python mode, `0` in isolated mode.

Belongs to the Python Path Configuration input.

Changed in version 3.11: This now takes effect on Windows as well.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Following source contract](parser-debug.md) · [Following source contract](prefix-to-run-module.md)
