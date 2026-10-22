# modules C API: Static module definitions and module construction

### Module definitions

Everything covered in the section above operates on any module object at all, including those that get imported from Python code.

C API modules normally rely on a *module definition*, `PyModuleDef` — a constant, statically allocated "description" laying out the way a module ought to be built.

That definition typically serves to set up an extension's "main" module object (consult [Defining extension modules](https://docs.python.org/3.14/c-api/extension-modules.html#extension-modules) for the specifics). Beyond that, it serves to build extension modules on the fly.

Where `PyModule_New()` differs, the definition supports handling of *module state* — a chunk of memory allocated and cleared in step with the module object. In contrast to the module's Python attributes, no Python code can swap out or remove what's stored in module state.

[Subject index](INDEX.md) · [Previous source contract](pymodule-getfilenameobject-to-pymodule-getfilename.md) · [Following source contract](pymoduledef-to-pymoduledef-type.md)
