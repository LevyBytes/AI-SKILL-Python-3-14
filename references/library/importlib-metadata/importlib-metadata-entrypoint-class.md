# importlib.metadata: `importlib.metadata.EntryPoint`

*class *importlib.metadata.EntryPoint

Details of an installed entry point.

Every `EntryPoint` instance carries `.name`, `.group`, and `.value` attributes along with a `.load()` method that resolves the value. It also has `.module`, `.attr`, and `.extras` attributes for pulling apart the pieces of the `.value` attribute, plus `.dist` to fetch information about the distribution package supplying the entry point.

Query all entry points:

```python
>>> eps = entry_points()

```

The `entry_points()` function hands back an `EntryPoints` object — a collection of every `EntryPoint` object, with `names` and `groups` attributes for convenience:

```python
>>> sorted(eps.groups)
['console_scripts', 'distutils.commands', 'distutils.setup_keywords', 'egg_info.writers', 'setuptools.installation']

```

`EntryPoints` carries a `select()` method that picks entry points matching given properties. Select entry points within the `console_scripts` group:

```python
>>> scripts = eps.select(group='console_scripts')

```

The same result, given that `entry_points()` forwards keyword arguments to select:

```python
>>> scripts = entry_points(group='console_scripts')

```

Single out a particular script called “wheel” (provided by the wheel project):

```python
>>> 'wheel' in scripts.names
True
>>> wheel = scripts['wheel']

```

The same result, querying for that entry point at selection time:

```python
>>> (wheel,) = entry_points(group='console_scripts', name='wheel')
>>> (wheel,) = entry_points().select(group='console_scripts', name='wheel')

```

Examine the resolved entry point:

```python
>>> wheel
EntryPoint(name='wheel', value='wheel.cli:main', group='console_scripts')
>>> wheel.module
'wheel.cli'
>>> wheel.attr
'main'
>>> wheel.extras
[]
>>> main = wheel.load()
>>> main
<function main at 0x103528488>

```

The `group` and `name` are arbitrary values set by the package author, and usually a client wants to resolve every entry point for a given group. Consult [the setuptools docs](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) for further detail on entry points, how they are defined, and how they are used.

Changed in version 3.12: The “selectable” entry points arrived in `importlib_metadata` 3.6 and Python 3.10. Before those changes, `entry_points` took no parameters and always handed back a dictionary of entry points keyed by group. As of `importlib_metadata` 5.0 and Python 3.12, `entry_points` always returns an `EntryPoints` object. Refer to [backports.entry_points_selectable](https://pypi.org/project/backports.entry_points_selectable/) for compatibility options.

Changed in version 3.13: `EntryPoint` objects no longer expose a tuple-like interface ([`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__)).

[Subject index](INDEX.md) · [Previous](importlib-metadata-entrypoints-class.md) · [Continue](importlib-metadata-metadata.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md) · [Owning module, declaration or section: Entry points](importlib-metadata-entry-points.md)
