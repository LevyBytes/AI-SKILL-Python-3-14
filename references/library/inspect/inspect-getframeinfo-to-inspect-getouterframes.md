# inspect: `inspect.getframeinfo()`, `inspect.getouterframes()`

inspect.getframeinfo(*frame*, *context=1*)

Fetch details about a frame or traceback object. A `Traceback` object comes back.

Changed in version 3.11: The return value is now a `Traceback` object rather than a named tuple.

 inspect.getouterframes(*frame*, *context=1*)

[Subject index](INDEX.md) · [Previous](inspect-traceback-class.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: The interpreter stack](inspect-frameinfo-class.md) · [Required continuation of the source contract](inspect-getouterframes.md)
