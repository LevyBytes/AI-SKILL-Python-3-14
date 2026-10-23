# argparse`argparse` - Parser for command-line options, arguments and subcommands

### `argparse` - Parser for command-line options, arguments and subcommands

Added in version 3.2.

**Source code:** [Lib/argparse.py](https://github.com/python/cpython/tree/3.14/Lib/argparse.py)

Note

Although `argparse` is the standard library's go-to module recommended for putting together simple command line tools, developers whose needs are stricter about the precise behavior of their command line tools may discover that it falls short on fine-grained control. See [Choosing an argument parsing library](https://docs.python.org/3.14/library/optparse.html#choosing-an-argument-parser) for other options worth weighing whenever `argparse` lacks a behavior your application demands (for instance, turning off interspersed options and positionals altogether, or letting an option value begin with `-` even though it matches some other declared option).

---

The `argparse` module simplifies the job of building friendly command-line interfaces. Your program declares which arguments it expects, and `argparse` works out how to pull them from [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv). On top of that, the `argparse` module produces help and usage text for you automatically. It additionally reports errors whenever a user feeds the program arguments that are not valid.

Everything `argparse` offers for command-line interfaces centers on an instance of `argparse.ArgumentParser`. That instance holds argument specifications and carries options that govern the parser as a whole:

```python
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

```

Each argument specification is attached to the parser through the `ArgumentParser.add_argument()` method. The method handles positional arguments, options carrying values, and on/off flags alike:

```python
parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

```

Invoking the parser is the job of the `ArgumentParser.parse_args()` method, which deposits the gathered data into an `argparse.Namespace` object:

```python
args = parser.parse_args()
print(args.filename, args.count, args.verbose)

```

Note

For a walkthrough on migrating [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) code over to `argparse`, consult [Upgrading Optparse Code](https://docs.python.org/3.14/howto/argparse-optparse.html#upgrading-optparse-code).

[Subject index](INDEX.md) · [Continue](argumentparser-objects.md)
