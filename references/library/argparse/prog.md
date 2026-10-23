# argparse - prog

### prog

Out of the box, `ArgumentParser` derives the program name shown in help messages from the manner in which the Python interpreter was launched:

- The [`base name`](https://docs.python.org/3.14/library/os.path.html#os.path.basename) of `sys.argv[0]` if a file was passed as argument.

- When the argument given is a directory or a zipfile, the Python interpreter name trailed by `sys.argv[0]`.

- Where the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) option came into play, the Python interpreter name, then `-m`, then the name of the module or package.

This default is nearly always what you want, since it lines the help messages up with the exact string typed to start the program on the command line. Should you still need to override that default, you can hand a different value through the `prog=` argument to `ArgumentParser`:

```python
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.print_help()
usage: myprogram [-h]

options:
 -h, --help  show this help message and exit

```

Keep in mind that the program name — be it derived from `sys.argv[0]`, from the `__main__` module attributes, or from the `prog=` argument — can be referenced inside help messages through the `%(prog)s` format specifier.

```python
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.add_argument('--foo', help='foo of the %(prog)s program')
>>> parser.print_help()
usage: myprogram [-h] [--foo FOO]

options:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program

```

Changed in version 3.14: Instead of forever defaulting to `os.path.basename(sys.argv[0])`, the `prog` value now mirrors the manner in which `__main__` got run.

[Subject index](INDEX.md) · [Previous](argumentparser-objects.md) · [Continue](usage.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
