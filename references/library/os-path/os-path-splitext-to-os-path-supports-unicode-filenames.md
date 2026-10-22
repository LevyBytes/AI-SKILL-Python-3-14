# os.path: `os.path.splitext()`, `os.path.supports_unicode_filenames`

os.path.splitext(*path*, */*)

Break the pathname *path* apart into a pair `(root, ext)` for which `root + ext == path`, where the extension, *ext*, is either empty or opens with a period and holds at most one period.

When the path carries no extension, *ext* will be `''`:

```python
>>> splitext('bar')
('bar', '')

```

When the path carries an extension, *ext* will hold that extension, the leading period included. Note that any earlier periods are disregarded:

```python
>>> splitext('foo.bar.exe')
('foo.bar', '.exe')
>>> splitext('/foo/bar.exe')
('/foo/bar', '.exe')

```

Leading periods on the path's last component count as belonging to the root:

```python
>>> splitext('.cshrc')
('.cshrc', '')
>>> splitext('/foo/....jpg')
('/foo/....jpg', '')

```

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 os.path.supports_unicode_filenames

`True` when arbitrary Unicode strings are usable as file names (subject to limits the file system imposes).

[Subject index](INDEX.md) · [Previous](os-path-splitdrive-to-os-path-splitroot.md) · [Continue](../ossaudiodev/ossaudiodev-access-to-oss-compatible-audio-devices.md) · [Owning module, declaration or section: os.path](os-path-abspath-to-os-path-dirname.md)
