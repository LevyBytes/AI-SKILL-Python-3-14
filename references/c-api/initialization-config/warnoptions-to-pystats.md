# initialization config C API: Warning filters, bytecode and interpreter statistics

PyWideStringList warnoptions

The options the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module uses to assemble its warning filters, running from lowest priority up to highest: [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions).

The [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module feeds [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) in reverse: the final `PyConfig.warnoptions` entry turns into the leading entry of `warnings.filters`, the one consulted first (and thus highest priority).

Each [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) command line option contributes its value to `warnoptions`, and the flag may appear more than once.

You can likewise supply warning options through the [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable, listing several at once delimited by commas (`,`).

Default: empty list.

 int write_bytecode

At a value of `0`, Python makes no attempt to emit `.pyc` files when source modules get imported.

Turned to `0` by the [`-B`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-B) command line option and the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) environment variable.

[`sys.dont_write_bytecode`](https://docs.python.org/3.14/library/sys.html#sys.dont_write_bytecode) starts out as the negated value of `write_bytecode`.

Default: `1`.

 PyWideStringList xoptions

The values gathered from the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line options: [`sys._xoptions`](https://docs.python.org/3.14/library/sys.html#sys._xoptions).

Default: empty list.

 int _pystats

When non-zero, dump performance statistics as Python exits.

Calls for a special build carrying the `Py_STATS` macro: refer to [`--enable-pystats`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-pystats).

Default: `0`.

Whenever `parse_argv` is non-zero, the `argv` arguments get parsed exactly as ordinary Python parses [command line arguments](https://docs.python.org/3.14/using/cmdline.html#using-on-cmdline), and the Python-specific arguments are then removed from `argv`.

Parsing the `xoptions` options drives other settings: refer to the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option.

Changed in version 3.9: The `show_alloc_count` field is gone.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](tracemalloc-to-verbose.md) · [Following source contract](pyconfig-initialization-sequence.md)
