# What’s New in Python 2.4 / Optimizations

### Optimizations

- The inner loops handling list and tuple slicing were tuned and now execute roughly a third quicker. The inner loops for dictionaries also got tuned, yielding speed gains for `keys()`, `values()`, `items()`, `iterkeys()`, `itervalues()`, and `iteritems()`. (Contributed by Raymond Hettinger.)

- The machinery used to grow and shrink lists was tuned for both speed and space efficiency. Appending to and popping from lists now goes faster thanks to leaner code paths and reduced reliance on the underlying system `realloc()`. List comprehensions gain from this as well. [`list.extend()`](https://docs.python.org/3.14/library/stdtypes.html#list.extend) was also tuned and no longer turns its argument into a temporary list ahead of extending the base list. (Contributed by Raymond Hettinger.)

- [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list), [`tuple()`](https://docs.python.org/3.14/library/stdtypes.html#tuple), [`map()`](https://docs.python.org/3.14/library/functions.html#map), [`filter()`](https://docs.python.org/3.14/library/functions.html#filter), and [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) now operate several times more quickly when handed non-sequence arguments that provide a `__len__()` method. (Contributed by Raymond Hettinger.)

- The methods `list.__getitem__()`, `dict.__getitem__()`, and `dict.__contains__()` are now realized as `method_descriptor` objects in place of `wrapper_descriptor` objects. This style of access doubles how fast they run and renders them better suited as arguments to functionals: `map(mydict.__getitem__, keylist)`. (Contributed by Raymond Hettinger.)

- A new opcode, `LIST_APPEND`, was added; it streamlines the bytecode generated for list comprehensions and makes them roughly a third faster. (Contributed by Raymond Hettinger.)

- The peephole bytecode optimizer has been enhanced to emit shorter, quicker bytecode; remarkably, the bytecode it produces is more readable. (Enhanced by Raymond Hettinger.)

- String concatenations written as `s = s + "abc"` and `s += "abc"` are now carried out more efficiently under certain conditions. Other Python implementations such as Jython won't include this optimization, so you shouldn't depend on it; the `join()` method of strings remains the recommended way to efficiently glue together a large number of strings. (Contributed by Armin Rigo.)

Taken together, these tuning efforts mean that, on the pystone benchmark, Python 2.4 comes in about 5% quicker than Python 2.3, and a full 35% quicker than Python 2.2. (pystone isn't an especially good benchmark, but it remains the most widely used gauge of Python's performance. Your own applications might display larger or smaller gains from Python 2.4.)

[Subject index](INDEX.md) · [Previous source section](sorted-builtin-numeric-and-module-launch-changes.md) · [Next source section](new-improved-and-deprecated-modules.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
