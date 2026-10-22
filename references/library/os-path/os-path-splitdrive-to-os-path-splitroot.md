# os.path: `os.path.splitdrive()`, `os.path.splitroot()`

os.path.splitdrive(*path*, */*)

Break the pathname *path* apart into a pair `(drive, tail)`; here *drive* is a mount point, or else the empty string. Where a system uses no drive specifications, *drive* always comes out as the empty string. Across every case, `drive + tail` will equal *path*.

Under Windows, a pathname is split into a drive/UNC sharepoint and a relative path.

When the path holds a drive letter, drive captures everything up to and including the colon:

```python
>>> splitdrive("c:/dir")
("c:", "/dir")

```

When the path holds a UNC path, drive captures the host name plus the share:

```python
>>> splitdrive("//host/computer/dir")
("//host/computer", "/dir")

```

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.splitroot(*path*, */*)

Break the pathname *path* apart into a 3-item tuple `(drive, root, tail)`, in which *drive* is a device name or mount point, *root* is a run of separators after the drive, and *tail* is whatever follows the root. Each of these items may turn out to be the empty string. Across every case, `drive + root + tail` will equal *path*.

Under POSIX systems, *drive* is invariably empty. The *root* may be empty (when *path* is relative), a lone forward slash (when *path* is absolute), or a pair of forward slashes (implementation-defined per [IEEE Std 1003.1-2017; 4.13 Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_13).) As an example:

```python
>>> splitroot('/home/sam')
('', '/', 'home/sam')
>>> splitroot('//home/sam')
('', '//', 'home/sam')
>>> splitroot('///home/sam')
('', '/', '//home/sam')

```

Under Windows, the choices for *drive* run from empty to a drive-letter name, a UNC share, or a device name. For *root*, the options are empty, a forward slash, or a backward slash. As an example:

```python
>>> splitroot('C:/Users/Sam')
('C:', '/', 'Users/Sam')
>>> splitroot('//Server/Share/Users/Sam')
('//Server/Share', '/', 'Users/Sam')

```

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](os-path-normpath-to-os-path-split.md) · [Continue](os-path-splitext-to-os-path-supports-unicode-filenames.md) · [Owning module, declaration or section: os.path](os-path-abspath-to-os-path-dirname.md)
