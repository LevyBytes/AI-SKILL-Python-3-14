# argparse — exit_on_error

### exit_on_error

Ordinarily, feeding an invalid argument list to the `parse_args()` method of an `ArgumentParser` makes it print a *message* to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) and quit with a status code of 2.

Should the user prefer to handle errors by hand, switching `exit_on_error` to `False` turns the feature on:

```python
>>> parser = argparse.ArgumentParser(exit_on_error=False)
>>> parser.add_argument('--integers', type=int)
_StoreAction(option_strings=['--integers'], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
>>> try:
...     parser.parse_args('--integers a'.split())
... except argparse.ArgumentError:
...     print('Catching an argumentError')
...
Catching an argumentError

```

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](add-help.md) · [Continue](suggest-on-error.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
