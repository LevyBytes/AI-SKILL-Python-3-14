# traceback: Exception printing and interpreter-loop examples

### Examples of Using the Module-Level Functions

The short example below builds a rudimentary read-eval-print loop, in the spirit of (though not as capable as) the regular Python interactive interpreter loop. If you want a fuller realization of the interpreter loop, turn to the [`code`](https://docs.python.org/3.14/library/code.html#module-code) module.

```python
import sys, traceback

def run_user_code(envdir):
    source = input(">>> ")
    try:
        exec(source, envdir)
    except Exception:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

envdir = {}
while True:
    run_user_code(envdir)

```

The example that follows walks through the various ways you can print and format the exception and its traceback:

```python
import sys, traceback

def lumberjack():
    bright_side_of_life()

def bright_side_of_life():
    return tuple()[0]

try:
    lumberjack()
except IndexError as exc:
    print("*** print_tb:")
    traceback.print_tb(exc.__traceback__, limit=1, file=sys.stdout)
    print("*** print_exception:")
    traceback.print_exception(exc, limit=2, file=sys.stdout)
    print("*** print_exc:")
    traceback.print_exc(limit=2, file=sys.stdout)
    print("*** format_exc, first and last line:")
    formatted_lines = traceback.format_exc().splitlines()
    print(formatted_lines[0])
    print(formatted_lines[-1])
    print("*** format_exception:")
    print(repr(traceback.format_exception(exc)))
    print("*** extract_tb:")
    print(repr(traceback.extract_tb(exc.__traceback__)))
    print("*** format_tb:")
    print(repr(traceback.format_tb(exc.__traceback__)))
    print("*** tb_lineno:", exc.__traceback__.tb_lineno)

```

Running the example would yield output resembling the following:

[Subject index](INDEX.md) · [Previous](framesummary-objects.md) · [Owning module, declaration or section: traceback](traceback-print-or-retrieve-a-stack-traceback.md) · [Required continuation of the source contract](traceback-and-stack-formatting-output.md)
