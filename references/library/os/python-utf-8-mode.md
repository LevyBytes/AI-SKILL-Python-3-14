# os - Python UTF-8 Mode

### Python UTF-8 Mode

Added in version 3.7: See [**PEP 540**](https://peps.python.org/pep-0540/) for more details.

The Python UTF-8 Mode disregards the [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding) and mandates that the UTF-8 encoding be used:

- Use UTF-8 for the [filesystem encoding](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

- [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding) returns `'utf-8'`.

- [`locale.getpreferredencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getpreferredencoding) returns `'utf-8'` (the *do_setlocale* argument has no effect).

- [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin), [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout), and [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) each adopt UTF-8 as their text encoding, with the `surrogateescape` [error handler](https://docs.python.org/3.14/library/codecs.html#error-handlers) turned on for `sys.stdin` and `sys.stdout` (`sys.stderr` keeps using `backslashreplace`, just as it does in the default locale-aware mode)

- Under Unix, `os.device_encoding()` returns `'utf-8'` in place of the device encoding.

Bear in mind that the standard stream settings under UTF-8 mode can be overridden by [`PYTHONIOENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONIOENCODING) (exactly as they can in the default locale-aware mode).

Following from the changes within those lower level APIs, several higher level APIs likewise show altered default behaviours:

- Command line arguments, environment variables and filenames get decoded to text by way of the UTF-8 encoding.

- `os.fsdecode()` and `os.fsencode()` employ the UTF-8 encoding.

- [`open()`](https://docs.python.org/3.14/library/functions.html#open), [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open), and [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open) employ the UTF-8 encoding by default. Even so, they still keep the strict error handler by default, so trying to open a binary file in text mode is apt to raise an exception rather than yield nonsense data.

The Python UTF-8 Mode switches on whenever the LC_CTYPE locale is `C` or `POSIX` at Python startup (see the [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read) function).

You can switch it on or off through the [`-X utf8`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option and the [`PYTHONUTF8`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUTF8) environment variable.

Where the [`PYTHONUTF8`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUTF8) environment variable goes unset entirely, the interpreter falls back to the current locale settings, *unless* the current locale is recognized as a legacy ASCII-based locale (as spelled out for [`PYTHONCOERCECLOCALE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONCOERCECLOCALE)), with locale coercion either off or failing. Inside such legacy locales, the interpreter defaults to turning on UTF-8 mode unless told explicitly to refrain.

The Python UTF-8 Mode can be turned on only at Python startup. Its value is readable from [`sys.flags.utf8_mode`](https://docs.python.org/3.14/library/sys.html#sys.flags).

See also the [UTF-8 mode on Windows](https://docs.python.org/3.14/using/windows.html#win-utf8-mode) and the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler).

See also

[**PEP 686**](https://peps.python.org/pep-0686/)

Python 3.15 will make Python UTF-8 Mode default.

[Subject index](INDEX.md) · [Previous](file-names-command-line-arguments-and-environment-variables.md) · [Continue](os-ctermid-to-os-fsencode.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
