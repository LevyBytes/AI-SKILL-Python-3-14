# optparse - Printing a version string

### Printing a version string

Much like the short usage string, `optparse` is able to print a version string for your program as well. You supply that string as the `version` argument to OptionParser:

```python
parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")

```

`%prog` gets expanded exactly the way it does within `usage`. Beyond that, `version` may hold whatever you wish. Once you provide it, `optparse` adds a `--version` option to your parser automatically. Should it run into this option on the command line, it expands your `version` string (substituting `%prog`), writes it to stdout, and exits.

For example, if your script is called `/usr/bin/foo`:

```shell
$ /usr/bin/foo --version
foo 1.0

```

The two methods below let you print and retrieve the `version` string:

 OptionParser.print_version(*file=None*)

Write the running program's version message (`self.version`) out to *file* (stdout by default). Just like `print_usage()`, every `%prog` found in `self.version` gets swapped for the running program's name. When `self.version` is empty or undefined, this does nothing.

 OptionParser.get_version()

Same as `print_version()` but returns the version string instead of printing it.

[Subject index](INDEX.md) · [Previous](optionparser-get-option-group.md) · [Continue](how-optparse-handles-errors.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
