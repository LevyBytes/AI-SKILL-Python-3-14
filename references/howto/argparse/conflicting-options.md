# Conflicting options

### Conflicting options

So far, we've worked with two methods of an [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) instance. Let's bring in a third, [`add_mutually_exclusive_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group). It lets us name options that clash with one another. Let's also rework the rest of the program so the new functionality fits better: we'll add the `--quiet` option, which acts as the reverse of the `--verbose` one:

```python
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

```

Our program is leaner now, and we've given up some functionality just for the sake of the demonstration. In any case, here's the output:

```shell
$ python prog.py 4 2
4^2 == 16
$ python prog.py 4 2 -q
16
$ python prog.py 4 2 -v
4 to the power 2 equals 16
$ python prog.py 4 2 -vq
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
$ python prog.py 4 2 -v --quiet
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose

```

That ought to be straightforward to track. I tacked on that final output so you can get a feel for the kind of flexibility on offer, namely blending long form options together with short form ones.

Before we wrap up, you'll probably want to spell out for your users the chief purpose of your program, on the off chance they aren't aware:

```python
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

```

Notice that small change in the usage text. See the `[-v | -q]`, which signals that we may use either `-v` or `-q`, but not the two of them together:

```shell
$ python prog.py --help
usage: prog.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

options:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet

```

[Subject index](INDEX.md) · [Previous source context](specifying-ambiguous-arguments.md) · [Following source context](how-to-translate-the-argparse-output.md)
