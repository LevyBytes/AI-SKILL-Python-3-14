# What’s New In Python 3.8 / New Modules - importlib.metadata

> (Contributed by Pierre Glaser and Olivier Grisel in [bpo-35900](https://bugs.python.org/issue?@action=redirect&bpo=35900).)

### New Modules

- A fresh [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata) module ships (provisionally) so you may read metadata belonging to third-party packages. As one illustration, it can pull an installed package's version, the roster of entry points, plus other details:

```python
>>> # Note following example requires that the popular "requests"
>>> # package has been installed.
>>>
>>> from importlib.metadata import version, requires, files
>>> version('requests')
'2.22.0'
>>> list(requires('requests'))
['chardet (<3.1.0,>=3.0.2)']
>>> list(files('requests'))[:5]
[PackagePath('requests-2.22.0.dist-info/INSTALLER'),
 PackagePath('requests-2.22.0.dist-info/LICENSE'),
 PackagePath('requests-2.22.0.dist-info/METADATA'),
 PackagePath('requests-2.22.0.dist-info/RECORD'),
 PackagePath('requests-2.22.0.dist-info/WHEEL')]

```

[Subject index](INDEX.md) · [Previous source section](object-reduction-and-pickle-protocol.md) · [Next source section](ast.md) · [Release/subject declaration](assignment-expressions.md) · [Preceding release/subject continuation](modular-inverses-and-language-changes.md)
