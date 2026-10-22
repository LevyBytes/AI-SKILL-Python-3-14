# inspect: `inspect.FrameInfo`

### The interpreter stack

A number of the functions below give back `FrameInfo` objects. To stay backwards compatible, these objects permit tuple-like operations across every attribute apart from `positions`. That behavior is regarded as deprecated and could be dropped down the road.

 *class *inspect.FrameInfo

 frame

The [frame object](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) to which the record corresponds.

[Subject index](INDEX.md) · [Previous](inspect-get-annotations.md) · [Continue](the-interpreter-stack.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md)
