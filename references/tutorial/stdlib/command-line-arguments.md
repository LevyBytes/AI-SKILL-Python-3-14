# 10.3. Command-line arguments

### 10.3. Command-line arguments

Everyday helper scripts frequently have to deal with command line arguments. Python keeps those arguments as a list in the *argv* attribute of the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module. Consider, as an example, this `demo.py` file:

```python
# File demo.py
import sys
print(sys.argv)

```

Running `python demo.py one two three` from the shell produces this output:

```python
['demo.py', 'one', 'two', 'three']

```

For a more capable way to handle command line arguments, turn to the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module. The script below pulls out one or more filenames plus an optional count of lines to show:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

```

Invoke it from the shell as `python top.py --lines=5 alpha.txt beta.txt`, and the script assigns `5` to `args.lines` while putting `['alpha.txt', 'beta.txt']` into `args.filenames`.

[Subject index](INDEX.md) · [Previous source section](file-wildcards.md) · [Following source section](error-output-redirection-and-program-termination.md)
