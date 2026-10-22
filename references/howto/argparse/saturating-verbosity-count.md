# Saturating verbosity count

Let's patch it:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

# bugfix: replace == with >=
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)

```

And here's what it produces:

```shell
$ python prog.py 4 -vvv
the square of 4 equals 16
$ python prog.py 4 -vvvv
the square of 4 equals 16
$ python prog.py 4
Traceback (most recent call last):
  File "prog.py", line 11, in <module>
    if args.verbosity >= 2:
TypeError: '>=' not supported between instances of 'NoneType' and 'int'

```

- The first output went fine, and patches the bug we had earlier. Namely, we want any value >= 2 to crank verbosity to the max.

- The third output isn't so great.

[Subject index](INDEX.md) · [Combining positional square and verbose flag](combining-positional-square-and-verbose-flag.md) · [Numeric verbosity levels and invalid choices](numeric-verbosity-levels-and-invalid-choices.md) · [Restricting verbosity with choices](restricting-verbosity-with-choices.md) · [Counting verbosity flags and None behavior](counting-verbosity-flags-and-none-behavior.md) · [Default zero for absent verbosity](default-zero-for-absent-verbosity.md) · [Previous source context](counting-verbosity-flags-and-none-behavior.md) · [Following source context](default-zero-for-absent-verbosity.md)
