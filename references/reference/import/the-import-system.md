# 5. The import system

### 5. The import system

Code living in one [module](https://docs.python.org/3.14/glossary.html#term-module) reaches the code held by another module through the act of [importing](https://docs.python.org/3.14/glossary.html#term-importing) it. Although the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement is by far the usual route for triggering the import machinery, it is not the sole route. Helpers like [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) and the built-in [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) are equally capable of triggering that machinery.

Two distinct steps are bundled into the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement: it locates the requested module, and afterward it attaches the outcome of that lookup to a name within the local scope. That lookup half of the `import` statement is specified as an invocation of the [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function supplied with suitable arguments. Whatever `__import__()` hands back is then what drives the name binding portion of the `import` statement. Consult the `import` statement itself for a precise account of how that name binding behaves.

Calling [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) on its own carries out nothing more than the module lookup plus, when the module turns up, its creation. Although a few side-effects can result — for instance pulling in parent packages and refreshing assorted caches (among them [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules)) — the name binding step belongs exclusively to the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement.

Whenever an [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement runs, the regular builtin [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function gets invoked. Alternative routes into the import system (for instance [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module)) are free to skip `__import__()` entirely and supply their own implementations of import semantics.

The very first time a module is imported, Python looks it up and, on success, builds a module object [1] and initializes it. Should the requested module be missing, a [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) results. Python applies a variety of approaches to track down the requested module once the import machinery starts. Those approaches are open to adjustment and extension through the assorted hooks covered in the sections that follow.

Changed in version 3.3: The import system was reworked to deliver in full the second stage of [**PEP 302**](https://peps.python.org/pep-0302/). Implicit import machinery is gone — the entire import system is now surfaced via [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path). On top of that, built-in support for namespace packages arrived (consult [**PEP 420**](https://peps.python.org/pep-0420/)).

[Subject index](INDEX.md) · [Following source section](importlib.md)
