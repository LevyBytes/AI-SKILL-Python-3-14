# argparse - color

### color

By default, the help message comes out in color by way of [ANSI escape sequences](https://en.wikipedia.org/wiki/ANSI_escape_code). For plain text help messages instead, you can switch this off either [in your local environment](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color), or within the argument parser itself by setting `color` to `False`:

```python
>>> parser = argparse.ArgumentParser(description='Process some integers.',
...                                  color=False)
>>> parser.add_argument('--action', choices=['sum', 'max'])
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
>>> parser.parse_args(['--help'])

```

Keep in mind that with `color=True`, whether output actually shows color hinges on both environment variables and what the terminal supports. With `color=False`, however, colored output is shut off no matter what, even where environment variables such as `FORCE_COLOR` are present.

Note

Color codes will creep into error messages when stderr is redirected to a file. Heading that off means setting the [`NO_COLOR`](https://no-color.org/) or [`PYTHON_COLORS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_COLORS) environment variable (for example, `NO_COLOR=1 python script.py 2> errors.txt`).

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](suggest-on-error.md) · [Continue](the-add-argument-method.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
