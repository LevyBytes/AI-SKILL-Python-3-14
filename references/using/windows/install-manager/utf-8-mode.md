# 4.7. UTF-8 mode

### 4.7. UTF-8 mode

Added in version 3.7.

Windows continues to rely on legacy encodings for its system encoding (the ANSI Code Page). Python draws on it as the default encoding for text files (for example, [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding)).

That can lead to trouble, since UTF-8 dominates the internet and most Unix systems, WSL (Windows Subsystem for Linux) among them.

The [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) lets you switch the default text encoding over to UTF-8. Turn the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) on either through the `-X utf8` command line option or through the `PYTHONUTF8=1` environment variable. Consult [`PYTHONUTF8`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUTF8) to learn how to switch UTF-8 mode on, and Python install manager to learn how to edit environment variables.

While the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) is active, the system encoding (the ANSI Code Page) remains reachable through the "mbcs" codec.

Be aware that placing `PYTHONUTF8=1` among the default environment variables changes the behavior of every Python 3.7+ application on the machine. If any of your Python 3.7+ applications depend on the legacy system encoding, the advice is to set that environment variable only temporarily or to fall back on the `-X utf8` command line option.

Note

Even with UTF-8 mode turned off, Python relies on UTF-8 by default on Windows for:

- Console I/O including standard I/O (see [**PEP 528**](https://peps.python.org/pep-0528/) for details).

- The [filesystem encoding](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) (see [**PEP 529**](https://peps.python.org/pep-0529/) for details).

[Subject index](INDEX.md) · [Previous source section](removing-the-max-path-limitation.md) · [Following source section](finding-modules.md)
