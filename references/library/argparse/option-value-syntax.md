# argparse — Option value syntax

### Option value syntax

Several styles for stating an option's value (when one is required) are accepted by `parse_args()`. The most basic form delivers the option and its value as two distinct arguments:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('--foo')
>>> parser.parse_args(['-x', 'X'])
Namespace(foo=None, x='X')
>>> parser.parse_args(['--foo', 'FOO'])
Namespace(foo='FOO', x=None)

```

With long options (whose names run beyond a single character), you may also bundle the option and its value into one command-line argument by joining them with `=`:

```python
>>> parser.parse_args(['--foo=FOO'])
Namespace(foo='FOO', x=None)

```

With short options (those exactly one character long), the option and value can be written back-to-back:

```python
>>> parser.parse_args(['-xX'])
Namespace(foo=None, x='X')

```

You may also string multiple short options together behind a single `-` prefix, provided that only the final option (or no option at all) needs a value:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x', action='store_true')
>>> parser.add_argument('-y', action='store_true')
>>> parser.add_argument('-z')
>>> parser.parse_args(['-xyzZ'])
Namespace(x=True, y=True, z='Z')

```

[Subject index](INDEX.md) · [Previous](argumentparser-parse-args.md) · [Continue](invalid-arguments.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
