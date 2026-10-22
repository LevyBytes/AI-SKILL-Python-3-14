# __main__ — `import __main__`

### `import __main__`

No matter which module kicked off a Python program, the other modules running alongside it can reach the top-level environment's scope ([namespace](https://docs.python.org/3.14/glossary.html#term-namespace)) simply by importing the `__main__` module. That brings in not a `__main__.py` file but whatever module was handed the special name `'__main__'`.

Below is a sample module that taps into the `__main__` namespace:

```python
# namely.py

import __main__

def did_user_define_their_name():
    return 'my_name' in dir(__main__)

def print_user_name():
    if not did_user_define_their_name():
        raise ValueError('Define the variable `my_name`!')

    print(__main__.my_name)

```

A sample way to put this module to use might look like this:

```python
# start.py

import sys

from namely import print_user_name

# my_name = "Dinsdale"

def main():
    try:
        print_user_name()
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())

```

At this point, running our program would produce output along these lines:

```shell
$ python start.py
Define the variable `my_name`!

```

The program's exit code would be 1, which flags an error. Uncommenting the `my_name = "Dinsdale"` line repairs the program, and it then exits with status code 0 to mark success:

```shell
$ python start.py
Dinsdale

```

Observe that importing `__main__` creates no trouble with accidentally executing the script-only top-level code stashed in the `if __name__ == "__main__"` block of the `start` module. So why does this hold up?

At interpreter startup Python places an empty `__main__` module into [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) and then fills it by running the top-level code. For our example that is the `start` module, which executes line by line and imports `namely`. `namely` then imports `__main__` (which is in fact `start`) — an import cycle! Happily, because the half-filled `__main__` module already sits in `sys.modules`, Python hands that one to `namely`. Consult [Special considerations for __main__](https://docs.python.org/3.14/reference/import.html#import-dunder-main) in the import system's reference for how the mechanism operates.

The Python REPL counts as yet another “top-level environment”, so whatever you define at the REPL lands in the `__main__` scope:

```python
>>> import namely
>>> namely.did_user_define_their_name()
False
>>> namely.print_user_name()
Traceback (most recent call last):
...
ValueError: Define the variable `my_name`!
>>> my_name = 'Jabberwocky'
>>> namely.did_user_define_their_name()
True
>>> namely.print_user_name()
Jabberwocky

```

Both [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) and [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) draw on the `__main__` scope in their implementations.

[Subject index](INDEX.md) · [Previous](idiomatic-usage.md) · [Owning module, declaration or section: __main__](main-top-level-code-environment.md)
