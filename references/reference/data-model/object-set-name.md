# object.__set_name__(*self*, *owner*, *name*)

object.__set_name__(*self*, *owner*, *name*)

Called automatically when the owning class *owner* is built. By then the object has been bound to *name* inside that class:

```python
class A:
    x = C()  # Automatically calls: x.__set_name__(A, 'x')

```

When the class variable is bound after its class has already been built, `__set_name__()` is not invoked automatically. Should you need it, you can invoke `__set_name__()` yourself:

```python
class A:
   pass

c = C()
A.x = c                  # The hook is not called
c.__set_name__(A, 'x')   # Manually invoke the hook

```

Consult Creating the class object for further details.

Added in version 3.6.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-class-creation.md) · [Previous source section](customizing-class-creation.md) · [Following source section](metaclasses.md)
