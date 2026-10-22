# 6.4.1. Importing * From a Package

### 6.4.1. Importing * From a Package

So what occurs when the user writes `from sound.effects import *`? Ideally you'd hope that this somehow reaches out to the filesystem, determines which submodules the package contains, and imports every one of them. That could be slow, and importing sub-modules might trigger unwanted side-effects meant to occur only when the sub-module is imported on purpose.

The lone remedy is for the package author to supply an explicit index of the package. Here's the convention the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement follows: if the code in a package's `__init__.py` defines a list called `__all__`, that list is treated as the set of module names to import when `from package import *` is met. Keeping this list current as new versions of the package come out is the package author's responsibility. Package authors are also free to skip supporting it, if importing * from their package serves no purpose they can see. As an example, the file `sound/effects/__init__.py` might hold this code:

```python
__all__ = ["echo", "surround", "reverse"]

```

That would make `from sound.effects import *` import the three named submodules of the `sound.effects` package.

Watch out for the possibility that submodules get shadowed by locally defined names. For instance, suppose you added a `reverse` function to the `sound/effects/__init__.py` file; then `from sound.effects import *` would bring in just the two submodules `echo` and `surround`, but *not* the `reverse` submodule, since the locally defined `reverse` function shadows it:

```python
__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'

```

When `__all__` is left undefined, the statement `from sound.effects import *` does *not* pull every submodule of the package `sound.effects` into the current namespace; all it guarantees is that the package `sound.effects` has been imported (perhaps running whatever initialization code sits in `__init__.py`) and then imports whichever names the package defines. That covers any names defined (and submodules explicitly loaded) by `__init__.py`. It also covers any of the package's submodules that earlier [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statements explicitly loaded. Take this code:

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *

```

Here, the `echo` and `surround` modules land in the current namespace, because they're defined in the `sound.effects` package at the moment the `from...import` statement runs. (This holds true when `__all__` is defined as well.)

Even though some modules are built to expose only names matching certain patterns when you use `import *`, doing so in production code is still regarded as poor practice.

Don't forget, there's nothing at all wrong with `from package import specific_submodule`! That's actually the recommended notation, except when the importing module needs submodules of the same name coming from different packages.

[Subject index](INDEX.md) · [Previous source section](packages.md) · [Following source section](intra-package-references.md)
