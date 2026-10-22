# Frame objects

### Frame objects

Reaching for [`frame.f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) on a [frame](https://docs.python.org/3.14/reference/datamodel.html#frame-objects) object is unsafe while that same frame happens to be running in a separate thread; attempting it can bring the interpreter down.

[Subject index](INDEX.md) · [Previous source context](immortalization.md) · [Following source context](iterators.md)
