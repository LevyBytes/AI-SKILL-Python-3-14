# What’s New in Python 2.6 / Optimizations — warnings

### Optimizations

- The [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module has been reimplemented in C. That lets the parser raise warnings and may also shorten the interpreter’s startup time. (Contributed by Neal Norwitz and Brett Cannon; [bpo-1631171](https://bugs.python.org/issue?@action=redirect&bpo=1631171).)

- Type objects now keep a method cache that can cut down the effort of locating the right method implementation for a given class; after a hit is cached, the interpreter need not walk base classes to settle on the correct method to invoke. Modifying a base class or the class itself flushes the cache, so even amid Python’s dynamic behavior the cache stays accurate. (The original optimization came from Armin Rigo; Kevin Jacobs brought it up to date for Python 2.6; [bpo-1700288](https://bugs.python.org/issue?@action=redirect&bpo=1700288).)

Out of the box, this applies only to the types bundled with the Python core. Extension modules are not guaranteed to play nicely with the cache, so each must deliberately set [`Py_TPFLAGS_HAVE_VERSION_TAG`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VERSION_TAG) in the module’s `tp_flags` field to turn the method cache on. (For cache compatibility, an extension module’s code must avoid directly reaching into and altering the `tp_dict` member of any type it defines. Few modules do that, but the Python interpreter has no way to know for sure. See [bpo-1878](https://bugs.python.org/issue?@action=redirect&bpo=1878) for some discussion.)

- Function calls that pass keyword arguments are now considerably quicker, since a fast pointer comparison generally avoids having to do a full string comparison. (Contributed by Raymond Hettinger; the first implementation came from Antoine Pitrou; [bpo-1819](https://bugs.python.org/issue?@action=redirect&bpo=1819).)

-

Every function exposed by the [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module was reimplemented in C as an outcome of the Need For Speed sprint. (Contributed by Raymond Hettinger.)

- A handful of the standard built-in types now flip a flag bit inside their type objects. The effect is a faster test for whether some object is a subclass of one of those types. (Contributed by Neal Norwitz.)

- Detection of whitespace and line breaks in Unicode strings now runs through quicker code; as a result the `split()` method is roughly 25% faster and `splitlines()` about 35% faster. (Contributed by Antoine Pitrou.) Routing the Unicode string’s data through pymalloc also cuts down on memory usage.

- The `with` statement now keeps the [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method on the stack, which yields a modest speedup. (Implemented by Jeffrey Yasskin.)

- So that less memory is held, the garbage collector now flushes its internal free lists when it collects the oldest generation of objects. The upshot is that memory can be handed back to the operating system earlier.

[Subject index](INDEX.md) · [Previous source section](complex-parsing-and-language-behavior.md) · [Release/subject declaration](python-3-0.md) · [Next source section](interpreter-changes.md)
