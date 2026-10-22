# webbrowser: `webbrowser.Error`, `webbrowser.open()`, `webbrowser.open_new()`, `webbrowser.open_new_tab()`, `webbrowser.get()`

### Command-line interface

As a command-line front end to the module, the **webbrowser** script is available. A URL is supplied as its argument, and it recognizes these optional parameters as well:

 -n, --new-window

Where feasible, opens the URL within a fresh browser window.

 -t, --new-tab

Where feasible, opens the URL within a fresh browser tab.

These two options are, of course, not allowed together. Example usage:

```bash
python -m webbrowser -t "https://www.python.org"

```

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI, not Android.

The following exception is defined:

 *exception *webbrowser.Error

Raised whenever something goes wrong while controlling a browser.

These functions are provided:

 webbrowser.open(*url*, *new=0*, *autoraise=True*)

Show *url* through the default browser. A *new* of 0 reuses the same browser window where it can; a *new* of 1 spins up a fresh browser window where it can; a *new* of 2 opens a fresh browser page (a “tab”) where it can. When *autoraise* is `True`, the window gets raised where it can (be aware that many window managers raise it no matter how this flag is set).

Yields `True` when a browser came up successfully, and `False` if not.

Keep in mind that on certain platforms, passing a filename to this function might happen to succeed and trigger the program the OS associates with it. That behavior, though, is neither portable nor officially backed.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `webbrowser.open` with argument `url`.

 webbrowser.open_new(*url*)

Where feasible, open *url* in a fresh window of the default browser; failing that, open *url* in the sole browser window available.

When a browser launches without trouble it gives back `True`; otherwise the result is `False`.

 webbrowser.open_new_tab(*url*)

Where feasible, open *url* in a fresh page (a “tab”) of the default browser; if that cannot happen, the effect matches `open_new()`.

When a browser launches without trouble it gives back `True`; otherwise the result is `False`.

 webbrowser.get(*using=None*)

Hand back a controller object matching the browser type *using*. Should *using* be `None`, the returned controller targets whichever default browser fits the caller's environment.

[Subject index](INDEX.md) · [Previous](webbrowser-convenient-web-browser-controller.md) · [Continue](webbrowser-register.md) · [Owning module, declaration or section: webbrowser](webbrowser-convenient-web-browser-controller.md)
