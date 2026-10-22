# Legacy single-phase initialization

### Legacy single-phase initialization

Attention

Single-phase initialization is an older way of setting up extension modules and carries recognized shortcomings and design flaws. Authors of extension modules are urged to reach for multi-phase initialization in its place.

Under single-phase initialization, the initialization function (`PyInit_modulename`) is expected to build, fill in, and return a module object. The usual approach relies on [`PyModule_Create()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_Create) together with functions such as [`PyModule_AddObjectRef()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObjectRef).

Here is how single-phase initialization departs from the default behavior:

- Single-phase modules are, or rather *contain*, “singletons”.

At the point of the module's first initialization, Python stashes away what lives in the module's `__dict__` — which is to say, ordinarily, the module's functions and types.

On every import after that, Python skips calling the initialization function. It instead spins up a fresh module object with a fresh `__dict__` and copies the stashed contents into it. Take, for instance, a single-phase module `_testsinglephase` [1] that declares a function `sum` alongside an exception class `error`:

```python
>>> import sys
>>> import _testsinglephase as one
>>> del sys.modules['_testsinglephase']
>>> import _testsinglephase as two
>>> one is two
False
>>> one.__dict__ is two.__dict__
False
>>> one.sum is two.sum
True
>>> one.error is two.error
True

```

Treat the precise behavior here as an implementation detail of CPython.

- Because `PyInit_modulename` accepts no *spec* argument, a portion of the import machinery's state gets preserved and then applied to the first appropriate module produced over the course of the `PyInit_modulename` call. Concretely, when a sub-module is brought in, this scheme attaches the parent package name in front of the module's name.

A `PyInit_modulename` function operating in single-phase mode ought to construct "its" module object at the earliest opportunity, ahead of any other module objects coming into existence.

- Non-ASCII module names (`PyInitU_modulename`) are not supported.

- Single-phase modules support module lookup functions like [`PyState_FindModule()`](https://docs.python.org/3.14/c-api/module.html#c.PyState_FindModule).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](defining-extension-modules.md) · [Previous source contract](pymoduledef-init.md) · [Following source contract](../file-objects/pyfile-fromfd-to-pyfile-writestring.md)
