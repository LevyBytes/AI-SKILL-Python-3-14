# initialization config C API: Presite imports and standard-stream encoding

wchar_t *run_presite

A `package.module` path naming the module to load ahead of `site.py` running.

Established through the [`-X presite=package.module`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option as well as the [`PYTHON_PRESITE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_PRESITE) environment variable, with the command-line option winning out.

Requires a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build) (the `Py_DEBUG` macro has to be defined).

Default: `NULL`.

 int show_ref_count

Report the overall reference count on exit (leaving out [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) objects)?

Turned to `1` by the [`-X showrefcount`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option.

Requires a [debug build of Python](https://docs.python.org/3.14/using/configure.html#debug-build) (the `Py_REF_DEBUG` macro has to be defined).

Default: `0`.

 int site_import

Load the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module during startup?

A value of zero turns off importing the module site along with the site-dependent edits to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) that come with it.

Those edits stay off too even when the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module is imported explicitly afterward (invoke [`site.main()`](https://docs.python.org/3.14/library/site.html#site.main) if you do want them applied).

Turned to `0` by the [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) command line option.

[`sys.flags.no_site`](https://docs.python.org/3.14/library/sys.html#sys.flags) receives the negated value of `site_import`.

Default: `1`.

 int skip_source_first_line

When non-zero, drop the opening line of the `PyConfig.run_filename` source.

This permits non-Unix spellings of `#!cmd` and exists purely as a DOS-specific workaround.

Turned to `1` by the [`-x`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-x) command line option.

Default: `0`.

 wchar_t *stdio_encoding

 wchar_t *stdio_errors

The encoding plus the encoding-error policy for [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout), and [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) (though `sys.stderr` sticks to the `"backslashreplace"` error handler at all times).

Draw on the [`PYTHONIOENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONIOENCODING) environment variable whenever it is non-empty.

Default encoding:

- `"UTF-8"` whenever `PyPreConfig.utf8_mode` is non-zero.

- Failing that, fall back to the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding).

Default error handler:

- Under Windows, go with `"surrogateescape"`.

- `"surrogateescape"` whenever `PyPreConfig.utf8_mode` is non-zero, or where the LC_CTYPE locale is “C” or “POSIX”.

- `"strict"` in every other case.

Consult also `PyConfig.legacy_windows_stdio`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](prefix-to-run-module.md) · [Following source contract](tracemalloc-to-verbose.md)
