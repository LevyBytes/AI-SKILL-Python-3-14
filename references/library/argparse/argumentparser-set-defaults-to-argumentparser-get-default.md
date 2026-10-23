# argparse - Parser defaults

### Parser defaults

 ArgumentParser.set_defaults(***kwargs*)

In the usual case, every attribute on the object that `parse_args()` returns gets pinned down by looking at the command-line arguments together with the argument actions. With `set_defaults()` you can tack on extra attributes whose values are fixed without any reference to the command line at all:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', type=int)
>>> parser.set_defaults(bar=42, baz='badger')
>>> parser.parse_args(['736'])
Namespace(bar=42, baz='badger', foo=736)

```

Bear in mind that defaults may be established at two levels: across the parser via `set_defaults()` and per argument via `add_argument()`. When both paths apply to one argument, whichever default was assigned last wins:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default='bar')
>>> parser.set_defaults(foo='spam')
>>> parser.parse_args([])
Namespace(foo='spam')

```

Defaults set at the parser level come in especially handy once several parsers are in play. The `add_subparsers()` method shows an example of exactly this kind.

 ArgumentParser.get_default(*dest*)

Fetches a namespace attribute's default value, whether that default came from `add_argument()` or from `set_defaults()`:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default='badger')
>>> parser.get_default('foo')
'badger'

```

[Subject index](INDEX.md) · [Previous](mutual-exclusion.md) · [Continue](argumentparser-print-usage-to-argumentparser-format-help.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
