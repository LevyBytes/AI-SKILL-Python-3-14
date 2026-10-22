# Language and standard library pending removal in future versions: importlib; importlib.metadata; logging; mailbox; os; pydoc.ErrorDuringImport; re; sre_compile, sre_constants, sre_parse; shutil

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - the *debug_override* parameter of [`cache_from_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.cache_from_source) is deprecated; turn to the *optimization* parameter instead.

- [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata):

  - the `EntryPoints` tuple interface.

  - an implicit `None` among return values.

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): the `warn()` method has carried a deprecation ever since Python 3.3; reach for [`warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning) in its stead.

- [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox): relying on StringIO input together with text mode is deprecated; switch over to BytesIO paired with binary mode.

- [`os`](https://docs.python.org/3.14/library/os.html#module-os): invoking [`os.register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) from within a multi-threaded process.

- `pydoc.ErrorDuringImport`: handing a tuple value to the *exc_info* parameter is deprecated; pass an exception instance instead.

- [`re`](https://docs.python.org/3.14/library/re.html#module-re): tighter rules now govern numerical group references and group names within regular expressions. A numerical reference is henceforth accepted only as a run of ASCII digits. Inside bytes patterns and replacement strings, a group name may now consist solely of ASCII letters, digits, and the underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

- the `sre_compile`, `sre_constants` and `sre_parse` modules.

- [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil): the *onerror* parameter of [`rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) has been deprecated since Python 3.12; switch to the *onexc* parameter instead.

[Subject index](INDEX.md) · [Previous source section](argparse-through-gettext.md) · [Next source section](ssl-options-and-protocols-threading-methods-typing-text.md)
