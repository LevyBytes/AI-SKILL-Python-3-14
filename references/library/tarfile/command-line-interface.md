# tarfile — Command-Line Interface

### Command-Line Interface

Added in version 3.4.

The `tarfile` module ships a straightforward command-line interface for working with tar archives.

To build a fresh tar archive, give its name right after the `-c` option and then enumerate the filename(s) you want included:

```shell
$ python -m tarfile -c monty.tar  spam.txt eggs.txt

```

Passing a directory is also acceptable:

```shell
$ python -m tarfile -c monty.tar life-of-brian_1979/

```

To pull a tar archive out into the current directory, reach for the `-e` option:

```shell
$ python -m tarfile -e monty.tar

```

To send the extracted contents into another directory instead, pass that directory's name:

```shell
$ python -m tarfile -e monty.tar  other-dir/

```

To see the files held in a tar archive, use the `-l` option:

```shell
$ python -m tarfile -l monty.tar

```

[Subject index](INDEX.md) · [Previous](stateful-extraction-filter-example.md) · [Continue](command-line-options.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
