# PyConfig.parser_debug

int parser_debug

The parser debug mode. When above `0`, parser debugging output is switched on (for experts only, contingent on compilation options).
Bumped up by the [`-d`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-d) command line option, and given the value held in the [`PYTHONDEBUG`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDEBUG) environment variable.

Requires a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build) (the `Py_DEBUG` macro has to be defined).

Default: `0`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](orig-argv-to-parse-argv.md) · [Previous source contract](pathconfig-warnings.md)
