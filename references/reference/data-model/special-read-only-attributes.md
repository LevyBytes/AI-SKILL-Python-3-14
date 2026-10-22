# 3.2.8.1.1. Special read-only attributes

##### 3.2.8.1.1. Special read-only attributes

| Attribute | Meaning |
| --- | --- |
| function.__builtins__ | Points at the `dictionary` holding the builtins namespace for the function. Added in version 3.10. |
| function.__globals__ | Points at the `dictionary` holding the function’s global variables – that is, the global namespace belonging to the module where the function was defined. |
| function.__closure__ | Either `None` or a `tuple` whose cells hold bindings for whatever names appear in the `co_freevars` attribute of the function’s `code object`. Each cell object carries a `cell_contents` attribute, through which the cell’s value may be both read and written. |

##### 3.2.13.1.1. Special read-only attributes

| codeobject.co_name | The function name |
| --- | --- |
| codeobject.co_qualname | The fully qualified function name Added in version 3.11. |
| codeobject.co_argcount | How many positional parameters in total the function has (counting positional-only parameters along with parameters carrying default values) |
| codeobject.co_posonlyargcount | How many positional-only parameters the function has (counting arguments that carry default values) |
| codeobject.co_kwonlyargcount | How many keyword-only parameters the function has (counting arguments that carry default values) |
| codeobject.co_nlocals | How many local variables the function makes use of (parameters counted in) |
| codeobject.co_varnames | A `tuple` holding the names of the function’s local variables (beginning with the parameter names) |
| codeobject.co_cellvars | A `tuple` holding the names of those local variables referenced by one or more nested scopes within the function |
| codeobject.co_freevars | A `tuple` holding the names of free (closure) variables that a nested scope draws from an enclosing scope. See also `function.__closure__`. Note: names that are global or builtin are *not* counted among these. |
| codeobject.co_code | A string standing for the function’s ordered run of bytecode instructions |
| codeobject.co_consts | A `tuple` holding the literals that the function’s bytecode uses |
| codeobject.co_names | A `tuple` holding the names that the function’s bytecode uses |
| codeobject.co_filename | The name of the file out of which the code was compiled |
| codeobject.co_firstlineno | The line number belonging to the function’s first line |
| codeobject.co_lnotab | A string that encodes how bytecode offsets map onto line numbers. The interpreter’s source code spells out the specifics. Deprecated since version 3.12: For code objects this attribute is deprecated and could disappear in Python 3.15. |
| codeobject.co_stacksize | The stack size that the code object requires |
| codeobject.co_flags | An `integer` encoding a number of flags for the interpreter. |

These flag bits apply to `co_flags`: bit `0x04` is turned on when the function accepts an arbitrary count of positional arguments via the `*arguments` syntax; bit `0x08` is turned on when the function takes arbitrary keyword arguments through the `**keywords` syntax; bit `0x20` is turned on when the function is a generator. Consult [Code Objects Bit Flags](https://docs.python.org/3.14/library/inspect.html#inspect-module-co-flags) for what each of the flags that may appear actually means.

Declarations of future features (such as `from __future__ import division`) likewise consume bits within `co_flags` to record whether a given feature was enabled when a code object was compiled. Refer to [`compiler_flag`](https://docs.python.org/3.14/library/__future__.html#future__._Feature.compiler_flag).

The remaining bits of `co_flags` are kept aside for internal purposes.

When a code object stands for a function carrying a docstring, the [`CO_HAS_DOCSTRING`](https://docs.python.org/3.14/library/inspect.html#inspect.CO_HAS_DOCSTRING) bit becomes set within `co_flags`, and the leading entry of `co_consts` is that function’s docstring.

##### 3.2.13.2.1. Special read-only attributes

| frame.f_back | Refers to the prior stack frame (in the caller’s direction), or `None` when this happens to be the bottommost stack frame |
| --- | --- |
| frame.f_code | The code object running within this frame. Reading this attribute raises an auditing event `object.__getattr__` with arguments `obj` and `"f_code"`. |
| frame.f_locals | The mapping the frame consults when resolving local variables. Where the frame points at an optimized scope, a write-through proxy object may come back. Changed in version 3.13: Return a proxy for optimized scopes. |
| frame.f_globals | The dictionary the frame consults when resolving global variables |
| frame.f_builtins | The dictionary the frame consults when resolving built-in (intrinsic) names |
| frame.f_lasti | This frame object’s “precise instruction” (namely an index into the code object’s bytecode string) |
| frame.f_generator | The owning generator or coroutine object for this frame, or `None` when the frame belongs to a normal function. Added in version 3.14. |

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Owning language section](user-defined-functions.md) · [Previous source section](user-defined-functions.md) · [Following source section](special-writable-attributes.md) · [Owning language section](internal-types.md) · [Owning language section](code-objects.md) · [Previous source section](code-objects.md) · [Following source section](codeobject-co-positions.md) · [Owning language section](frame-objects.md) · [Previous source section](frame-objects.md)
