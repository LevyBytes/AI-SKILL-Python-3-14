# Optional verbosity values and omission

### Introducing Optional arguments

Up to now we've been toying with positional arguments. Let's take a look at how optional ones get added:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")

```

And the output:

```shell
$ python prog.py --verbosity 1
verbosity turned on
$ python prog.py
$ python prog.py --help
usage: prog.py [-h] [--verbosity VERBOSITY]

options:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY
                        increase output verbosity
$ python prog.py --verbosity
usage: prog.py [-h] [--verbosity VERBOSITY]
prog.py: error: argument --verbosity: expected one argument

```

Here's the breakdown:

- The program is built to print something whenever `--verbosity` is given and to print nothing when it isn't.

- To prove the option really is optional, running the program without it raises no error. Be aware that, by default, when an optional argument goes unused, the matching variable, here `args.verbosity`, is handed the value `None`, which is why it doesn't pass the truth check in the [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) statement.

- The help message reads a little differently.

- Whenever the `--verbosity` option is used, you're also required to supply some value, any value.

[Subject index](INDEX.md) · [Boolean verbose flag with store_true](boolean-verbose-flag-with-store-true.md) · [Previous source context](numeric-positional-argument-conversion-and-errors.md) · [Following source context](boolean-verbose-flag-with-store-true.md)
