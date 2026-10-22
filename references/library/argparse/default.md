# argparse — default

### default

Every optional argument, along with certain positional ones, can be left off the command line. The `default` keyword argument to `add_argument()`, which itself defaults to `None`, says what value to substitute when the command-line argument is missing. For optional arguments, that `default` kicks in whenever the option string was absent from the command line:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=42)
>>> parser.parse_args(['--foo', '2'])
Namespace(foo='2')
>>> parser.parse_args([])
Namespace(foo=42)

```

Should the target namespace already carry an attribute, the action *default* leaves it untouched:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=42)
>>> parser.parse_args([], namespace=argparse.Namespace(foo=101))
Namespace(foo=101)

```

When the `default` happens to be a string, the parser treats that value as though it had come straight off the command line. Specifically, it runs any supplied type conversion argument over the value before placing the attribute onto the `Namespace` it returns. Failing that, the parser leaves the value untouched:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--length', default='10', type=int)
>>> parser.add_argument('--width', default=10.5, type=int)
>>> parser.parse_args()
Namespace(length=10, width=10.5)

```

When a positional argument has nargs of `?` or `*`, its `default` value applies whenever no command-line argument turned up:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', nargs='?', default=42)
>>> parser.parse_args(['a'])
Namespace(foo='a')
>>> parser.parse_args([])
Namespace(foo=42)

```

Since `nargs='*'` collects whatever values are given into a list, a positional argument that is missing produces an empty list (`[]`). This only changes when *default* is something other than `None` (so `default=None` still yields `[]`).

When an argument is required, its `default` value gets disregarded. That covers, for instance, positional arguments whose nargs is anything besides `?` or `*`, as well as optional arguments flagged `required=True`.

Setting `default=argparse.SUPPRESS` means that no attribute is added at all when the command-line argument was missing:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=argparse.SUPPRESS)
>>> parser.parse_args([])
Namespace()
>>> parser.parse_args(['--foo', '1'])
Namespace(foo='1')

```

[Subject index](INDEX.md) · [Previous](const.md) · [Continue](type.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
