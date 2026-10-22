# initialization config C API: Filesystem encoding and interpreter home configuration

wchar_t *filesystem_encoding

[Filesystem encoding](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler): [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding).

On macOS, Android and VxWorks: defaults to `"utf-8"`.

On Windows: defaults to `"utf-8"`, or `"mbcs"` whenever `legacy_windows_fs_encoding` of `PyPreConfig` is non-zero.

The default encoding elsewhere:

- `"utf-8"` whenever `PyPreConfig.utf8_mode` is non-zero.

- `"ascii"` when Python finds that `nl_langinfo(CODESET)` reports the ASCII encoding, while the `mbstowcs()` function decodes from some other encoding (commonly Latin1).

- `"utf-8"` when `nl_langinfo(CODESET)` yields an empty string.

- In all other cases, the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding) is used: the `nl_langinfo(CODESET)` result.

During Python startup, the encoding name gets normalized into the Python codec name. To take one case, `"ANSI_X3.4-1968"` becomes `"ascii"`.

See also the `filesystem_errors` member.

 wchar_t *filesystem_errors

[Filesystem error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler): [`sys.getfilesystemencodeerrors()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencodeerrors).

On Windows: defaults to `"surrogatepass"`, or `"replace"` whenever `legacy_windows_fs_encoding` of `PyPreConfig` is non-zero.

Elsewhere: defaults to `"surrogateescape"`.

Supported error handlers:

- `"strict"`

- `"surrogateescape"`

- `"surrogatepass"` (available only with the UTF-8 encoding)

See also the `filesystem_encoding` member.

 int use_frozen_modules

When non-zero, frozen modules are used.

Assigned by the [`PYTHON_FROZEN_MODULES`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_FROZEN_MODULES) environment variable.

Default: `1` for a release build, or `0` for a [debug build](https://docs.python.org/3.14/using/configure.html#debug-build).

 unsigned long hash_seed

 int use_hash_seed

The randomized hash function seed.

Where `use_hash_seed` is zero, a seed is picked at random during Python startup and `hash_seed` is disregarded.

Assigned by the [`PYTHONHASHSEED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHASHSEED) environment variable.

Default *use_hash_seed* value: `-1` in Python mode, `0` in isolated mode.

 wchar_t *home

Establish the default Python "home" directory, namely where the standard Python libraries reside (refer to [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME)).

Assigned by the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable.

Default: `NULL`.

Part of the Python Path Configuration input.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](dev-mode-to-faulthandler.md) · [Following source contract](import-time-to-isolated.md)
