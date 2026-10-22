# optparse — Introduction

### Introduction

For parsing command-line options, `optparse` is a more convenient, flexible, and powerful library than the bare-bones [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt) module. `optparse` adopts a more declarative style of command-line parsing: you build an `OptionParser` instance, fill it with options, and parse the command line. `optparse` lets users give options in the conventional GNU/POSIX syntax, and on top of that generates usage and help messages for you.

Below is an example of putting `optparse` to work in a simple script:

```python
from optparse import OptionParser
...
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

```

With just these few lines, anyone using your script can now do the "usual thing" at the command-line, for instance:

```python
<yourscript> --file=outfile -q

```

While parsing the command line, `optparse` sets attributes on the `options` object that `parse_args()` returns, based on the values the user gave at the command-line. By the time `parse_args()` finishes parsing this command line, `options.filename` will hold `"outfile"` and `options.verbose` will hold `False`. `optparse` handles both long and short options, lets short options be combined together, and lets options pair with their arguments in several ways. So all the following command lines come out equivalent to the example above:

```python
<yourscript> -f outfile --quiet
<yourscript> --quiet --file outfile
<yourscript> -q -foutfile
<yourscript> -qfoutfile

```

On top of that, users may run any one of the following

```python
<yourscript> -h
<yourscript> --help

```

and `optparse` will print out a brief summary of your script's options:

```text
Usage: <yourscript> [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  write report to FILE
  -q, --quiet           don't print status messages to stdout

```

where the value of *yourscript* is worked out at runtime (usually from `sys.argv[0]`).

[Subject index](INDEX.md) · [Previous](argparse-option-value-differences.md) · [Continue](background.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
