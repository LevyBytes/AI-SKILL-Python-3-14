# Python 3.13.0 alpha 3 / macos / locale

[gh-108269](https://github.com/python/cpython/issues/108269): Turn `CFBundleAllowMixedLocalizations` to true within the Info.plist of the framework, the bundled Python.app, and IDLE.app for framework installs on macOS. With this, applications can honor the user's preferred locale whenever it differs from english.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
