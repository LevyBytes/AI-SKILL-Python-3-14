# Functions

### Functions

 importlib.__import__(*name*, *globals=None*, *locals=None*, *fromlist=()*, *level=0*)

An implementation of the built-in `__import__()` function.

Note

For importing modules from code, reach for `import_module()` rather than this function.

 importlib.import_module(*name*, *package=None*)

Import a module. Which module gets imported is governed by the *name* argument, given either absolutely or relatively (for example, `pkg.mod` or `..mod`). Should *name* be relative, you must also supply *package* set to the package name that serves as the anchor against which the package name is resolved (for instance, `import_module('..mod', 'pkg.subpkg')` will import `pkg.mod`).

Think of the `import_module()` function as a convenience layer wrapping `importlib.__import__()`. As a result, every bit of its behavior follows from `importlib.__import__()`. Where the two diverge most notably is the return value: `import_module()` hands back the named package or module (e.g. `pkg.mod`), whereas [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) hands back the top-level package or module (e.g. `pkg`).

When you import a module on the fly that came into being after the interpreter started up (say, a Python source file you just wrote), it may be necessary to invoke `invalidate_caches()` so that the import system picks up on the freshly added module.

Changed in version 3.3: Parent packages are automatically imported.

 importlib.invalidate_caches()

Clear out the internal caches belonging to the finders held in [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path). Should a finder define `invalidate_caches()`, that method gets invoked to carry out the clearing. Invoke this whenever modules get created or installed while your program runs, so that every finder is sure to register that the new module exists.

Added in version 3.3.

Changed in version 3.10: A namespace package added or installed at a fresh [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) location, once that very namespace had already been imported, is now detected.

 importlib.reload(*module*)

Reload a module imported earlier, passed as *module*. Since the argument has to be a module object, the module must already have been imported with success. This comes in handy when you have changed the module's source file with an outside editor and want to exercise the updated version without quitting the Python interpreter. What comes back is the module object ? which may differ if re-importing ends up putting a different object into [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

When `reload()` is executed:

- The module's Python code is compiled afresh and its top-level code runs again, producing a fresh batch of objects that get bound to names within the module's dictionary; this happens by reusing the [loader](https://docs.python.org/3.14/glossary.html#term-loader) that loaded the module the first time around. For extension modules, the `init` function does not run a second time.

- Just like every other object in Python, the previous objects stick around until nothing references them ? that is, until their reference counts reach zero.

- Entries in the module namespace get repointed at whatever objects are new or changed.

- References elsewhere to the previous objects ? for example, names living outside the module ? keep pointing at the old objects rather than being switched to the new ones, so wherever you want them updated you have to do so per namespace.

A handful of further caveats apply:

Reloading a module keeps its dictionary ? that is, the module's global variables ? in place. Because redefining names replaces the previous definitions, this is usually harmless. Where the updated module omits a name the previous one had defined, the previous definition stays put. A module can turn this behavior to its benefit when it keeps a global table or object cache around ? a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement lets it check whether the table already exists and bypass re-initializing it when that is what you want:

```python
try:
    cache
except NameError:
    cache = {}

```

Reloading modules that are built-in or dynamically loaded seldom accomplishes much. Steer clear of reloading [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys), [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__), [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins), and similarly central modules. Quite often, extension modules were never built to undergo initialization more than once, and reloading them can break in unpredictable ways.

Suppose a module pulls objects in from a different module via [`from`](https://docs.python.org/3.14/reference/simple_stmts.html#from) ? [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) ?; running `reload()` against that other module will not refresh the objects it had imported. To get around this, you can either run the `from` statement over again, or switch to `import` plus qualified names (*module.name*).

Should a module create instances of a class, reloading the module where that class lives leaves the instances' method definitions untouched ? they go on using the previous class definition. Derived classes behave the same way.

Added in version 3.4.

Changed in version 3.7: Should the module undergoing a reload have no `ModuleSpec`, [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) now gets raised.

Warning

Thread safety is not a property of this function. Invoking it across several threads at once can yield surprising results. For reloading modules safely across threads, the suggestion is to rely on a [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) or some other synchronization primitive.

[Subject index](INDEX.md) · [Previous](introduction.md) · [Continue](importlib-abc-metapathfinder-class.md)
