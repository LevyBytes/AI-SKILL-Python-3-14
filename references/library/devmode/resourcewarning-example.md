# ResourceWarning Example

### ResourceWarning Example

Here is a script that tallies how many lines sit in the text file named on the command line:

```python
import sys

def main():
    fp = open(sys.argv[1])
    nlines = len(fp.readlines())
    print(nlines)
    # The file is closed implicitly

if __name__ == "__main__":
    main()

```

Notice the script never closes the file outright. Out of the box, Python raises no warning at all. Run against README.txt, a file of 269 lines:

```shell
$ python script.py README.txt
269

```

Once the Python Development Mode is switched on, a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) warning shows up:

```shell
$ python -X dev script.py README.txt
269
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
  main()
ResourceWarning: Enable tracemalloc to get the object allocation traceback

```

On top of that, switching on [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) reveals the line at which the file was opened:

```shell
$ python -X dev -X tracemalloc=5 script.py README.rst
269
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
  main()
Object allocated at (most recent call last):
  File "script.py", lineno 10
    main()
  File "script.py", lineno 4
    fp = open(sys.argv[1])

```

The remedy is to close the file outright. Here it is done with a context manager:

```python
def main():
    # Close the file explicitly when exiting the with block
    with open(sys.argv[1]) as fp:
        nlines = len(fp.readlines())
    print(nlines)

```

Failing to close a resource outright can keep it open far longer than you’d anticipate, and it may bring on serious trouble as Python shuts down. That’s a problem under CPython, and an even bigger one under PyPy. Closing resources outright leaves an application steadier and easier to trust.

[Subject index](INDEX.md) · [Previous](iobase-destructor-close-errors.md) · [Continue](bad-file-descriptor-error-example.md)
