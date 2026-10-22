# annotationlib: `annotationlib.Format`

### Classes

 *class *annotationlib.Format

An [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum) that enumerates the formats annotations may be returned in. The enum members, or the integers that correspond to them, may be handed to `get_annotations()` and the module's other functions, and likewise to [`__annotate__`](https://docs.python.org/3.14/reference/datamodel.html#object.__annotate__) functions.

 VALUE* = 1*

Values are what you get from evaluating the annotation expressions.

 VALUE_WITH_FAKE_GLOBALS* = 2*

A special value that flags an annotate function as running inside a special environment furnished with fake globals. On receiving this value, an annotate function should either hand back the same result it would for the `Format.VALUE` format, or raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) to indicate it has no support for running in such an environment. This format serves only internal purposes and ought not be handed to the functions of this module.

 FORWARDREF* = 3*

Values are genuine annotation values (matching the `Format.VALUE` format) where the values are defined, and `ForwardRef` proxies where they are undefined. The genuine objects may themselves hold references to `ForwardRef` proxy objects.

 STRING* = 4*

Values are the textual form of the annotation as written in the source code, subject to modifications that include — but are not limited to — whitespace normalizations and constant values optimizations.

The precise content of these strings is liable to change across future Python versions.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](annotation-semantics.md) · [Continue](forward-reference-class-and-evaluation.md) · [Owning module, declaration or section: annotationlib](annotationlib-functionality-for-introspecting-annotations.md)
