# What’s New in Python 2.3 / The optparse Module — getopt, optparse

### The optparse Module

Basic parsing of command-line arguments comes from the [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt) module. The new [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module (originally named Optik) delivers richer command-line parsing that respects the Unix conventions, builds the `--help` output on its own, and can run distinct actions per option.

Begin by instantiating [`OptionParser`](https://docs.python.org/3.14/library/optparse.html#optparse.OptionParser) and describing your program's options to it.

```python
import sys
from optparse import OptionParser

op = OptionParser()
op.add_option('-i', '--input',
              action='store', type='string', dest='input',
              help='set input filename')
op.add_option('-l', '--length',
              action='store', type='int', dest='length',
              help='set maximum length of output')

```

To parse a command line, you then call the [`parse_args()`](https://docs.python.org/3.14/library/optparse.html#optparse.OptionParser.parse_args) method.

```python
options, args = op.parse_args(sys.argv[1:])
print options
print args

```

The result is an object holding all the option values, together with a list of strings holding whatever arguments remain.

Running the script with assorted arguments now behaves just as you'd anticipate. Observe that the length argument gets converted to an integer automatically.

```shell
$ ./python opt.py -i data arg1
<Values at 0x400cad4c: {'input': 'data', 'length': None}>
['arg1']
$ ./python opt.py --input=data --length=4
<Values at 0x400cad2c: {'input': 'data', 'length': 4}>
[]
$

```

The help message gets generated for you automatically:

```shell
$ ./python opt.py --help
usage: opt.py [options]

options:
  -h, --help            show this help message and exit
  -iINPUT, --input=INPUT
                        set input filename
  -lLENGTH, --length=LENGTH
                        set maximum length of output
$

```

Refer to the module's documentation for more specifics.

Greg Ward wrote Optik, drawing on suggestions from the readers of the Getopt SIG.

[Subject index](INDEX.md) · [Previous source section](date-time-type.md) · [Next source section](pymalloc-a-specialized-object-allocator.md) · [Release/subject declaration](standard-set-type.md)
