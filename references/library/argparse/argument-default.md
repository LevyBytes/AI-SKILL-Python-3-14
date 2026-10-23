# argparse - argument_default

### argument_default

As a rule, argument defaults come either from a default passed to `add_argument()` or from a call to the `set_defaults()` methods carrying a particular collection of name-value pairs. Now and then, though, setting one parser-wide default across all arguments proves handy. You pull that off by feeding the `argument_default=` keyword argument to `ArgumentParser`. For instance, to globally hold back attribute creation during `parse_args()` calls, we pass `argument_default=SUPPRESS`:

```python
>>> parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar', nargs='?')
>>> parser.parse_args(['--foo', '1', 'BAR'])
Namespace(bar='BAR', foo='1')
>>> parser.parse_args([])
Namespace()

```

[Subject index](INDEX.md) · [Previous](fromfile-prefix-chars.md) · [Continue](allow-abbrev.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
