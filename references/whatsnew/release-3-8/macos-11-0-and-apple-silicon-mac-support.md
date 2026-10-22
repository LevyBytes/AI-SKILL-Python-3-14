# What’s New In Python 3.8 / macOS 11.0 (Big Sur) and Apple Silicon Mac support

### Notable changes in Python 3.8.10

### macOS 11.0 (Big Sur) and Apple Silicon Mac support

Beginning with 3.8.10, Python can be compiled and run atop macOS 11 (Big Sur) as well as on Apple Silicon Macs, which rest on the `ARM64` architecture. A freshly added universal build flavor, `universal2`, now covers both `ARM64` and `Intel 64` natively within a single set of executables. Be aware that “weaklinking” — producing binaries aimed at newer macOS releases that still run properly on older ones by probing at runtime for absent features — was left out of this backport from Python 3.9; if you must span several macOS releases, keep targeting and compiling against the earliest version in that span.

(The original work here came from Ronald Oussoren and Lawrence D’Anna under [gh-85272](https://github.com/python/cpython/issues/85272), with corrections supplied by FX Coudert and Eli Rykoff, then carried back to 3.8 by Maxime Bélanger and Ned Deily)

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-8-9.md) · [Next source section](urllib-parse.md) · [Release/subject declaration](assignment-expressions.md)
