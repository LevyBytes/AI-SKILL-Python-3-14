# 7.11. The `import` statement

### 7.11. The `import` statement

```text

import_stmt:     "import" module "as" [identifier] ("," module "as" [identifier])*
                 | "from" relative_module "import" identifier "as" [identifier]
                 ("," identifier "as" [identifier])*
                 | "from" relative_module "import" "(" identifier "as" [identifier]
                 ("," identifier "as" [identifier])* [","] ")"
                 | "from" relative_module "import" "*"
module:          (identifier ".")* identifier
relative_module: "."* module | "."+
```

Running the plain import statement (the one lacking a `from` clause) happens across two stages:

1.

locate a module, then load and initialize it where that is needed

2.

bind a name or names within the current namespace for the scope at which the `import` statement sits, behaving exactly as an assignment statement would (carrying `global` and `nonlocal` semantics too).

Where the statement holds several clauses (set off by commas), both stages get performed individually for every clause, precisely as if each clause had been broken out into its own import statement.

What the first stage involves — locating and loading modules — gets laid out at much greater length in the section covering the [import system](https://docs.python.org/3.14/reference/import.html#importsystem), which additionally walks through the assorted kinds of packages and modules eligible for import along with every hook available for tailoring the import system. Note that a failure at this stage can signal either that the module went undiscovered, *or* that something went wrong while initializing it, which covers running the module's own code.

Once the asked-for module is fetched without trouble, it surfaces in the local namespace by one of three routes:

- Where `as` trails the module name, the name written after `as` gets bound straight to the imported module.

- Where no alternative name is given and the module under import is a top-level one, that module's name is bound within the local namespace as a reference pointing at the imported module

- Where the module under import is *not* a top-level one, it is the name of the top-level package holding that module that gets bound within the local namespace as a reference to the top-level package. You then have to reach the imported module by its complete qualified name instead of directly

The `from` variant follows a somewhat more involved procedure:

1.

locate the module named in the `from` clause, then load and initialize it where that is needed;

2.

working through every identifier named across the `import` clauses:

  1.

determine whether the imported module carries an attribute under that name

  2.

failing that, try importing a submodule by that name and then re-examine the imported module for the attribute

  3.

where the attribute remains absent, [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) gets raised.

  4.

otherwise the current namespace stores a reference to that value, taking the name from the `as` clause where one exists and falling back on the attribute name where it does not

Examples:

```python
import foo                 # foo imported and bound locally
import foo.bar.baz         # foo, foo.bar, and foo.bar.baz imported, foo bound locally
import foo.bar.baz as fbb  # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as fbb
from foo.bar import baz    # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as baz
from foo import attr       # foo imported and foo.attr bound as attr

```

Where a star (`'*'`) stands in for the identifier list, every public name the module defines gets bound into the local namespace for the scope at which the `import` statement sits.

A module's *public names* are worked out by inspecting that module's namespace for a variable called `__all__`; whenever it is defined, it has to be a sequence of strings naming things the module defines or imports. Any name holding non-ASCII characters has to follow the NFKC [normalization form](https://www.unicode.org/reports/tr15/#Norm_Forms); turn to [Non-ASCII characters in names](https://docs.python.org/3.14/reference/lexical_analysis.html#lexical-names-nonascii) for the particulars. Whatever names `__all__` lists count as public and are obliged to exist. Absent a defined `__all__`, the public-name set takes in each name within the module's namespace that does not open with an underscore (`'_'`). The whole public API ought to live in `__all__`. Its purpose is to keep you from inadvertently exporting things outside the API (library modules, say, that the module imported and made use of internally).

The wildcard flavor of import — `from module import *` — is sanctioned solely at module level. Trying it within class or function definitions provokes a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError).

Picking a module to import does not oblige you to write out the module's absolute name. Whenever a module or package nests inside another package, you can perform a relative import within that same top package while leaving the package name unstated. Placing leading dots ahead of the module or package named after `from` lets you indicate how far up the present package hierarchy to climb without writing exact names. A single leading dot stands for the present package where the importing module lives. A pair of dots climbs one package level. Three dots climbs two levels, and onward. Thus running `from . import mod` out of a module inside the `pkg` package winds up importing `pkg.mod`. Running `from ..subpkg2 import mod` from within `pkg.subpkg1` brings in `pkg.subpkg2.mod`. You will find the specification governing relative imports in the [Package Relative Imports](https://docs.python.org/3.14/reference/import.html#relativeimports) section.

For applications that work out at runtime which modules to load, [`importlib.import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) is supplied.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `import` with arguments `module`, `filename`, `sys.path`, `sys.meta_path`, `sys.path_hooks`.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-continue-statement.md) · [Following source section](future-statements.md)
