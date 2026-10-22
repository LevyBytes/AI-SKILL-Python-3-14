# Short options

### Short options

Anyone used to command line usage will see that I've so far skipped the matter of short forms of the options. It's pretty simple:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")

```

And here it goes:

```shell
$ python prog.py -v
verbosity turned on
$ python prog.py --help
usage: prog.py [-h] [-v]

options:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity

```

Notice that this new capability shows up in the help text as well.

[Subject index](INDEX.md) · [Previous source context](boolean-verbose-flag-with-store-true.md) · [Following source context](combining-positional-square-and-verbose-flag.md)
