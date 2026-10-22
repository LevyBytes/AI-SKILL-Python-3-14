# argparse — Registering custom types or actions

### Registering custom types or actions

 ArgumentParser.register(*registry_name*, *value*, *object*)

Now and then you want a custom string to appear in error messages so the output reads more kindly. For that, `register()` lets you attach custom actions or types to a parser, after which you can name the type by the label it was registered under rather than by its callable's name.

Three arguments go into `register()`: *registry_name*, which names the internal registry that will hold the object (`action` or `type`, for instance); *value*, the key the object is filed under; and object, the callable being registered.

Here is how registering a custom type on a parser looks in practice:

```python
>>> import argparse
>>> parser = argparse.ArgumentParser()
>>> parser.register('type', 'hexadecimal integer', lambda s: int(s, 16))
>>> parser.add_argument('--foo', type='hexadecimal integer')
_StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type='hexadecimal integer', choices=None, required=False, help=None, metavar=None, deprecated=False)
>>> parser.parse_args(['--foo', '0xFA'])
Namespace(foo=250)
>>> parser.parse_args(['--foo', '1.2'])
usage: PROG [-h] [--foo FOO]
PROG: error: argument --foo: invalid 'hexadecimal integer' value: '1.2'

```

[Subject index](INDEX.md) · [Previous](intermixed-argument-parsing.md) · [Continue](argparse-argumenterror-to-argparse-argumenttypeerror.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
