# json - Command-line interface

### Command-line interface

**Source code:** [Lib/json/tool.py](https://github.com/python/cpython/tree/3.14/Lib/json/tool.py)

---

You can run the `json` module as a script through `python -m json` to check and pretty-print JSON objects. This interface is provided by the `json.tool` submodule.

When you leave out the optional `infile` and `outfile` arguments, [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) and [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) stand in for them, respectively:

```shell
$ echo '{"json": "obj"}' | python -m json
{
    "json": "obj"
}
$ echo '{1.2:3.4}' | python -m json
Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

```

Changed in version 3.5: Output now follows the same order as the input. Apply the `--sort-keys` option to order dictionary output alphabetically by key.

Changed in version 3.14: You can now run the `json` module straight away as `python -m json`. To preserve backwards compatibility, calling the CLI as `python -m json.tool` still works.

[Subject index](INDEX.md) · [Previous](implementation-limitations.md) · [Continue](command-line-options.md) · [Owning module, declaration or section: json](json-encoding-and-decoding-overview.md)
