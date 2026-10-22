# Language and standard library pending removal in future versions: importlib.metadata; logging; mailbox; os; pydoc.ErrorDuringImport; re; sre_compile, sre_constants, sre_parse; shutil

- [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata):

  - The `EntryPoints` tuple interface.

  - Implicit `None` on return values.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): the `warn()` method, deprecated since Python 3.3, should be replaced by [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning).

- [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox): relying on StringIO input and text mode is deprecated; use BytesIO and binary mode in their place.

- [`os`](https://docs.python.org/3.14/library/os.html#module-os): invoking [`os.register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) within a multi-threaded process.

- `pydoc.ErrorDuringImport`: passing a tuple for the *exc_info* parameter is deprecated; supply an exception instance.

- [`re`](https://docs.python.org/3.14/library/re.html#module-re): tighter rules now govern numerical group references and group names inside regular expressions. A numerical reference is now accepted only as a run of ASCII digits. For bytes patterns and replacement strings, group names may now contain only ASCII letters, digits, and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

- The `sre_compile`, `sre_constants`, and `sre_parse` modules.

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil): the *onerror* parameter of [`rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) is deprecated as of Python 3.12; rely on the *onexc* parameter instead.

[Subject index](INDEX.md) · [Previous source section](argparse-through-importlib.md) · [Next source section](ssl-options-and-protocols-threading-methods.md)
