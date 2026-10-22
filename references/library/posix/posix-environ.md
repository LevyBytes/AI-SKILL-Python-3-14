# posix — Notable Module Contents

### Notable Module Contents

On top of the many functions covered in the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module documentation, `posix` exposes this one data item:

`posix.environ`

A dictionary that captures the string environment as it stood when the interpreter began. On Unix the keys and values are bytes, on Windows they are str. As an illustration, `environ[b'HOME']` (`environ['HOME']` on Windows) holds the path to your home directory, the counterpart of `getenv("HOME")` in C.

Altering this dictionary has no bearing on the string environment that [`execv()`](https://docs.python.org/3.14/library/os.html#os.execv), [`popen()`](https://docs.python.org/3.14/library/os.html#os.popen) or [`system()`](https://docs.python.org/3.14/library/os.html#os.system) hands onward; to actually change the environment, hand `environ` to [`execve()`](https://docs.python.org/3.14/library/os.html#os.execve), or append variable assignments and export statements onto the command string fed to `system()` or `popen()`.

Changed in version 3.2: On Unix, keys and values are bytes.

Note

The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module ships its own version of `environ` that refreshes the environment as it is changed. Note too that once you touch [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ) this dictionary goes stale. Reaching for the `os` module’s flavor is preferable to going straight at the `posix` module.

[Subject index](INDEX.md) · [Previous](large-file-support.md) · [Owning module, declaration or section: posix](posix-the-most-common-posix-system-calls.md)
