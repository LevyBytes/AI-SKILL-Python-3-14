# json - Command-line options

### Command-line options

 infile

The JSON file you want checked or pretty-printed:

```shell
$ python -m json mp_films.json
[
    {
        "title": "And Now for Something Completely Different",
        "year": 1971
    },
    {
        "title": "Monty Python and the Holy Grail",
        "year": 1975
    }
]

```

When *infile* is omitted, input is taken from [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin).

 outfile

Send the result of processing *infile* to the supplied *outfile*. Failing that, it goes to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout).

 --sort-keys

Order dictionary output alphabetically according to the key.

Added in version 3.5.

 --no-ensure-ascii

Turn off escaping for non-ascii characters; refer to `json.dumps()` for further detail.

Added in version 3.9.

 --json-lines

Treat each input line as its own JSON object during parsing.

Added in version 3.8.

 --indent, --tab, --no-indent, --compact

A set of mutually exclusive switches that govern whitespace.

Added in version 3.9.

 -h, --help

Print the help text.

Footnotes

[Subject index](INDEX.md) · [Previous](command-line-interface.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
