# Multiple module instances

### Multiple module instances

As a rule, extension modules aren't singletons. Suppose the [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) entry gets deleted and the module is imported once more: a brand-new module object comes into being, usually filled with newly minted method and type objects, while the previous module goes through ordinary garbage collection. The same thing happens with modules written purely in Python.

Further module instances can come about within [sub-interpreters](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support), or once the Python runtime has been reinitialized (through [`Py_Finalize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Finalize) followed by [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize)). Under those circumstances, letting module instances share Python objects would, in all likelihood, lead to crashes or undefined behavior.

The remedy is to keep every instance of an extension module *isolated*: a mutation to one instance ought not to quietly bleed into the rest, and whatever state the module holds — references to Python objects included — should belong to that one module instance alone. The guide at [Isolating Extension Modules](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-howto) walks through this in depth.

An easier route around the same trouble is [raising an error on repeated initialization](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-optout).

Every module is supposed to either work with [sub-interpreters](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support) or come right out and declare that it does not. Typically that comes from isolation or from refusing repeated initialization, per the preceding paragraphs. A module can also confine itself to the main interpreter by way of the [`Py_mod_multiple_interpreters`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_multiple_interpreters) slot.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](defining-extension-modules.md) · [Following source contract](pyinit-modulename-to-pymodinit-func.md)
