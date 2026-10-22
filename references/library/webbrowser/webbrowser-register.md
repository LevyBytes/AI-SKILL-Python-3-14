# webbrowser: `webbrowser.register()`

webbrowser.register(*name*, *constructor*, *instance=None*, ***, *preferred=False*)

Record the browser type *name*. After a browser type has been recorded, the `get()` function is able to hand back a controller for it. When *instance* is omitted or set to `None`, *constructor* runs with no parameters to build an instance whenever one is needed. When *instance* is supplied, *constructor* is never invoked and is permitted to be `None`.

Giving *preferred* a value of `True` marks this browser as a favored outcome for a `get()` call carrying no argument. Apart from that, this entry point only helps if you intend either to assign the `BROWSER` variable or to call `get()` with a non-empty argument that lines up with the name of a handler you register.

Changed in version 3.7: *preferred* keyword-only parameter was added.

Several browser types come predefined. The table below lists the type names you can hand to the `get()` function alongside the matching controller-class instantiations, every one of them declared inside this module.

| Type Name | Class Name | Notes |
| --- | --- | --- |
| `'mozilla'` | `Mozilla('mozilla')` |  |
| `'firefox'` | `Mozilla('mozilla')` |  |
| `'epiphany'` | `Epiphany('epiphany')` |  |
| `'kfmclient'` | `Konqueror()` | (1) |
| `'konqueror'` | `Konqueror()` | (1) |
| `'kfm'` | `Konqueror()` | (1) |
| `'opera'` | `Opera()` |  |
| `'links'` | `GenericBrowser('links')` |  |
| `'elinks'` | `Elinks('elinks')` |  |
| `'lynx'` | `GenericBrowser('lynx')` |  |
| `'w3m'` | `GenericBrowser('w3m')` |  |
| `'windows-default'` | `WindowsDefault` | (2) |
| `'macosx'` | `MacOSXOSAScript('default')` | (3) |
| `'safari'` | `MacOSXOSAScript('safari')` | (3) |
| `'google-chrome'` | `Chrome('google-chrome')` |  |
| `'chrome'` | `Chrome('chrome')` |  |
| `'chromium'` | `Chromium('chromium')` |  |
| `'chromium-browser'` | `Chromium('chromium-browser')` |  |
| `'iosbrowser'` | `IOSBrowser` | (4) |

Notes:

1.

On Unix, “Konqueror” serves as the file manager of the KDE desktop, so reaching for it is only sensible while KDE is active. A dependable means of spotting KDE would be welcome, but the `KDEDIR` variable does not cut it. Be aware too that the “kfm” name still applies even when the **konqueror** command is invoked under KDE 2 — the code picks whatever approach works best for launching Konqueror.

2.

Windows platforms exclusively.

3.

macOS exclusively.

4.

iOS exclusively.

Added in version 3.2: On Mac, a fresh `MacOSXOSAScript` class now stands in for the earlier `MacOSX` class. The new class allows launching browsers that are not the OS default at the moment.

Added in version 3.3: Chrome and Chromium are now supported.

Changed in version 3.12: A handful of outdated browsers no longer have support. The dropped browsers are Grail, Mosaic, Netscape, Galeon, Skipstone, Iceape, plus Firefox releases 35 and earlier.

Changed in version 3.13: iOS is now supported.

A few straightforward examples follow:

```python
url = 'https://docs.python.org/'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)

```

[Subject index](INDEX.md) · [Previous](webbrowser-error-to-webbrowser-get.md) · [Continue](controller-name-to-controller-open-new-tab.md) · [Owning module, declaration or section: webbrowser](webbrowser-convenient-web-browser-controller.md) · [Owning module, declaration or section: Command-line interface](webbrowser-error-to-webbrowser-get.md)
