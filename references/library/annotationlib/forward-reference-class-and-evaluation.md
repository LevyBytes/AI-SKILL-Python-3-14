# annotationlib / Classes: `annotationlib.ForwardRef`, `evaluate()`

*class *annotationlib.ForwardRef

A proxy object standing in for forward references within annotations.

You get back instances of this class whenever the `FORWARDREF` format is in play and an annotation holds a name that cannot be resolved. Such a situation arises when an annotation employs a forward reference — for example, where a class gets mentioned ahead of its definition.

 __forward_arg__

A string holding the code that was evaluated in order to yield the `ForwardRef`. This string may not match the original source exactly.

 evaluate(***, *owner=None*, *globals=None*, *locals=None*, *type_params=None*, *format=Format.VALUE*)

Evaluate the forward reference and return the value it produces.

When the *format* argument equals `VALUE` (its default), this method may raise an exception — for example a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) — should the forward reference name something that cannot be resolved. You can supply this method's arguments to bind names that would otherwise have no definition. When the *format* argument is `FORWARDREF`, the method never raises, though it may give back a `ForwardRef` instance. As an illustration, suppose the forward reference object carries the code `list[undefined]`, in which `undefined` is a name with no definition; evaluating it under the `FORWARDREF` format yields `list[ForwardRef('undefined')]`. When the *format* argument is `STRING`, the method returns `__forward_arg__`.

The *owner* parameter is the favored route for handing scope information into this method. A `ForwardRef`'s owner is whatever object holds the annotation the `ForwardRef` came out of — for instance a module object, a type object, or a function object.

The *globals*, *locals*, and *type_params* parameters offer a finer-grained way to shape which names are reachable as the `ForwardRef` is evaluated. *globals* and *locals* get forwarded to [`eval()`](https://docs.python.org/3.14/library/functions.html#eval), standing for the global and local namespaces against which the name is evaluated. The *type_params* parameter matters for objects built with the native syntax for [generic classes](https://docs.python.org/3.14/reference/compound_stmts.html#generic-classes) and [functions](https://docs.python.org/3.14/reference/compound_stmts.html#generic-functions). It is a tuple of [type parameters](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) in scope at the time the forward reference is being evaluated. For instance, when you evaluate a `ForwardRef` pulled from an annotation located in the class namespace of a generic class `C`, *type_params* ought to be set to `C.__type_params__`.

The `ForwardRef` instances that `get_annotations()` returns keep references to details about the scope they came from, so invoking this method with no extra arguments can be enough to evaluate them. `ForwardRef` instances produced by other routes might carry no scope details at all, in which case you may have to pass arguments to this method for evaluation to succeed.

When no *owner*, *globals*, *locals*, or *type_params* is supplied and the `ForwardRef` holds nothing about its origin, empty globals and locals dictionaries are used instead.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](annotationlib-format-class.md) · [Continue](annotation-string-conversion-and-evaluation.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md) · [Owning module, declaration or section: Classes](annotationlib-format-class.md)
