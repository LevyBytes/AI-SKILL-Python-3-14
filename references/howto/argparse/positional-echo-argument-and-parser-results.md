# Positional echo argument and parser results

### Introducing Positional arguments

For example:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)

```

And running the code:

```shell
$ python prog.py
usage: prog.py [-h] echo
prog.py: error: the following arguments are required: echo
$ python prog.py --help
usage: prog.py [-h] echo

positional arguments:
  echo

options:
  -h, --help  show this help message and exit
$ python prog.py foo
foo

```

Here's what's going on:

- We've tacked on the [`add_argument()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument) method, our means of stating which command-line options the program agrees to take. For this one I called it `echo` to keep it consistent with what it does.

- Invoking our program now demands that we provide an option.

- The [`parse_args()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.parse_args) method does in fact hand back some data drawn from the supplied options, in this instance `echo`.

- The variable amounts to a kind of "magic" that [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) does at no charge (meaning you needn't state which variable that value lands in). You'll also spot that its name lines up with the string argument passed to the method, `echo`.

[Subject index](INDEX.md) · [Positional help text](positional-help-text.md) · [Numeric positional argument conversion and errors](numeric-positional-argument-conversion-and-errors.md) · [Previous source context](the-basics.md) · [Following source context](positional-help-text.md)
