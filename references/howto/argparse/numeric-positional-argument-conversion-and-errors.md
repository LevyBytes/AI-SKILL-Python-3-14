# Numeric positional argument conversion and errors

Now, what about something even handier:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()
print(args.square**2)

```

What follows is what comes out when you run the code:

```shell
$ python prog.py 4
Traceback (most recent call last):
  File "prog.py", line 5, in <module>
    print(args.square**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

```

That didn't pan out. The reason is that [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) handles whatever options we pass it as strings, unless we say otherwise. So let's instruct `argparse` to read that input as an integer:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)

```

What follows is what comes out when you run the code:

```shell
$ python prog.py 4
16
$ python prog.py four
usage: prog.py [-h] square
prog.py: error: argument square: invalid int value: 'four'

```

That worked out. The program even kindly bails out on bad illegal input before carrying on.

[Subject index](INDEX.md) · [Positional echo argument and parser results](positional-echo-argument-and-parser-results.md) · [Positional help text](positional-help-text.md) · [Previous source context](positional-help-text.md) · [Following source context](optional-verbosity-values-and-omission.md)
