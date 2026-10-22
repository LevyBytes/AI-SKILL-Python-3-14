# 6.1. More on Modules

### 6.1. More on Modules

Beyond function definitions, a module may also hold executable statements. Their purpose is to initialize the module, and they fire only the *first* time the module name appears in an import statement. [1] (They likewise run when the file is launched as a script.)

Every module carries its own private namespace, which serves as the global namespace for all the functions the module defines. As a result, the person writing a module is free to use global variables in it without fear of accidentally colliding with a user's own globals. Conversely, when you know precisely what you're doing, you can reach a module's global variables through the very notation you'd use for its functions: `modname.itemname`.

Modules are allowed to import other modules. By convention—though it isn't mandatory—all [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statements go at the top of a module (or a script, for that matter). When the imported module names sit at the module's top level (outside any function or class), they get added to that module's global namespace.

The [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement comes in a form that pulls names out of a module straight into the namespace of the importing module. To illustrate:

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

With this form, the module name that the imports came from is not brought into the local namespace (so here, `fibo` remains undefined).

A further form even pulls in every name that a module defines:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

That brings in all names apart from any that start with an underscore (`_`). For the most part, Python programmers steer clear of this feature, because it dumps an unknown collection of names into the interpreter and could mask things you've already defined.

Keep in mind that, broadly speaking, importing `*` from a module or package is discouraged, as it frequently produces code that's hard to read. That said, it's fine to reach for it to cut down on typing during interactive sessions.

When the module name is trailed by `as`, the name that comes after `as` is bound directly to the imported module.

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

Effectively this brings in the module just the way `import fibo` would, except the module ends up accessible under `fib` instead.

The same approach works alongside [`from`](https://docs.python.org/3.14/reference/simple_stmts.html#from), producing comparable results:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

```

Note

To keep things efficient, every module gets imported just one time within a given interpreter session. Consequently, if you edit your modules you'll have to restart the interpreter—or, when it's only a single module you're testing interactively, call [`importlib.reload()`](https://docs.python.org/3.14/library/importlib.html#importlib.reload), for instance `import importlib; importlib.reload(modulename)`.

[Subject index](INDEX.md) · [Previous source section](modules.md) · [Following source section](executing-modules-as-scripts.md)
