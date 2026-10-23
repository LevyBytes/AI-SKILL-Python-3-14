# annotationlib - Security implications of introspecting annotations

### Security implications of introspecting annotations

A good deal of what this module does entails running annotation-related code, which is then free to do whatever it pleases. To take two cases, `get_annotations()` can call into an arbitrary [annotate function](https://docs.python.org/3.14/glossary.html#term-annotate-function), and `ForwardRef.evaluate()` can run [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) over an arbitrary string. Whatever code lives inside an annotation could fire off arbitrary system calls, spin forever in a loop, or carry out any other action. The same holds for every read of the [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotations__) attribute and for an assortment of annotation-handling functions in the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module, [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints) among them.

Whatever security problem this gives rise to is already live the instant you import code that might harbor untrusted annotations: the mere act of importing code can always set arbitrary operations in motion. Even so, it is unsafe to take in strings or other input from an untrusted origin and feed them to any of the annotation-introspection APIs — by, for instance, reworking an `__annotations__` dictionary or building a `ForwardRef` object outright.

[Subject index](INDEX.md) · [Previous](limitations-of-the-forwardref-format.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md)
