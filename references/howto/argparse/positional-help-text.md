# Positional help text

Keep in mind, though, that even if the help display looks pleasant enough, right now it isn't as helpful as it could be. As an example, we can see `echo` listed as a positional argument, yet what it does stays unknown unless we guess or dig through the source code. So let's make it a touch more useful:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)

```

And we get:

```shell
$ python prog.py -h
usage: prog.py [-h] echo

positional arguments:
  echo        echo the string you use here

options:
  -h, --help  show this help message and exit

```

[Subject index](INDEX.md) · [Positional echo argument and parser results](positional-echo-argument-and-parser-results.md) · [Numeric positional argument conversion and errors](numeric-positional-argument-conversion-and-errors.md) · [Previous source context](positional-echo-argument-and-parser-results.md) · [Following source context](numeric-positional-argument-conversion-and-errors.md)
