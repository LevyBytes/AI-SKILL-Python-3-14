# __main__ - Idiomatic Usage

### Idiomatic Usage

Certain modules hold code aimed purely at script execution, such as reading command-line arguments or pulling data in from standard input. Were such a module imported elsewhere — say, for unit testing — that script code would fire off by accident too.

That is precisely where the `if __name__ == '__main__'` code block earns its keep. Anything inside the block stays dormant unless the module is run within the top-level environment.

Keeping the body under `if __name__ == '__main__'` as small as you can tends to make the code clearer and more correct. The usual practice is for a function called `main` to wrap the program's core behavior:

```python
# echo.py

import shlex
import sys

def echo(phrase: str) -> None:
   """A dummy wrapper around print."""
   # for demonstration purposes, you can imagine that there is some
   # valuable and reusable logic inside this function
   print(phrase)

def main() -> int:
    """Echo the input arguments to standard output"""
    phrase = shlex.join(sys.argv)
    echo(phrase)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit

```

Observe that had the module not tucked the code inside the `main` function and instead placed it straight into the `if __name__ == '__main__'` block, the `phrase` variable would end up global across the whole module. That invites bugs, since other functions in the module might accidentally reach for the global rather than a local name. Wrapping it in a `main` function avoids the trouble.

A `main` function brings the further advantage of leaving the `echo` function self-contained and reusable from other code. Importing `echo.py` defines both the `echo` and `main` functions, yet calls neither, since `__name__ != '__main__'`.

### Idiomatic Usage

What goes in `__main__.py` is usually not guarded by an `if __name__ == '__main__'` block. Rather, these files stay brief and pull in functions to run from elsewhere. Those other modules then lend themselves to straightforward unit testing and genuine reuse.

Should you use one, an `if __name__ == '__main__'` block still behaves as intended for a `__main__.py` file inside a package, because once imported its `__name__` attribute carries the package's path:

```python
>>> import asyncio.__main__
>>> asyncio.__main__.__name__
'asyncio.__main__'

```

That said, it falls apart for `__main__.py` files sitting at the root of a `.zip` file. For that reason, a stripped-down `__main__.py` lacking a `__name__` check is the preferred, consistent choice.

See also

Look to [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) for a standard-library package that ships a minimal `__main__.py`. It carries no `if __name__ == '__main__'` block. Launch it via `python -m venv [directory]`.

Turn to [`runpy`](https://docs.python.org/3.14/library/runpy.html#module-runpy) for fuller coverage of the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) flag passed to the interpreter executable.

Check [`zipapp`](https://docs.python.org/3.14/library/zipapp.html#module-zipapp) to learn how to run applications bundled as *.zip* files. Here Python hunts for a `__main__.py` file at the archive's root directory.

[Subject index](INDEX.md) · [Previous](what-is-the-top-level-code-environment.md) · [Continue](packaging-considerations.md) · [Owning module, declaration or section: __main__](main-top-level-code-environment.md) · [Previous](main-py-in-python-packages.md) · [Continue](import-main.md)
