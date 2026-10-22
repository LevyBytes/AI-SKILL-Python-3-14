# sys.stdin, sys.stdout, sys.stderr

sys.stdin

sys.stdout

sys.stderr

The [File objects](https://docs.python.org/3.14/glossary.html#term-file-object) the interpreter relies on for standard input, output and errors:

- every bit of interactive input goes through `stdin` (calls to [`input()`](https://docs.python.org/3.14/library/functions.html#input) among them);

- output from [`print()`](https://docs.python.org/3.14/library/functions.html#print), from [expression](https://docs.python.org/3.14/glossary.html#term-expression) statements, and the prompts shown by [`input()`](https://docs.python.org/3.14/library/functions.html#input) all travel through `stdout`;

- `stderr` receives the interpreter’s own prompts along with its error messages.

These streams are ordinary [text files](https://docs.python.org/3.14/glossary.html#term-text-file), of the sort the [`open()`](https://docs.python.org/3.14/library/functions.html#open) function returns. Here is how their parameters get decided:

- Both the encoding and the error handling take their starting values from [`PyConfig.stdio_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.stdio_encoding) and [`PyConfig.stdio_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.stdio_errors).

Under Windows the console device runs on UTF-8. Non-character devices like disk files and pipes fall back to the system locale encoding (that is, the ANSI codepage). Non-console character devices such as NUL — those where `isatty()` yields `True` — take whatever the console input and output codepages held at startup, used for stdin and for stdout/stderr respectively. When the process never attaches to a console to begin with, that defaults to the system [locale encoding](https://docs.python.org/3.14/glossary.html#term-locale-encoding).

You can override the console’s special behaviour by defining the environment variable PYTHONLEGACYWINDOWSSTDIO before Python launches. With that set, the console codepages serve just as they would for any other character device.

On every platform you may override the character encoding by defining the [`PYTHONIOENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONIOENCODING) environment variable ahead of starting Python, or through the new [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `utf8` command line option together with the [`PYTHONUTF8`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUTF8) environment variable. For the Windows console, though, that holds only when [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO) has been set as well.

- In interactive use the `stdout` stream is line-buffered; otherwise it is block-buffered, just like ordinary text files. The `stderr` stream stays line-buffered either way. To strip the buffering from both streams, hand in the [`-u`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-u) command-line option or define the [`PYTHONUNBUFFERED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUNBUFFERED) environment variable.

Changed in version 3.9: In non-interactive use `stderr` is now line-buffered rather than fully buffered.

Note

For reading or writing binary data across the standard streams, work through the underlying binary [`buffer`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.buffer) object. As one example, to push bytes out to `stdout`, call `sys.stdout.buffer.write(b'abc')`.

That said, when you are authoring a library — with no say over the context its code ends up running in — keep in mind the standard streams could be swapped for file-like objects such as [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO), which offer no `buffer` attribute.

[API family](INDEX.md) · [sys context index](../INDEX.md).
