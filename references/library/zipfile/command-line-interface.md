# zipfile — Command-line interface

### Command-line interface

The `zipfile` module ships a straightforward command-line interface for working with ZIP archives.

To build a new ZIP archive, give its name following the `-c` option and then list whichever filename(s) ought to be included:

```shell
$ python -m zipfile -c monty.zip spam.txt eggs.txt

```

Handing over a directory works just as well:

```shell
$ python -m zipfile -c monty.zip life-of-brian_1979/

```

To pull a ZIP archive out into the named directory, reach for the `-e` option:

```shell
$ python -m zipfile -e monty.zip target-dir/

```

To get a listing of the files within a ZIP archive, reach for the `-l` option:

```shell
$ python -m zipfile -l monty.zip

```

[Subject index](INDEX.md) · [Previous](zipinfo-reserved-to-zipinfo-file-size.md) · [Continue](command-line-options.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md)
