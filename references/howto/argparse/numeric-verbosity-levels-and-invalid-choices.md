# Numeric verbosity levels and invalid choices

What if we hand this program of ours back the option of multiple verbosity values, and genuinely put them to use:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int,
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

And the output:

```shell
$ python prog.py 4
16
$ python prog.py 4 -v
usage: prog.py [-h] [-v VERBOSITY] square
prog.py: error: argument -v/--verbosity: expected one argument
$ python prog.py 4 -v 1
4^2 == 16
$ python prog.py 4 -v 2
the square of 4 equals 16
$ python prog.py 4 -v 3
16

```

[Subject index](INDEX.md) · [Combining positional square and verbose flag](combining-positional-square-and-verbose-flag.md) · [Restricting verbosity with choices](restricting-verbosity-with-choices.md) · [Counting verbosity flags and None behavior](counting-verbosity-flags-and-none-behavior.md) · [Saturating verbosity count](saturating-verbosity-count.md) · [Default zero for absent verbosity](default-zero-for-absent-verbosity.md) · [Previous source context](combining-positional-square-and-verbose-flag.md) · [Following source context](restricting-verbosity-with-choices.md)
