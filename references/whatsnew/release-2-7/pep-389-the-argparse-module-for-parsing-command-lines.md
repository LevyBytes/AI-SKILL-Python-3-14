# What’s New in Python 2.7 / PEP 389: The argparse Module for Parsing Command Lines - argparse, getopt, optparse

### PEP 389: The argparse Module for Parsing Command Lines

The [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module for parsing command-line arguments was introduced as a more capable substitute for the [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module.

This means that Python now ships three separate modules for parsing command-line arguments: [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt), [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse), and [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse). Because the `getopt` module mirrors the C library’s `getopt()` function quite closely, it stays handy when you are writing a Python prototype destined to be rewritten in C later. `optparse` turns redundant, yet there are no plans to drop it given how many scripts still depend on it, and given that no automated method exists to update those scripts. (Bringing the `argparse` API into line with `optparse`’s interface was considered but turned down as too messy and hard.)

In brief, when you are writing a fresh script and need not concern yourself with compatibility against older Python versions, reach for [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) rather than [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse).

Here’s an example:

```python
import argparse

parser = argparse.ArgumentParser(description='Command-line example.')

# Add optional switches
parser.add_argument('-v', action='store_true', dest='is_verbose',
                    help='produce verbose output')
parser.add_argument('-o', action='store', dest='output',
                    metavar='FILE',
                    help='direct output to FILE instead of stdout')
parser.add_argument('-C', action='store', type=int, dest='context',
                    metavar='NUM', default=0,
                    help='display NUM lines of added context')

# Allow any number of additional arguments.
parser.add_argument(nargs='*', action='store', dest='inputs',
                    help='input filenames (default is stdin)')

args = parser.parse_args()
print args.__dict__

```

Unless you override them, the `-h` and `--help` switches get added automatically and yield tidily formatted output:

```python
-> ./python.exe argparse-example.py --help
usage: argparse-example.py [-h] [-v] [-o FILE] [-C NUM] [inputs [inputs ...]]

Command-line example.

positional arguments:
  inputs      input filenames (default is stdin)

optional arguments:
  -h, --help  show this help message and exit
  -v          produce verbose output
  -o FILE     direct output to FILE instead of stdout
  -C NUM      display NUM lines of added context

```

Just like [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse), the command-line switches and arguments come back as an object carrying attributes named after the *dest* parameters:

```python
-> ./python.exe argparse-example.py -v
{'output': None,
 'is_verbose': True,
 'context': 0,
 'inputs': []}

-> ./python.exe argparse-example.py -v -o /tmp/output -C 4 file1 file2
{'output': '/tmp/output',
 'is_verbose': True,
 'context': 4,
 'inputs': ['file1', 'file2']}

```

[`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) offers far richer validation than [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse); give an integer to demand an exact argument count, pass `'*'` to accept zero or more, pass `'+'` to accept one or more, or use `'?'` for a single optional argument. Sub-parsers may be nested inside a top-level parser to set up subcommands that each carry their own switch sets, for instance `svn commit`, `svn checkout`, and the like. You can declare an argument’s type as [`FileType`](https://docs.python.org/3.14/library/argparse.html#argparse.FileType), which opens files for you automatically and recognizes that `'-'` denotes standard input or output.

See also

[`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) documentation

The documentation page of the argparse module.

[Migrating optparse code to argparse](https://docs.python.org/3.14/howto/argparse-optparse.html#upgrading-optparse-code)

Part of the Python documentation, describing how to convert code that uses [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse).

[**PEP 389**](https://peps.python.org/pep-0389/) - argparse - New Command Line Parsing Module

PEP written and implemented by Steven Bethard.

[Subject index](INDEX.md) · [Previous source section](pep-378-format-specifier-for-thousands-separator.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Next source section](pep-391-dictionary-based-configuration-for-logging.md)
