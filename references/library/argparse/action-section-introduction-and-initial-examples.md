# argparse — action — Section introduction and initial examples

### action

An `ArgumentParser` object ties each command-line argument to an action. Such actions are free to do nearly anything with the command-line arguments tied to them, but most of them merely attach an attribute onto the object that `parse_args()` hands back. You control how the command-line arguments get processed through the `action` keyword argument. The actions that ship with the module are:

- `'store'` - Simply records the value of the argument. This serves as the default action.

- `'store_const'` - Records whatever value the const keyword argument names; keep in mind that const defaults to `None`. You will most often see the `'store_const'` action paired with optional arguments that act as some kind of flag. As an example:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_const', const=42)
>>> parser.parse_args(['--foo'])
Namespace(foo=42)

```

- `'store_true'` and `'store_false'` - These act as particular variants of `'store_const'`, storing `True` and `False` respectively, with their defaults being `False` and `True`:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_true')
>>> parser.add_argument('--bar', action='store_false')
>>> parser.add_argument('--baz', action='store_false')
>>> parser.parse_args('--foo --bar'.split())
Namespace(foo=True, bar=False, baz=True)

```

- `'append'` - Tacks each argument value onto a list. This comes in handy when you want to let an option be given more than once. Should the default be a list that is not empty, the parsed result begins with whatever the default list holds, and any command-line values get appended afterward. Sample usage:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='append', default=['0'])
>>> parser.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['0', '1', '2'])

```

- `'append_const'` - Tacks the value named by the const keyword argument onto a list; again, const defaults to `None`. The `'append_const'` action proves handy when several arguments all need to push constants into one shared list. As an example:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--str', dest='types', action='append_const', const=str)
>>> parser.add_argument('--int', dest='types', action='append_const', const=int)
>>> parser.parse_args('--str --int'.split())
Namespace(types=[<class 'str'>, <class 'int'>])

```

- `'extend'` - Tacks every element of a multi-value argument onto a list. You will generally combine the `'extend'` action with the nargs keyword argument set to `'+'` or `'*'`. Be aware that if nargs stays `None` (its default) or is `'?'`, every individual character of the argument string ends up appended to the list. Sample usage:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument("--foo", action="extend", nargs="+", type=str)
>>> parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"])
Namespace(foo=['f1', 'f2', 'f3', 'f4'])

```

Added in version 3.8.

- `'count'` - Tallies how many times an argument shows up. As one example, this helps when you want to raise verbosity levels:

[Subject index](INDEX.md) · [Previous](name-or-flags.md) · [Continue](action-code-example-parser-argparse-argumentparser.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
