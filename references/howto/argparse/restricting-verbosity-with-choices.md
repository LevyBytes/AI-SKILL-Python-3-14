# Restricting verbosity with choices

Each of these looks fine apart from the final one, which reveals a bug in our program. Let's patch it by limiting the values that the `--verbosity` option will take:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
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
$ python prog.py 4 -v 3
usage: prog.py [-h] [-v {0,1,2}] square
prog.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)
$ python prog.py 4 -h
usage: prog.py [-h] [-v {0,1,2}] square

positional arguments:
  square                display a square of a given number

options:
  -h, --help            show this help message and exit
  -v, --verbosity {0,1,2}
                        increase output verbosity

```

Notice that this adjustment turns up both in the error message and in the help string.

[Subject index](INDEX.md) · [Combining positional square and verbose flag](combining-positional-square-and-verbose-flag.md) · [Numeric verbosity levels and invalid choices](numeric-verbosity-levels-and-invalid-choices.md) · [Counting verbosity flags and None behavior](counting-verbosity-flags-and-none-behavior.md) · [Saturating verbosity count](saturating-verbosity-count.md) · [Default zero for absent verbosity](default-zero-for-absent-verbosity.md) · [Previous source context](numeric-verbosity-levels-and-invalid-choices.md) · [Following source context](counting-verbosity-flags-and-none-behavior.md)
