# Overview of descriptor invocation

### Overview of descriptor invocation

You may call a descriptor outright via `desc.__get__(obj)` or `desc.__get__(None, cls)`.

More typically, though, attribute access invokes a descriptor on its own.

Evaluating `obj.x` searches for the attribute `x` along the chain of namespaces tied to `obj`. When that search turns up a descriptor outside the instance [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__), its [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) method runs in accordance with the precedence rules given below.

Exactly how invocation proceeds hinges on whether `obj` is an object, a class, or an instance of super.

[Subject index](INDEX.md) · [Previous source context](descriptor-protocol.md) · [Following source context](invocation-from-an-instance.md)
