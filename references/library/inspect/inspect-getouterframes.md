# inspect - inspect.getouterframes

Obtain a list of `FrameInfo` objects covering a frame together with every frame surrounding it. Those frames stand for the chain of calls that brought *frame* into being. At the head of the returned list sits *frame* itself, while the tail holds the outermost call along *frame*’s stack.

Changed in version 3.5: What comes back is a list of [named tuples](https://docs.python.org/3.14/glossary.html#term-named-tuple), each shaped as `FrameInfo(frame, filename, lineno, function, code_context, index)`.

Changed in version 3.11: The result is now a list of `FrameInfo` objects.

[Subject index](INDEX.md) · [Continue](inspect-getinnerframes-to-inspect-trace.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: inspect.getouterframes](inspect-getframeinfo-to-inspect-getouterframes.md) · [Preceding source contract and version conditions](inspect-getframeinfo-to-inspect-getouterframes.md)
