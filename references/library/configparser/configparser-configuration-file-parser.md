# configparser — `configparser` — Configuration file parser

### `configparser` — Configuration file parser

**Source code:** [Lib/configparser.py](https://github.com/python/cpython/tree/3.14/Lib/configparser.py)

---

The `ConfigParser` class lives in this module; it offers a simple configuration language whose layout resembles the INI files familiar from Microsoft Windows. With it, your Python programs become easy for end users to tailor to their needs.

Note

The value-type prefixes from the Windows Registry's extended take on INI syntax are neither parsed nor emitted by this library.

See also

Module [`tomllib`](https://docs.python.org/3.14/library/tomllib.html#module-tomllib)

For application configuration files, TOML is a precisely-specified format. Its explicit aim is to serve as a better take on INI.

Module [`shlex`](https://docs.python.org/3.14/library/shlex.html#module-shlex)

Helps build Unix shell-style mini-languages, which themselves can serve as application configuration files.

Module [`json`](https://docs.python.org/3.14/library/json.html#module-json)

A portion of JavaScript syntax is realized by the `json` module — occasionally chosen for configuration, though it lacks comment support.

[Subject index](INDEX.md) · [Continue](quick-start-section-introduction-and-initial-examples.md)
