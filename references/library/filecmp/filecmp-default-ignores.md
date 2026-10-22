# filecmp: `filecmp.DEFAULT_IGNORES`

filecmp.DEFAULT_IGNORES

Added in version 3.4.

The directories that `dircmp` passes over out of the box.

What follows is a pared-down demonstration of leaning on the `subdirs` attribute to walk two directories recursively and surface the shared files that differ:

```python
>>> from filecmp import dircmp
>>> def print_diff_files(dcmp):
...     for name in dcmp.diff_files:
...         print("diff_file %s found in %s and %s" % (name, dcmp.left,
...               dcmp.right))
...     for sub_dcmp in dcmp.subdirs.values():
...         print_diff_files(sub_dcmp)
...
>>> dcmp = dircmp('dir1', 'dir2')
>>> print_diff_files(dcmp)

```

[Subject index](INDEX.md) · [Previous](filecmp-dircmp-report-to-filecmp-dircmp-report-full-closure.md) · [Continue](../fileformats/file-formats.md) · [Owning module, declaration or section: filecmp](filecmp-cmp-to-filecmp-clear-cache.md) · [Owning module, declaration or section: The `dircmp` class](filecmp-dircmp-class.md)
