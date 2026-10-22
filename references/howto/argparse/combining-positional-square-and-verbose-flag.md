# Combining positional square and verbose flag

### Combining Positional and Optional arguments

Our program keeps getting more involved:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)

```

And now the output:

```shell
$ python prog.py
usage: prog.py [-h] [-v] square
prog.py: error: the following arguments are required: square
$ python prog.py 4
16
$ python prog.py 4 --verbose
the square of 4 equals 16
$ python prog.py --verbose 4
the square of 4 equals 16

```

- We've reinstated a positional argument, which is why it grumbles.

- Observe that the ordering makes no difference.

[Subject index](INDEX.md) · [Numeric verbosity levels and invalid choices](numeric-verbosity-levels-and-invalid-choices.md) · [Restricting verbosity with choices](restricting-verbosity-with-choices.md) · [Counting verbosity flags and None behavior](counting-verbosity-flags-and-none-behavior.md) · [Saturating verbosity count](saturating-verbosity-count.md) · [Default zero for absent verbosity](default-zero-for-absent-verbosity.md) · [Previous source context](short-options.md) · [Following source context](numeric-verbosity-levels-and-invalid-choices.md)
