# Boolean verbose flag with store_true

The earlier example takes any integer value at all for `--verbosity`, but for our modest program just two of them really matter, `True` or `False`. Let's adjust the code to suit:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")

```

And the output:

```shell
$ python prog.py --verbose
verbosity turned on
$ python prog.py --verbose 1
usage: prog.py [-h] [--verbose]
prog.py: error: unrecognized arguments: 1
$ python prog.py --help
usage: prog.py [-h] [--verbose]

options:
  -h, --help  show this help message and exit
  --verbose   increase output verbosity

```

Here's the breakdown:

- The option now acts more like a flag than something demanding a value. We even renamed the option to fit that idea. Notice that we now hand over a new keyword, `action`, with the value `"store_true"`. That means, should the option appear, set `args.verbose` to `True`. Leaving it off implies `False`.

- It objects when you hand it a value, fully in keeping with what flags really are.

- Notice the help text has changed.

[Subject index](INDEX.md) · [Optional verbosity values and omission](optional-verbosity-values-and-omission.md) · [Previous source context](optional-verbosity-values-and-omission.md) · [Following source context](short-options.md)
