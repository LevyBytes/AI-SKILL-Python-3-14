# argparse - type

### type

The parser ordinarily takes in command-line arguments as plain strings. Frequently, though, you would rather have the command-line string treated as some other type, for example a [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`int`](https://docs.python.org/3.14/library/functions.html#int). The `type` keyword on `add_argument()` makes it possible to carry out whatever type-checking and type conversion you require.

When you combine the type keyword with the default keyword, the type converter runs only in the case where the default is a string.

What you give to `type` may be a callable that takes one string or the name of a registered type (refer to `register()`). Should the function raise `ArgumentTypeError`, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), that exception gets caught and a cleanly formatted error message appears. Exceptions of any other kind are left unhandled.

Familiar built-in types and functions work as type converters:

```python
import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('count', type=int)
parser.add_argument('distance', type=float)
parser.add_argument('street', type=ascii)
parser.add_argument('code_point', type=ord)
parser.add_argument('datapath', type=pathlib.Path)

```

Functions you define yourself are equally valid:

```pycon
>>> def hyphenated(string):
...     return '-'.join([word[:4] for word in string.casefold().split()])
...
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('short_title', type=hyphenated)
>>> parser.parse_args(['"The Tale of Two Cities"'])
Namespace(short_title='"the-tale-of-two-citi')

```

Using the [`bool()`](https://docs.python.org/3.14/library/functions.html#bool) function as a type converter is discouraged. The whole of what it does is turn empty strings into `False` and non-empty ones into `True`, which is rarely the behavior you are after:

```python
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('--verbose', type=bool)
>>> parser.parse_args(['--verbose', 'False'])
Namespace(verbose=True)

```

For typical substitutes, look at `BooleanOptionalAction` or `action='store_true'`.

Broadly speaking, the `type` keyword is a shortcut best reserved for straightforward conversions that can raise nothing beyond one of the three supported exceptions. Anything calling for richer error-handling or resource management belongs further downstream, once the arguments have already been parsed.

To take an example, JSON or YAML conversions carry intricate failure modes that demand better reporting than the `type` keyword can offer. A [`JSONDecodeError`](https://docs.python.org/3.14/library/json.html#json.JSONDecodeError) would come out poorly formatted, and a [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) exception would go entirely unhandled.

Even `FileType` runs into limits when paired with the `type` keyword. Suppose one argument relies on `FileType` and then some later argument fails - an error is reported, yet the file is left open rather than closed automatically. Here you would do better to hold off until the parser has finished and then employ the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)-statement to handle the files.

If your type checker only needs to verify a value against a fixed set, think about reaching for the choices keyword instead.

[Subject index](INDEX.md) · [Previous](default.md) · [Continue](choices.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
