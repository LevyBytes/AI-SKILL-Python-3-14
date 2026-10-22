# What's New In Python 3.9 / macOS 11.0 (Big Sur) and Apple Silicon Mac support

### macOS 11.0 (Big Sur) and Apple Silicon Mac support

Starting with 3.9.1, Python offers complete support for building and running atop macOS 11.0 (Big Sur) as well as Apple Silicon Macs, which rest on the `ARM64` architecture. There is a fresh universal build flavor, `universal2`, that natively covers both `ARM64` and `Intel 64` within a single batch of executables. You can likewise build binaries on today’s macOS releases and ship them to a span of earlier macOS versions (verified down to 10.9), all while exposing certain newer OS functions and options conditionally according to whichever operating system version is running at the time — the so-called “weaklinking”.

(Contributed by Ronald Oussoren and Lawrence D’Anna in [bpo-41100](https://bugs.python.org/issue?@action=redirect&bpo=41100).)

[Subject index](INDEX.md) · [Previous source section](typing.md) · [Next source section](collections-abc.md) · [Release/subject declaration](summary-release-highlights.md)
