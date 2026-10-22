# 3.1.1. Requirements for optional modules

### 3.1.1. Requirements for optional modules

Certain [optional modules](https://docs.python.org/3.14/glossary.html#term-optional-module) within the standard library depend on third-party libraries being present for development (header files, for instance, have to be reachable).

The `configure` output flags any absent requirements. Modules left out because dependencies are missing show up close to the tail of the `make` output, occasionally under an internal label — `_ctypes` standing in for the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module, as one example.

When you ship a CPython interpreter that omits optional modules, the recommended practice is to notify users, since they typically assume the standard library modules will be present.

The dependencies needed to compile the optional modules follow:

| Dependency | Minimum version | Python module |
| --- | --- | --- |
| libbz2 |  | `bz2` |
| libffi | 3.3.0 recommended | `ctypes` |
| liblzma |  | `lzma` |
| libmpdec | 2.5.0 | `decimal` [1] |
| libreadline or libedit [2] |  | `readline` |
| libuuid |  | `_uuid` [3] |
| ncurses [4] |  | `curses` |
| OpenSSL | 3.0.18 recommended (1.1.1 minimum) | `ssl`, `hashlib` [5] |
| SQLite | 3.15.2 | `sqlite3` |
| Tcl/Tk | 8.5.12 | `tkinter`, IDLE, `turtle` |
| zlib | 1.2.2.1 | `zlib`, `gzip`, `ensurepip` |
| zstd | 1.4.5 | `compression.zstd` |

Be aware that this table omits some optional modules; specifically, modules tied to a particular platform such as [`winreg`](https://docs.python.org/3.14/library/winreg.html#module-winreg) do not appear above.

See also

- The [devguide](https://devguide.python.org/getting-started/setup-building/#install-dependencies) carries a complete list of dependencies needed to compile every module, plus steps for installing them across common platforms.

- `--with-system-expat` permits a build that links against an outside [libexpat](https://libexpat.github.io/) library.

- Options for third-party dependencies

Changed in version 3.1: Tcl/Tk version 8.3.1 became the minimum for [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter).

Changed in version 3.5: Tcl/Tk version 8.4 became the minimum for [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter).

Changed in version 3.7: OpenSSL 1.0.2 became the minimum for [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) and [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl).

Changed in version 3.10: OpenSSL 1.1.1 became the minimum for [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) and [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl). SQLite 3.7.15 became the minimum for [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3).

Changed in version 3.11: Tcl/Tk version 8.5.12 became the minimum for [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter).

Changed in version 3.13: SQLite 3.15.2 became the minimum for [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3).

[Subject index](INDEX.md) · [Previous source section](build-requirements.md) · [Following source section](generated-files.md)
