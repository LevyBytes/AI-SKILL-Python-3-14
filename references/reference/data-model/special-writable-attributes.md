# 3.2.8.1.2. Special writable attributes

##### 3.2.8.1.2. Special writable attributes

For the most part, assigning to these attributes triggers a type check on the value:

| Attribute | Meaning |
| --- | --- |
| function.__doc__ | The documentation string of the function, or `None` when there is none. |
| function.__name__ | The function’s name. See also: `__name__ attributes`. |
| function.__qualname__ | The qualified name of the function. See also: `__qualname__ attributes`. Added in version 3.3. |
| function.__module__ | The name of whatever module the function was defined in, or `None` when there is none. |
| function.__defaults__ | A `tuple` of the default values supplied for parameters that have defaults, or `None` when no parameter carries a default. |
| function.__code__ | The code object that represents the function body once compiled. |
| function.__dict__ | The namespace that backs arbitrary function attributes. See also: `__dict__ attributes`. |
| function.__annotations__ | A `dictionary` of parameter annotations. Its keys are the parameter names, together with `'return'` for the return annotation when one is given. See also: `object.__annotations__`. Changed in version 3.14: Evaluation of annotations is now deferred until needed. See **PEP 649**. |
| function.__annotate__ | This function’s annotate function, or `None` when the function bears no annotations. See `object.__annotate__`. Added in version 3.14. |
| function.__kwdefaults__ | A `dictionary` of the defaults for keyword-only parameters. |
| function.__type_params__ | A `tuple` holding a generic function’s type parameters. Added in version 3.12. |

Function objects additionally permit getting and setting arbitrary attributes, which is useful, for instance, for pinning metadata onto functions. The usual attribute dot-notation serves to get and set such attributes.

**CPython implementation detail:** As things stand, CPython grants function attributes solely to user-defined functions. Support for function attributes on built-in functions could arrive later.

You can dig up additional detail on a function’s definition from its code object, which the `__code__` attribute makes reachable.

##### 3.2.13.2.2. Special writable attributes

| frame.f_trace | When not `None`, a function invoked for assorted events while code runs (debuggers rely on this). By default an event fires upon each fresh source line (consult `f_trace_lines`). |
| --- | --- |
| frame.f_trace_lines | Assign `False` to this attribute to stop a tracing event from firing on every source line. |
| frame.f_trace_opcodes | Assign `True` to this attribute so that per-opcode events can be requested. Be aware that interpreter behaviour becomes undefined should exceptions thrown by the trace function escape into the function under trace. |
| frame.f_lineno | The frame’s current line number – assigning to this inside a trace function leaps to the named line (applies only to the bottom-most frame). By writing this attribute, a debugger can realize a Jump command (also called Set Next Statement). |

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Owning language section](user-defined-functions.md) · [Previous source section](special-read-only-attributes.md) · [Following source section](instance-methods.md) · [Owning language section](internal-types.md) · [Owning language section](frame-objects.md) · [Following source section](frame-object-methods.md)
