# argparse - fromfile_prefix_chars

### fromfile_prefix_chars

There are times when, faced with an unusually long argument list, it is more sensible to stash the arguments in a file than to type them all on the command line. When the `ArgumentParser` constructor receives the `fromfile_prefix_chars=` argument, any arguments beginning with one of the named characters are taken as files and swapped out for the arguments held inside them. For example:

```python
>>> with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
...     fp.write('-f\nbar')
...
>>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
>>> parser.add_argument('-f')
>>> parser.parse_args(['-f', 'foo', '@args.txt'])
Namespace(f='bar')

```

Arguments pulled from a file default to one per line (though see `convert_arg_line_to_args()` as well) and are handled as though they had appeared at the same spot as the original file-referencing argument on the command line. Hence in the example above, the expression `['-f', 'foo', '@args.txt']` counts as equivalent to the expression `['-f', 'foo', '-f', 'bar']`.

Note

Every line counts as one argument, which means a blank line comes through as an empty string (`''`).

`ArgumentParser` relies on the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) when reading the file that holds arguments.

`None` is the default for the `fromfile_prefix_chars=` argument, so by default no argument is ever read as a file reference.

Changed in version 3.12: For reading argument files, `ArgumentParser` moved its encoding and errors away from the prior defaults (namely [`locale.getpreferredencoding(False)`](https://docs.python.org/3.14/library/locale.html#locale.getpreferredencoding) plus `"strict"`) over to the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). On Windows, encode the argument file as UTF-8 rather than in the ANSI Codepage.

[Subject index](INDEX.md) · [Previous](prefix-chars.md) · [Continue](argument-default.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
