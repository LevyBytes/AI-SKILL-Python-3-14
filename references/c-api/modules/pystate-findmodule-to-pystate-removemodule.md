# Module lookup (single-phase initialization)

### Module lookup (single-phase initialization)

Under the legacy [single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#single-phase-initialization) initialization scheme, singleton modules are produced that can be looked up against the current interpreter. As a result, fetching the module object afterward needs nothing more than a reference to the module definition.

For modules produced through multi-phase initialization these functions fall flat, because a lone definition can spawn several such modules.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyState_FindModule(PyModuleDef *def)

*Return value: Borrowed reference.** Sits within the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Gives back the module object built from *def* for the current interpreter. Before this method works, the module object has to have been bound to the interpreter state through `PyState_AddModule()`. Where the matching module object cannot be located, or has yet to be bound to the interpreter state, `NULL` comes back.

 int PyState_AddModule([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module, PyModuleDef *def)

* Has belonged to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) ever since version 3.3.*

Binds whatever module object you hand the function to the interpreter state. That in turn makes the module object reachable through `PyState_FindModule()`.

Takes effect solely for modules produced via single-phase initialization.

Once a module relying on [single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#single-phase-initialization) has been imported, Python invokes `PyState_AddModule` for you, so calling it yourself from module initialization code is needless (though it does no harm). You only have to call it explicitly when the module’s own init code goes on to call `PyState_FindModule`. The function exists chiefly to support building alternative import mechanisms (whether by calling it outright, or by studying its implementation to learn which state updates are required).

Should a module have been bound earlier under the same *def*, the fresh *module* takes its place.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller.

It returns `-1` along with a set exception on error, or `0` when it succeeds.

Added in version 3.3.

 int PyState_RemoveModule(PyModuleDef *def)

* Has been in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) from version 3.3 onward.*

Strips the module object built from *def* out of the interpreter state. It returns `-1` along with a set exception on error, or `0` when it succeeds.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous source contract](pymodule-addstringconstant-to-pyunstable-module-setgil.md)
