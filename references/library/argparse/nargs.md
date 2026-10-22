# argparse — nargs

### nargs

Typically an `ArgumentParser` object pairs one command-line argument with one action to perform. The `nargs` keyword argument lets you bind some other count of command-line arguments to a single action. See also [Specifying ambiguous arguments](https://docs.python.org/3.14/howto/argparse.html#specifying-ambiguous-arguments). These are the values you can supply:

- `N` (an integer). A group of `N` arguments off the command line gets collected together into a list. As an example:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs=2)
>>> parser.add_argument('bar', nargs=1)
>>> parser.parse_args('c --foo a b'.split())
Namespace(bar=['c'], foo=['a', 'b'])

```

Keep in mind that `nargs=1` yields a single-element list. That differs from the default behavior, where the item appears on its own.

- `'?'`. Where possible, a single argument is taken from the command line and delivered as one item. When no command-line argument exists, the default value is produced instead. For optional arguments there is one more scenario - the option string appears but no command-line argument follows it. Under those circumstances, the const value is produced. A few examples make this clearer:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='?', const='c', default='d')
>>> parser.add_argument('bar', nargs='?', default='d')
>>> parser.parse_args(['XX', '--foo', 'YY'])
Namespace(bar='XX', foo='YY')
>>> parser.parse_args(['XX', '--foo'])
Namespace(bar='XX', foo='c')
>>> parser.parse_args([])
Namespace(bar='d', foo='d')

```

A frequent application of `nargs='?'` is to permit optional input and output files:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('infile', nargs='?')
>>> parser.add_argument('outfile', nargs='?')
>>> parser.parse_args(['input.txt', 'output.txt'])
Namespace(infile='input.txt', outfile='output.txt')
>>> parser.parse_args(['input.txt'])
Namespace(infile='input.txt', outfile=None)
>>> parser.parse_args([])
Namespace(infile=None, outfile=None)

```

- `'*'`. Every command-line argument that is present gets gathered into a list. Bear in mind that there is rarely much point in having more than a single positional argument set to `nargs='*'`, although several optional arguments using `nargs='*'` is workable. As an example:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='*')
>>> parser.add_argument('--bar', nargs='*')
>>> parser.add_argument('baz', nargs='*')
>>> parser.parse_args('a b --foo x y --bar 1 2'.split())
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

```

- `'+'`. Much like `'*'`, every command-line argument present is gathered into a list. On top of that, an error message is raised whenever no command-line argument at all was supplied. As an example:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('foo', nargs='+')
>>> parser.parse_args(['a', 'b'])
Namespace(foo=['a', 'b'])
>>> parser.parse_args([])
usage: PROG [-h] foo [foo ...]
PROG: error: the following arguments are required: foo

```

When you leave the `nargs` keyword argument out, the action itself decides how many arguments get consumed. As a rule, that translates to one command-line argument being consumed and one item (rather than a list) being produced. Any action that consumes no command-line arguments (for instance `'store_const'`) is given `nargs=0`.

[Subject index](INDEX.md) · [Previous](action-code-example-parser-argparse-argumentparser.md) · [Continue](const.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
