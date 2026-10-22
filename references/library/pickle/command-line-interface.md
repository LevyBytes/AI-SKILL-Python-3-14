# pickle — Command-line interface

### Command-line interface

You may run the `pickle` module directly as a script at the command line, and it will print out what the pickle files hold. That said, if the pickle you are inspecting originates from a source you do not trust, prefer `-m pickletools`, which is the safer route since it never runs pickle bytecode — refer to [pickletools CLI usage](https://docs.python.org/3.14/library/pickletools.html#pickletools-cli).

```bash
python -m pickle pickle_file [pickle_file ...]

```

This module accepts the option below:

 pickle_file

The pickle file you want read; pass `-` instead to pull input from standard input.

See also

Module [`copyreg`](https://docs.python.org/3.14/library/copyreg.html#module-copyreg)

Pickle interface constructor registration for extension types.

Module [`pickletools`](https://docs.python.org/3.14/library/pickletools.html#module-pickletools)

Tools for working with and analyzing pickled data.

Module [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve)

Indexed databases of objects; uses `pickle`.

Module [`copy`](https://docs.python.org/3.14/library/copy.html#module-copy)

Shallow and deep object copying.

Module [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal)

High-performance serialization of built-in types.

Footnotes

[Subject index](INDEX.md) · [Previous](examples.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)
