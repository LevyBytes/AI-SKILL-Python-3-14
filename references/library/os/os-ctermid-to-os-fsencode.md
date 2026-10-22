# os: `os.ctermid()`, `os.environ`, `os.environb`, `os.reload_environ()`, `os.chdir()`, `os.fchdir()`, `os.getcwd()`, `os.fsencode()`

### Process Parameters

These functions and data items supply information about and act upon the current process and user.

 os.ctermid()

Return the filename that maps to the controlling terminal of the process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, not WASI.

 os.environ

A [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) object whose keys and values are strings standing for the process environment. As an example, `environ['HOME']` is the pathname of your home directory (on certain platforms), and matches `getenv("HOME")` in C.

This mapping gets captured the first time the `os` module is imported, ordinarily during Python startup while `site.py` is being processed. Environment changes made afterward do not show up in `os.environ`, save for changes you make by altering `os.environ` directly.

You can use this mapping both to alter the environment and to query it. `putenv()` gets invoked automatically whenever the mapping is altered.

Under Unix, keys and values rely on [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding) and the `'surrogateescape'` error handler. Turn to `environb` whenever you would prefer a different encoding.

Under Windows, the keys get converted to uppercase. That holds true when getting, setting, or deleting an item too. As an example, `environ['monty'] = 'python'` maps the key `'MONTY'` onto the value `'python'`.

Note

Invoking `putenv()` directly leaves `os.environ` unchanged, so altering `os.environ` is the better course.

Note

On certain platforms, FreeBSD and macOS among them, setting `environ` can produce memory leaks. Consult the system documentation covering `putenv()`.

You may delete items in this mapping to unset environment variables. `unsetenv()` gets invoked automatically once an item is deleted from `os.environ`, and once one of the `pop()` or `clear()` methods runs.

See also

The `os.reload_environ()` function.

Changed in version 3.9: Reworked so the merge (`|`) and update (`|=`) operators of [**PEP 584**](https://peps.python.org/pep-0584/) are supported.

 os.environb

Bytes version of `environ`: a [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) object whose keys and values are both [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects standing for the process environment. `environ` and `environb` stay synchronized (altering `environb` updates `environ`, and the other way round).

`environb` is only available if `supports_bytes_environ` is `True`.

Added in version 3.2.

Changed in version 3.9: Reworked so the merge (`|`) and update (`|=`) operators of [**PEP 584**](https://peps.python.org/pep-0584/) are supported.

 os.reload_environ()

The `os.environ` and `os.environb` mappings hold a cache of the environment variables as they stood when Python started. Because of that, changes to the current process environment do not show up when they are made outside Python, or via `os.putenv()` or `os.unsetenv()`. Call `os.reload_environ()` to bring `os.environ` and `os.environb` up to date with any such changes to the current process environment.

Warning

This function is not thread-safe. Calling it while another thread is altering the environment is undefined behavior. Reading from `os.environ` or `os.environb`, or calling `os.getenv()`, during a reload may yield an empty result.

Added in version 3.14.

 os.chdir(*path*)

 os.fchdir(*fd*)

 os.getcwd()

These functions are described in Files and Directories.

 os.fsencode(*filename*)

Encode [path-like](https://docs.python.org/3.14/glossary.html#term-path-like-object) *filename* to the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler); return [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) unchanged.

`fsdecode()` is the reverse function.

Added in version 3.2.

Changed in version 3.6: Now also accepts objects that implement the `os.PathLike` interface.

[Subject index](INDEX.md) · [Previous](python-utf-8-mode.md) · [Continue](os-fsdecode-to-os-fspath.md) · [Owning module, declaration or section: os](os-error-to-os-name.md)
