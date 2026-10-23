# posix`posix` - The most common POSIX system calls

## posix - The most common POSIX system calls

### `posix` - The most common POSIX system calls

---

Through this module you reach operating-system features that the C Standard and the POSIX standard define (a lightly veiled Unix interface).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

**Do not import this module directly.** Reach for the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module instead, since it offers a *portable* take on this same interface. Under Unix the `os` module is a superset of what `posix` exposes. Where the OS isn’t Unix, `posix` simply doesn’t exist, yet a subset of it always shows up via the `os` interface. After `os` has been imported, choosing it over `posix` costs you *no* speed. On top of that, `os` adds extra behavior — for instance it calls [`putenv()`](https://docs.python.org/3.14/library/os.html#os.putenv) on its own whenever an `os.environ` entry changes.

Problems surface as exceptions: type mistakes raise the customary exceptions, whereas anything the system calls report back becomes an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

[Subject index](INDEX.md) · [Continue](large-file-support.md)
