# pprint: `pprint.pp()`, `pprint.pprint()`, `pprint.pformat()`, `pprint.isreadable()`, `pprint.isrecursive()`

### Functions

`pprint.pp(*object*, *stream=None*, *indent=1*, *width=80*, *depth=None*, ***, *compact=False*, *sort_dicts=False*, *underscore_numbers=False*)`

Writes out the formatted representation of *object* and then a newline. Inside the interactive interpreter you can call this in place of the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function to inspect values. Tip: within a scope you may rebind `print = pprint.pp`.

Parameters:

- **object** – Whichever object you want printed.

- **stream** ([file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) | None) – The file-like object the output goes to, by way of its `write()` method. Leave it at the `None` default and [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) takes over.

- **indent** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – How much indentation is tacked on at each nesting level.

- **width** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The target ceiling on characters per output line. Where a structure simply won't fit under that limit, a best effort is made.

- **depth** ([*int*](https://docs.python.org/3.14/library/functions.html#int)* | **None*) – How many nesting levels are allowed to print. Whenever the structure under print runs deeper than that, the next level inward is swapped for `...`. Left at the `None` default, there is no cap on how deep formatting goes.

- **compact** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – Governs how lengthy [sequences](https://docs.python.org/3.14/glossary.html#term-sequence) get laid out. At the `False` default, every sequence item lands on its own line; otherwise each output line packs in as many items as the *width* permits.

- **sort_dicts** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `True`, a dictionary prints with its keys sorted; otherwise the keys appear in insertion order, which is the default.

- **underscore_numbers** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)) – When `True`, integers print using the `_` character as a thousands separator; otherwise no underscores show, which is the default.

```python
>>> import pprint
>>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
>>> stuff.insert(0, stuff)
>>> pprint.pp(stuff)
[<Recursion on list with id=...>,
 'spam',
 'eggs',
 'lumberjack',
 'knights',
 'ni']

```

Added in version 3.8.

`pprint.pprint(*object*, *stream=None*, *indent=1*, *width=80*, *depth=None*, ***, *compact=False*, *sort_dicts=True*, *underscore_numbers=False*)`

An alias for `pp()` whose *sort_dicts* defaults to `True`, so the dictionaries' keys get sorted for you automatically; reach for `pp()` instead, where that default is `False`, if you'd rather skip the sorting.

`pprint.pformat(*object*, *indent=1*, *width=80*, *depth=None*, ***, *compact=False*, *sort_dicts=True*, *underscore_numbers=False*)`

Hands back the formatted representation of *object* as a string. The *indent*, *width*, *depth*, *compact*, *sort_dicts*, and *underscore_numbers* values feed into the `PrettyPrinter` constructor as formatting parameters, carrying the meanings spelled out above.

`pprint.isreadable(*object*)`

Works out whether the formatted representation of *object* is “readable” — that is, whether [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) could rebuild the value from it. For recursive objects it always gives back `False`.

```python
>>> pprint.isreadable(stuff)
False

```

`pprint.isrecursive(*object*)`

Works out whether *object* calls for a recursive representation. The same caveats noted under `saferepr()` below apply to this function, and it may throw a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) should it miss a recursive object.

[Subject index](INDEX.md) · [Previous](pprint-data-pretty-printer.md) · [Continue](pprint-saferepr.md) · [Owning module, declaration or section: pprint](pprint-data-pretty-printer.md)
