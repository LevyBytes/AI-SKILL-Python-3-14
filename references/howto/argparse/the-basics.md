# The basics

### The basics

We'll begin with a bare-bones example that does (nearly) nothing:

```python
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

```

What follows is what comes out when you run the code:

```shell
$ python prog.py
$ python prog.py --help
usage: prog.py [-h]

options:
  -h, --help  show this help message and exit
$ python prog.py --verbose
usage: prog.py [-h]
prog.py: error: unrecognized arguments: --verbose
$ python prog.py foo
usage: prog.py [-h]
prog.py: error: unrecognized arguments: foo

```

Here's the breakdown:

- Run the script with no options and nothing prints to stdout. Hardly handy.

- The second invocation begins to show why the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module matters. We've done practically nothing, yet a tidy help message already appears.

- The `--help` option, which `-h` can also stand in for, is the lone option handed to us at no cost (that is, no need to declare it). Supplying anything else triggers an error. Yet even so, a handy usage message comes along for free as well.

[Subject index](INDEX.md) · [Previous source context](concepts.md) · [Following source context](positional-echo-argument-and-parser-results.md)
