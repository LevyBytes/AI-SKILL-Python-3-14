# 7.1.1. iOS version compatibility

### 7.1. Python at runtime on iOS

### 7.1.1. iOS version compatibility

You declare the lowest iOS version you support at compile time through the [`--host`](https://docs.python.org/3.14/using/configure.html#cmdoption-host) option passed to `configure`. Out of the box, an iOS build of Python targets a minimum supported iOS version of 13.0. Should you want a different floor, supply that version number within the `--host` argument — as an illustration, `--host=arm64-apple-ios15.4-simulator` produces an ARM64 simulator build whose deployment target sits at 15.4.

[Subject index](INDEX.md) · [Previous source section](using-python-on-ios.md) · [Following source section](platform-identification.md)
