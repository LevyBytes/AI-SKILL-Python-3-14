# Counting verbosity flags and None behavior

Now let's try another way of handling verbosity, one that's fairly widespread. It also lines up with how the CPython executable deals with its own verbosity argument (look at the output of `python --help`):

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display the square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)

```

We've brought in another action, "count", to tally how many times particular options show up.

```shell
$ python prog.py 4
16
$ python prog.py 4 -v
4^2 == 16
$ python prog.py 4 -vv
the square of 4 equals 16
$ python prog.py 4 --verbosity --verbosity
the square of 4 equals 16
$ python prog.py 4 -v 1
usage: prog.py [-h] [-v] square
prog.py: error: unrecognized arguments: 1
$ python prog.py 4 -h
usage: prog.py [-h] [-v] square

positional arguments:
  square           display a square of a given number

options:
  -h, --help       show this help message and exit
  -v, --verbosity  increase output verbosity
$ python prog.py 4 -vvv
16

```

- Right, it now behaves more like a flag (much like `action="store_true"`) in the earlier version of our script. That accounts for the grumble.

- It likewise acts much like the "store_true" action.

- Here's a look at what the "count" action provides. You've very likely run across this style of usage before.

- And when you leave off the `-v` flag, that flag is taken to hold the `None` value.

- As you'd expect, when we use the long form of the flag, we should land on the same output.

- Regrettably, our help output says little about the new capability our script just gained, though that can always be remedied by sharpening the documentation for our script (for instance, through the `help` keyword argument).

- That final output reveals a bug in our program.

[Subject index](INDEX.md) · [Combining positional square and verbose flag](combining-positional-square-and-verbose-flag.md) · [Numeric verbosity levels and invalid choices](numeric-verbosity-levels-and-invalid-choices.md) · [Restricting verbosity with choices](restricting-verbosity-with-choices.md) · [Saturating verbosity count](saturating-verbosity-count.md) · [Default zero for absent verbosity](default-zero-for-absent-verbosity.md) · [Previous source context](restricting-verbosity-with-choices.md) · [Following source context](saturating-verbosity-count.md)
