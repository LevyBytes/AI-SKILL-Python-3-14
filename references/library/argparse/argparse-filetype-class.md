# argparse - FileType objects

### FileType objects

 *class *argparse.FileType(*mode='r'*, *bufsize=-1*, *encoding=None*, *errors=None*)

Objects suitable for the type argument of `ArgumentParser.add_argument()` come from the `FileType` factory. Any argument whose type is a `FileType` object will open its command-line value as a file, honoring the chosen modes, buffer sizes, encodings, and error handling (consult the [`open()`](https://docs.python.org/3.14/library/functions.html#open) function for the full picture):

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--raw', type=argparse.FileType('wb', 0))
>>> parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
>>> parser.parse_args(['--raw', 'raw.dat', 'file.txt'])
Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<_io.FileIO name='raw.dat' mode='wb'>)

```

FileType objects recognize the pseudo-argument `'-'` and turn it automatically into [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) for readable `FileType` objects and [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) for writable `FileType` objects:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('infile', type=argparse.FileType('r'))
>>> parser.parse_args(['-'])
Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)

```

Note

Suppose one argument relies on *FileType* and a later argument then fails: an error is reported, but the file stays open rather than closing on its own. That can also overwrite the output files. Here you're better off holding off until the parser finishes and then employing the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)-statement to manage the files.

Changed in version 3.4: Added the *encoding* and *errors* parameters.

Deprecated since version 3.14.

[Subject index](INDEX.md) · [Previous](subcommands-code-example-subcommand-functions.md) · [Continue](argumentparser-add-argument-group.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
