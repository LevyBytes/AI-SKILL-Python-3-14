# Python 3.10.0 alpha 3 / macos / collections and iteration

[bpo-41100](https://bugs.python.org/issue?@action=redirect&bpo=41100): Introduce support covering macOS 11 along with Apple Silicon machines.

Building ?Universal 2? binaries is now achievable through ??enable-universalsdk ?with-universal-archs=universal2?.

Builds produced on newer macOS releases can run on earlier ones too (verified back through macOS 10.9), provided the appropriate deployment target is set. Validation here relies on Xcode 11 or newer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
