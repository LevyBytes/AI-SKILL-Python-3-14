# Default zero for absent verbosity

Let's patch that bug:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)

```

We've now brought in one more keyword, `default`. We pinned it to `0` so it lines up comparably with the other int values. Recall that, by default, when an optional argument isn't supplied, it takes the `None` value, and that can't be measured against an int value (which is where the [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception comes from).

And:

```shell
$ python prog.py 4
16

```

You can travel pretty far on just what we've picked up so far, and we've barely scratched the surface. The [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module packs a lot of power, and we'll poke at a bit more of it before wrapping up this tutorial.

[Subject index](INDEX.md) · [Combining positional square and verbose flag](combining-positional-square-and-verbose-flag.md) · [Numeric verbosity levels and invalid choices](numeric-verbosity-levels-and-invalid-choices.md) · [Restricting verbosity with choices](restricting-verbosity-with-choices.md) · [Counting verbosity flags and None behavior](counting-verbosity-flags-and-none-behavior.md) · [Saturating verbosity count](saturating-verbosity-count.md) · [Previous source context](saturating-verbosity-count.md) · [Following source context](getting-a-little-more-advanced.md)
