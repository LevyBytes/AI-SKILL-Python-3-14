# glob — Examples

### Examples

Picture a directory holding these files: `1.gif`, `2.txt`, `card.gif` plus a subdirectory `sub` whose sole file is `3.txt`. `glob()` yields the results shown below. Observe how the leading parts of each path are kept.

```python
>>> import glob
>>> glob.glob('./[0-9].*')
['./1.gif', './2.txt']
>>> glob.glob('*.gif')
['1.gif', 'card.gif']
>>> glob.glob('?.gif')
['1.gif']
>>> glob.glob('**/*.txt', recursive=True)
['2.txt', 'sub/3.txt']
>>> glob.glob('./**/', recursive=True)
['./', './sub/']

```

When the directory holds files whose names begin with `.`, those go unmatched by default. As an example, take a directory holding `card.gif` and `.card.gif`:

```python
>>> import glob
>>> glob.glob('*.gif')
['card.gif']
>>> glob.glob('.c*')
['.card.gif']

```

See also

The [`fnmatch`](https://docs.python.org/3.14/library/fnmatch.html#module-fnmatch) module provides shell-style filename expansion (not path expansion).

See also

The [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) module provides high-level path objects.

[Subject index](INDEX.md) · [Previous](glob-translate.md) · [Continue](../graphlib/graphlib-topologicalsorter-class.md) · [Owning module, declaration or section: glob](glob-glob-to-glob-escape.md)
