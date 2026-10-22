# os.path: `os.path.isjunction()`, `os.path.islink()`, `os.path.ismount()`, `os.path.isdevdrive()`, `os.path.isreserved()`, `os.path.join()`, `os.path.normcase()`

os.path.isjunction(*path*)

Yield `True` when *path* names an `existing` directory entry that happens to be a junction. When the current platform offers no junction support, the result is always `False`.

Added in version 3.12.

 os.path.islink(*path*)

Yield `True` when *path* names an `existing` directory entry that happens to be a symbolic link. The result is always `False` when the Python runtime offers no support for symbolic links.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.ismount(*path*)

Yield `True` when pathname *path* is a *mount point*: a spot in a file system at which a separate file system has been attached. Under POSIX, the routine tests whether the parent of *path*, `*path*/..`, sits on a device other than *path*, or whether `*path*/..` and *path* land on the same i-node of the same device — which should pick out mount points across all Unix and POSIX variants. Bind mounts on the same filesystem cannot be detected dependably this way. Under Linux, btrfs subvolumes always come back as `True`, even where they are not actually mount points. Under Windows, both a drive letter root and a share UNC always count as mount points, and for every other path `GetVolumePathName` gets invoked to determine whether it differs from the supplied path.

Changed in version 3.4: Under Windows, detection of mount points that are not the root gained support.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.isdevdrive(*path*)

Yield `True` when pathname *path* resides on a Windows Dev Drive. Tuned for developer workflows, a Dev Drive delivers quicker file reads and writes. The recommended uses include source code, throwaway build directories, package caches, and other operations heavy on IO.

For an invalid path — say, one lacking any recognizable drive — an error may be raised, but on platforms with no Dev Drive support the result is `False`. Details on turning on and creating Dev Drives are in [the Windows documentation](https://learn.microsoft.com/windows/dev-drive/).

Added in version 3.12.

Changed in version 3.13: every platform now offers the function, which always gives back `False` wherever Dev Drives are unsupported

 os.path.isreserved(*path*)

Yield `True` when *path* is a reserved pathname under the current system.

Under Windows, the reserved filenames take in those closing with a space or a dot; those carrying colons (that is, file streams such as "name:stream"), wildcard characters (that is, `'*?"<>'`), a pipe, or ASCII control characters; plus DOS device names like "NUL", "CON", "CONIN$", "CONOUT$", "AUX", "PRN", "COM1", and "LPT1".

Note

The rules this function applies for reserved paths are an approximation that holds on most Windows systems. Those rules shift over time across the various Windows releases. As rule changes reach broad availability, future Python releases may update this function.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Added in version 3.13.

 os.path.join(*path*, */*, **paths*)

Combine one or more path segments in a sensible way. What comes back is *path* joined with every member of **paths*, placing exactly one directory separator after each non-empty piece save the last. In other words, the result finishes with a separator only when the final piece is empty or itself ends with a separator.

When a segment is an absolute path (which under Windows demands both a drive and a root), every earlier segment is discarded and the join carries on from that absolute path segment. Take Linux as an example:

```python
>>> os.path.join('/home/foo', 'bar')
'/home/foo/bar'
>>> os.path.join('/home/foo', '/home/bar')
'/home/bar'

```

Under Windows, hitting a rooted path segment (such as `r'\foo'`) does not reset the drive. When a segment lies on another drive or is an absolute path, every earlier segment is discarded and the drive is reset. As an example:

```python
>>> os.path.join('c:\\', 'foo')
'c:\\foo'
>>> os.path.join('c:\\foo', 'd:\\bar')
'd:\\bar'

```

Keep in mind that because every drive carries its own current directory, `os.path.join("c:", "foo")` denotes a path taken relative to the current directory on drive `C:` (`c:foo`), not `c:\foo`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for *path* and *paths*.

 os.path.normcase(*path*, */*)

Bring the case of a pathname into a normal form. Under Windows, every character in the pathname is lowercased and forward slashes are turned into backward slashes as well. On the other operating systems, the path is handed back untouched.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](os-path-exists-to-os-path-isdir.md) · [Continue](os-path-normpath-to-os-path-split.md) · [Owning module, declaration or section: os.path](os-path-abspath-to-os-path-dirname.md)
