# What's New in Python 2.5 / Optimizations - re, readline, struct

### Optimizations

A number of these optimizations originated at the NeedForSpeed sprint, which ran in Reykjavik, Iceland, between May 21–28 2006. That gathering concentrated on making the CPython implementation faster and was bankrolled by EWT LLC with on-site help from CCP Games. The optimizations contributed during the sprint carry a special mark in the list that follows.

- When the built-in [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) and [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) types first arrived in Python 2.4, they sat atop Python's dictionary type. With 2.5 the underlying data structure has been tailored specifically for sets, so sets now consume a third less memory and run a bit quicker. (Implemented by Raymond Hettinger.)

- Certain Unicode operations — locating substrings, splitting strings, and encoding and decoding through character maps — now run faster. (The substring search and splitting gains came from Fredrik Lundh and Andrew Dalke at the NeedForSpeed sprint. Walter Dörwald and Martin von Löwis improved the character maps.)

- For long strings of digits, the `long(str, base)` function now runs faster because it computes fewer intermediate results. The biggest gain, a 6 times speedup, shows up around 800–1000 digits. (Contributed by Alan McIntyre and committed at the NeedForSpeed sprint.)

- You can no longer combine iterating across a file with `for line in file` and invoking the file object's `read()`/[`readline()`](https://docs.python.org/3.14/library/readline.html#module-readline)/`readlines()` methods. Iteration relies on an internal buffer that the `read*()` methods bypass; those methods would instead hand back the data sitting past the buffer, so the data would surface out of order. Mixing iteration with these methods now causes the `read*()` method to raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). (Implemented by Thomas Wouters.)

- The [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module now translates structure format strings into an internal form and caches that form, delivering a 20% speedup. (Contributed by Bob Ippolito at the NeedForSpeed sprint.)

- By moving to Python's allocator functions in place of the system's `malloc()` and `free()`, the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module picked up a 1 or 2% speedup. (Contributed by Jack Diederich at the NeedForSpeed sprint.)

- The peephole optimizer in the code generator now carries out basic constant folding within expressions. Write something along the lines of `a = 2+3` and the code generator performs the arithmetic itself, emitting code that matches `a = 5`. (Proposed and implemented by Raymond Hettinger.)

- Function calls run faster now because each code object holds onto the most recently completed frame (a "zombie frame") in one of its internal fields and reuses it on the code object's next invocation. (Patch originally from Michael Hudson, then revised by Armin Rigo and Richard Jones, and committed during the NeedForSpeed sprint.) Frame objects, too, are a touch smaller, which can help cache locality and trim memory usage slightly. (Contributed by Neal Norwitz.)

- Python's built-in exceptions are now new-style classes, and that switch greatly accelerates instantiation. Thanks to this, version 2.4's exception handling is outpaced by Python 2.5's, which runs roughly 30% quicker. (At the NeedForSpeed sprint, this was contributed by Richard Jones, Georg Brandl and Sean Reifschneider.)

- Imports now remember which paths were tried, noting whether each one exists, so the interpreter issues fewer `open()` and `stat()` calls during startup. (Contributed by Martin von Löwis and Georg Brandl.)

[Subject index](INDEX.md) · [Previous source section](interactive-interpreter-changes.md) · [Next source section](standard-library-module-changes.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
