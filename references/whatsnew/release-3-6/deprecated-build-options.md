# What's New In Python 3.6 / Deprecated Build Options

### Deprecated Build Options

On UNIX platforms other than macOS, the `--with-system-ffi` configure flag now defaults to on. You can switch it off via `--without-system-ffi`, yet relying on that flag is deprecated and Python 3.7 will reject it. This shift leaves macOS untouched. Be aware that plenty of OS distributors already apply the `--with-system-ffi` flag while compiling their system Python.

[Subject index](INDEX.md) · [Previous source section](deprecated-functions-and-types-of-the-c-api.md) · [Next source section](api-and-feature-removals.md) · [Release/subject declaration](summary-release-highlights.md)
