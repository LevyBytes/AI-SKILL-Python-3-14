# argparse - Intermixed parsing

### Intermixed parsing

 ArgumentParser.parse_intermixed_args(*args=None*, *namespace=None*)

 ArgumentParser.parse_known_intermixed_args(*args=None*, *namespace=None*)

Quite a few Unix commands let you mix optional arguments in among the positional ones. That parsing style is backed by the `parse_intermixed_args()` and `parse_known_intermixed_args()` methods.

Not every `argparse` feature is available with these parsers; reaching for an unsupported one raises an exception. Specifically, neither subparsers nor mutually exclusive groups holding both optionals and positionals are allowed.

The example coming up highlights how `parse_known_args()` and `parse_intermixed_args()` differ: the first leaves `['2', '3']` behind as unparsed arguments, whereas the second gathers every positional into `rest`.

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('cmd')
>>> parser.add_argument('rest', nargs='*', type=int)
>>> parser.parse_known_args('doit 1 --foo bar 2 3'.split())
(Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
>>> parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])

```

`parse_known_intermixed_args()` hands back a two-item tuple — the filled-in namespace alongside whatever argument strings are left over. `parse_intermixed_args()`, by contrast, raises an error should any unparsed argument strings remain.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](argumentparser-exit-to-argumentparser-error.md) · [Continue](argumentparser-register.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
