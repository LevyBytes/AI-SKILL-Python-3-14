# argparse - The Namespace object

### The Namespace object

 *class *argparse.Namespace

A plain class that `parse_args()` uses by default to build and return an object that carries the attributes.

The class is intentionally bare-bones, merely an [`object`](https://docs.python.org/3.14/library/functions.html#object) subclass that prints a legible string. Should you want a dict-style view of its attributes, reach for the standard Python idiom [`vars()`](https://docs.python.org/3.14/library/functions.html#vars):

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> args = parser.parse_args(['--foo', 'BAR'])
>>> vars(args)
{'foo': 'BAR'}

```

Sometimes you'd rather an `ArgumentParser` set its attributes on an object that already exists instead of a fresh `Namespace`. Do so by passing the `namespace=` keyword argument:

```python
>>> class C:
...     pass
...
>>> c = C()
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
>>> c.foo
'BAR'

```

[Subject index](INDEX.md) · [Previous](beyond-sys-argv.md) · [Continue](argumentparser-add-subparsers.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
