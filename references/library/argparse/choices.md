# argparse — choices

### choices

Certain command-line arguments ought to come from a limited pool of values. You can manage those by handing a sequence object to `add_argument()` as the *choices* keyword argument. As the command line is parsed, each argument value is checked, and an error message appears whenever the argument fell outside the permitted values:

```python
>>> parser = argparse.ArgumentParser(prog='game.py')
>>> parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
>>> parser.parse_args(['rock'])
Namespace(move='rock')
>>> parser.parse_args(['fire'])
usage: game.py [-h] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')

```

You may hand any sequence over as the *choices* value, so [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) objects, [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) objects, and your own sequence types are all accepted.

Reaching for [`enum.Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) is discouraged, since it is awkward to govern how it shows up in usage, help, and error messages.

Bear in mind that *choices* get verified once any type conversions are complete, so the objects within *choices* ought to line up with the type you specified. That can leave *choices* looking odd in usage, help, or error messages.

So that *choices* stay friendly to users, you might wrap a custom type that converts and formats the values, or drop type altogether and deal with conversion inside your own application code.

When choices are formatted, they take the place of the default *metavar*, which normally comes from *dest*. That is generally the behavior you want, since the *dest* parameter never reaches the user. Should that presentation not suit you (perhaps the list of choices is long), simply hand over an explicit metavar.

[Subject index](INDEX.md) · [Previous](type.md) · [Continue](required.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
