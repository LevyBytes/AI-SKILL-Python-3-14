# argparse — dest

### dest

The bulk of `ArgumentParser` actions attach some value as an attribute on the object that `parse_args()` returns. What that attribute gets named is set by the `dest` keyword argument of `add_argument()`. With positional argument actions, `dest` is usually given as the very first argument to `add_argument()`:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('bar')
>>> parser.parse_args(['XXX'])
Namespace(bar='XXX')

```

With optional argument actions, the `dest` value is normally worked out from the option strings. `ArgumentParser` arrives at the `dest` value by taking the first long option string and trimming off the leading `--`. When no long option strings were given, `dest` instead comes from the first short option string with its leading `-` removed. Every internal `-` is swapped for a `_` so that the resulting string is a legal attribute name. The examples that follow show how this works:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('-f', '--foo-bar', '--foo')
>>> parser.add_argument('-x', '-y')
>>> parser.parse_args('-f 1 -x 2'.split())
Namespace(foo_bar='1', x='2')
>>> parser.parse_args('--foo 1 -y 2'.split())
Namespace(foo_bar='1', x='2')

```

To supply your own attribute name, use `dest`:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', dest='bar')
>>> parser.parse_args('--foo XXX'.split())
Namespace(bar='XXX')

```

Several arguments are permitted to share one `dest`. The default behavior keeps only the value of whichever such argument appeared last on the command line. To instead gather every value into a list, apply `action='append'`. When the clash is between *option strings* and not `dest` names, refer to conflict_handler.

[Subject index](INDEX.md) · [Previous](metavar.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Continue](deprecated.md)
