# initialization config C API: Locale coercion, environment and UTF-8 preconfiguration

int coerce_c_locale

When this equals `2`, coerce the C locale.

When this equals `1`, inspect the LC_CTYPE locale to determine whether coercion is warranted.

Refer to the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding).

Default: `-1` in Python config, `0` in isolated config.

 int coerce_c_locale_warn

When non-zero, raise a warning should the C locale be coerced.

Default: `-1` in Python config, `0` in isolated config.

 int dev_mode

[Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode): refer to `PyConfig.dev_mode`.

Default: `-1` in Python mode, `0` in isolated mode.

 int isolated

Isolated mode: refer to `PyConfig.isolated`.

Default: `0` in Python mode, `1` in isolated mode.

 int legacy_windows_fs_encoding

When non-zero:

- Force `PyPreConfig.utf8_mode` to `0`,

- Force `PyConfig.filesystem_encoding` to `"mbcs"`,

- Force `PyConfig.filesystem_errors` to `"replace"`.

Seeded from the value of the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable.

Present only on Windows. The `#ifdef MS_WINDOWS` macro is available for Windows-specific code.

Default: `0`.

 int parse_argv

When non-zero, `Py_PreInitializeFromArgs()` and `Py_PreInitializeFromBytesArgs()` interpret their `argv` argument exactly as standard Python interprets command-line arguments: refer to [Command Line Arguments](https://docs.python.org/3.14/using/cmdline.html#using-on-cmdline).

Default: `1` in Python config, `0` in isolated config.

 int use_environment

Consult [environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-envvars)? Refer to `PyConfig.use_environment`.

Default: `1` in Python config and `0` in isolated config.

 int utf8_mode

When non-zero, switch on the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode).

Driven to `0` or `1` by the [`-X utf8`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option together with the [`PYTHONUTF8`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUTF8) environment variable.

Also driven to `1` whenever the `LC_CTYPE` locale is `C` or `POSIX`.

Default: `-1` in Python config and `0` in isolated config.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pypreconfig-to-configure-locale.md) · [Following source contract](py-preinitialize-to-py-preinitializefrombytesargs.md)
