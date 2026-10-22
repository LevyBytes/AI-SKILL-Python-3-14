# curses — `curses` — Terminal handling for character-cell displays

### `curses` — Terminal handling for character-cell displays

**Source code:** [Lib/curses](https://github.com/python/cpython/tree/3.14/Lib/curses)

---

The `curses` module exposes an interface to the curses library — the de-facto standard tool for writing portable, advanced terminal-handling code.

Although curses sees most of its use under Unix, builds also exist for Windows, DOS, and quite possibly additional platforms. This extension module aims to follow the API offered by ncurses, an open-source curses implementation maintained on Linux together with the BSD flavors of Unix.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](https://docs.python.org/3.14/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability).

This is an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should it be absent from your build of CPython, consult whatever documentation your distributor supplies (meaning whoever handed Python to you). And if that distributor is you, refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Note

Anywhere this documentation refers to a *character*, the accepted forms are an integer, a Unicode string holding one character, or a byte string holding a single byte.

Anywhere this documentation refers to a *character string*, you may supply it as either a Unicode string or a byte string.

See also

Module [`curses.ascii`](https://docs.python.org/3.14/library/curses.ascii.html#module-curses.ascii)

Helpers for handling ASCII characters, independent of whatever locale you have configured.

Module [`curses.panel`](https://docs.python.org/3.14/library/curses.panel.html#module-curses.panel)

A panel-stack extension that gives curses windows a sense of depth.

Module `curses.textpad`

An editable text widget for curses that offers **Emacs**-style key bindings.

[Curses Programming with Python](https://docs.python.org/3.14/howto/curses.html#curses-howto)

A tutorial covering curses use from Python, written by Andrew Kuchling and Eric Raymond.

[Subject index](INDEX.md) · [Continue](curses-error-to-curses-endwin.md)
