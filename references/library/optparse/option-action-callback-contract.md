# optparse - Standard option actions - Contract: Call the function specified by `callback`, which is called as

Call the function specified by `callback`, which is called as

```python
func(option, opt_str, value, parser, *args, **kwargs)

```

See section Option Callbacks for more detail.

- `"help"`

Prints a full help message covering every option in the current option parser. That help message is assembled from the `usage` string given to OptionParser's constructor plus the `help` string given to each option.

When an option has no `help` string, it still shows up in the help message. To leave an option out altogether, use the special value `optparse.SUPPRESS_HELP`.

Since `optparse` attaches a `help` option to all OptionParsers on its own, you rarely have to make one yourself.

Example:

```python
from optparse import OptionParser, SUPPRESS_HELP

# usually, a help option is added automatically, but that can
# be suppressed using the add_help_option argument
parser = OptionParser(add_help_option=False)

parser.add_option("-h", "--help", action="help")
parser.add_option("-v", action="store_true", dest="verbose",
                  help="Be moderately verbose")
parser.add_option("--file", dest="filename",
                  help="Input file to read data from")
parser.add_option("--secret", help=SUPPRESS_HELP)

```

Should `optparse` spot either `-h` or `--help` along the command line, it writes a help message resembling the one below to stdout (taking `sys.argv[0]` to be `"foo.py"`):

```text
Usage: foo.py [options]

Options:
  -h, --help        Show this help message and exit
  -v                Be moderately verbose
  --file=FILENAME   Input file to read data from

```

After printing the help message, `optparse` terminates your process with `sys.exit(0)`.

- `"version"`

[Subject index](INDEX.md) · [Previous](boolean-option-action-example.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: Standard option actions](standard-option-actions-overview.md) · [Required continuation of the source contract](standard-option-types.md)
