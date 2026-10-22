# argparse — action — Code example: >>> parser = argparse.ArgumentParser()

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--verbose', '-v', action='count', default=0)
>>> parser.parse_args(['-vvv'])
Namespace(verbose=3)

```

Keep in mind that the *default* stays `None` unless you set it to *0* yourself.

- `'help'` - Emits a full help message covering every option in the current parser, then exits. A help action gets attached to the parser automatically by default. Consult `ArgumentParser` to learn how that output gets assembled.

- `'version'` - Looks for a `version=` keyword argument in the `add_argument()` call, and once triggered it prints version details and exits:

```python
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
>>> parser.parse_args(['--version'])
PROG 2.0

```

You are also free to plug in any action of your own by handing over an `Action` subclass (for instance `BooleanOptionalAction`) or some other object honoring the same interface. Bear in mind that only actions which actually consume command-line arguments (such as `'store'`, `'append'`, `'extend'`, or custom actions whose `nargs` is non-zero) work alongside positional arguments.

To build a custom action, the suggested approach is to subclass `Action`, providing your own `__call__()` method and, if you like, your own `__init__()` and `format_usage()` methods. Another option is to register your custom actions through the `register()` method and then refer to them by the name you registered.

Here is a custom action shown in use:

```python
>>> class FooAction(argparse.Action):
...     def __init__(self, option_strings, dest, nargs=None, **kwargs):
...         if nargs is not None:
...             raise ValueError("nargs not allowed")
...         super().__init__(option_strings, dest, **kwargs)
...     def __call__(self, parser, namespace, values, option_string=None):
...         print('%r %r %r' % (namespace, values, option_string))
...         setattr(namespace, self.dest, values)
...
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action=FooAction)
>>> parser.add_argument('bar', action=FooAction)
>>> args = parser.parse_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
>>> args
Namespace(bar='1', foo='2')

```

To go deeper, refer to `Action`.

[Subject index](INDEX.md) · [Previous](action-section-introduction-and-initial-examples.md) · [Continue](nargs.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: action](action-section-introduction-and-initial-examples.md)
