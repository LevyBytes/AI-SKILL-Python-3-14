# Why doesn't CPython use a more traditional garbage collection scheme?

### Why doesn't CPython use a more traditional garbage collection scheme?

For starters, that isn't a C standard feature and is consequently not portable. (Yes, the Boehm GC library is known to us. It carries snippets of assembler code for *most* common platforms, though not every one, and while it's mostly transparent, it isn't fully transparent; patches are needed to make Python operate with it.)

Traditional GC likewise becomes troublesome once Python is embedded inside other applications. Although replacing the standard `malloc()` and `free()` with versions from the GC library is fine in a standalone Python, an application embedding Python may wish to provide its *own* replacement for `malloc()` and `free()`, and may not want Python's. As things stand, CPython works with anything that implements `malloc()` and `free()` correctly.

[Subject index](INDEX.md)
