# What's New In Python 3.13 / webbrowser - webbrowser

### webbrowser

- Drop the untested and undocumented `MacOSX` class, which carried a Python 3.11 deprecation. Reach for the `MacOSXOSAScript` class (which arrived in Python 3.2) in its place. (Contributed by Hugo van Kemenade in [gh-104804](https://github.com/python/cpython/issues/104804).)

- Drop the deprecated `MacOSXOSAScript._name` attribute. Reach for the [`MacOSXOSAScript.name`](https://docs.python.org/3.14/library/webbrowser.html#webbrowser.controller.name) attribute in its place. (Contributed by Nikita Sobolev in [gh-105546](https://github.com/python/cpython/issues/105546).)

[Subject index](INDEX.md) · [Previous source section](urllib.md) · [Next source section](new-deprecations.md) · [Release/subject declaration](summary-release-highlights.md)
