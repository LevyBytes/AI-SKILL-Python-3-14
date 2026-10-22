# 6.3.1. Attribute references

### 6.3.1. Attribute references

An attribute reference consists of a primary trailed by a period and a name:

```text

attributeref: primary "." identifier
```

The primary has to evaluate to an object whose type permits attribute references, as the majority of objects do. That object then gets asked to supply the attribute named by the identifier. Whatever type and value come back is dictated by the object itself. Evaluating the very same attribute reference more than once can return distinct objects.

You can customize this production by overriding either the [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) method or the [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) method. Python invokes the `__getattribute__()` method first, and it either returns a value or raises [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) when the attribute cannot be found.

When an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) gets raised and the object provides a `__getattr__()` method, that method runs as a fallback.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](primaries.md) · [Previous source section](primaries.md) · [Following source section](subscriptions-and-slicings.md)
