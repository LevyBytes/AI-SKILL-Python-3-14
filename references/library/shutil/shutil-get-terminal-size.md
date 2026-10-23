# shutil - Querying the size of the output terminal

### Querying the size of the output terminal

`shutil.get_terminal_size(*fallback=(columns, lines)*)`

Fetch the dimensions of the terminal window.

For both dimensions it consults the matching environment variable — `COLUMNS` and `LINES` respectively. Where that variable is set and holds a positive integer, that value wins.

In the usual case, where neither `COLUMNS` nor `LINES` is set, the terminal attached to [`sys.__stdout__`](https://docs.python.org/3.14/library/sys.html#sys.__stdout__) is interrogated through a call to [`os.get_terminal_size()`](https://docs.python.org/3.14/library/os.html#os.get_terminal_size).

Should the terminal size resist querying — whether the system can’t query it or we simply aren’t tied to a terminal — the `fallback` parameter’s value steps in. `fallback` defaults to `(80, 24)`, the size many terminal emulators take as standard.

What comes back is a named tuple of type [`os.terminal_size`](https://docs.python.org/3.14/library/os.html#os.terminal_size).

See also: The Single UNIX Specification, Version 2, [Other Environment Variables](https://pubs.opengroup.org/onlinepubs/7908799/xbd/envvar.html#tag_002_003).

Added in version 3.3.

Changed in version 3.11: Should [`os.get_terminal_size()`](https://docs.python.org/3.14/library/os.html#os.get_terminal_size) come back with zeroes, the `fallback` values now kick in there too.

[Subject index](INDEX.md) · [Previous](archiving-example-with-base-dir.md) · [Owning module, declaration or section: shutil](shutil-high-level-file-operations.md)
