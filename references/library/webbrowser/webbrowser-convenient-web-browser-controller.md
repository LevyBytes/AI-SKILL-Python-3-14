# webbrowser`webbrowser` - Convenient web-browser controller

# Webbrowser, Windows

## Overview

Covers: webbrowser — Convenient web-browser controller; MS Windows Specific Services.

## webbrowser - Convenient web-browser controller

### `webbrowser` - Convenient web-browser controller

**Source code:** [Lib/webbrowser.py](https://github.com/python/cpython/tree/3.14/Lib/webbrowser.py)

---

A high-level way to present web-based documents to people is what the `webbrowser` module supplies. In nearly every situation, you only need to invoke this module's `open()` function and the proper behavior follows.

On Unix, graphical browsers take precedence whenever X11 is present, yet a text-mode browser is the fallback when no graphical browser exists or no X11 display is reachable. Should a text-mode browser be selected, the process that called it stays blocked until the person quits that browser.

Whenever the `BROWSER` environment variable is set, its contents are read as an [`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep)-separated roster of browsers to attempt before the platform's own defaults. If one entry holds the `%s` token, that entry counts as a verbatim browser command line, with the URL argument dropped in where `%s` sits; if instead an entry is a single word naming one of the already-registered browsers, that browser moves to the head of the lookup order; and an entry that omits `%s` is simply read as the name of a browser to start. [1]

Changed in version 3.14: The `BROWSER` variable can additionally be employed to rearrange the platform-default ordering. That ability proves especially handy on macOS, since the platform defaults there point to things other than command-line tools on `PATH`.

When running anywhere other than Unix, or when a remote browser is on hand under Unix, the controlling process does not pause for the person to finish browsing; instead it permits the remote browser to keep its own windows on screen. Where Unix offers no remote browser, the controlling process starts a fresh browser and then waits.

Under iOS, the `BROWSER` environment variable gets disregarded, as does every argument that governs autoraise, browser preference, and the creation of a new tab or window. A web page is *always* shown in whichever browser the person prefers, opened in a new tab, with that browser pulled to the foreground. Running the `webbrowser` module on iOS depends on the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module; if `ctypes` is absent, every call to `open()` fails.

[Subject index](INDEX.md) · [Continue](webbrowser-error-to-webbrowser-get.md)
