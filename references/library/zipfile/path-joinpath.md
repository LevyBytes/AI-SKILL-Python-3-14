# zipfile: `Path.joinpath()`

Path.joinpath(**other*)

Hand back a fresh Path object that has every one of the *other* arguments joined on. These amount to the same thing:

```python
>>> Path(...).joinpath('child').joinpath('grandchild')
>>> Path(...).joinpath('child', 'grandchild')
>>> Path(...) / 'child' / 'grandchild'

```

Changed in version 3.10: Ahead of 3.10, `joinpath` went undocumented and took precisely one parameter.

The [zipp](https://pypi.org/project/zipp/) project supplies backports of the newest path object functionality to earlier Pythons. Swap in `zipp.Path` wherever you'd use `zipfile.Path` for early access to upcoming changes.

[Subject index](INDEX.md) · [Previous](path-name-to-path-read-bytes.md) · [Continue](zipfile-pyzipfile-class.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Owning module, declaration or section: zipfile.Path](zipfile-path-class.md) · [Owning module, declaration or section: Path objects](zipfile-path-class.md)
