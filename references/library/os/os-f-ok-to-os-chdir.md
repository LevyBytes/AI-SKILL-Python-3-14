# os: `os.F_OK`, `os.R_OK`, `os.W_OK`, `os.X_OK`, `os.chdir()`

When *effective_ids* is `True`, `access()` runs its access checks against the effective uid/gid rather than the real uid/gid. Your platform might not provide *effective_ids*; you can confirm whether it is present by checking `os.supports_effective_ids`. Where it is missing, using it raises a [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Note

Calling `access()` to verify that a user may, say, open a file before they actually do so with [`open()`](https://docs.python.org/3.14/library/functions.html#open) opens a security hole, since the user could exploit the brief window between the check and the open to tamper with the file. Favor [EAFP](https://docs.python.org/3.14/glossary.html#term-EAFP) techniques instead. As an example:

```python
if os.access("myfile", os.R_OK):
    with open("myfile") as fp:
        return fp.read()
return "some default data"

```

is better written as:

```python
try:
    fp = open("myfile")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()

```

Note

Even when `access()` reports that an I/O operation should succeed, that operation can still fail, especially on network filesystems whose permission semantics go beyond the ordinary POSIX permission-bit model.

Changed in version 3.3: Added the *dir_fd*, *effective_ids*, and *follow_symlinks* parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.F_OK

 os.R_OK

 os.W_OK

 os.X_OK

Values to hand to the *mode* parameter of `access()` to check, respectively, the existence, readability, writability and executability of *path*.

 os.chdir(*path*)

Switch the current working directory to *path*.

This function can support specifying a file descriptor. The descriptor has to reference an opened directory, not an open file.

This function can raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) and subclasses such as [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError), [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError), and [`NotADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#NotADirectoryError).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.chdir` with argument `path`.

Changed in version 3.3: On some platforms, *path* may now be given as a file descriptor.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Continue](os-chflags-to-stat-sf-snapshot.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Files and Directories](os-access.md) · [Owning module, declaration or section: os.access](os-access.md) · [Preceding source contract and version conditions](os-access.md)
