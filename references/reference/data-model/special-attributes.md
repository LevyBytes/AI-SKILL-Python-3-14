# 3.2.10.1. Special attributes

#### 3.2.10.1. Special attributes

| Attribute | Meaning |
| --- | --- |
| type.__name__ | The class’s name. See also: `__name__ attributes`. |
| type.__qualname__ | The class’s qualified name. See also: `__qualname__ attributes`. |
| type.__module__ | The name of the module in which the class was defined. |
| type.__dict__ | A `mapping proxy` that exposes the class’s namespace as read-only. See also: `__dict__ attributes`. |
| type.__bases__ | A `tuple` listing the class’s bases. Typically, given a class declared as `class X(A, B, C)`, its `X.__bases__` equals precisely `(A, B, C)`. |
| type.__base__ | **CPython implementation detail:** Within the inheritance chain, the one base class that dictates how instances are laid out in memory. At the C level this attribute maps to `tp_base`. |
| type.__doc__ | The class’s documentation string, or `None` where none is defined. Subclasses do not inherit it. |
| type.__annotations__ | A dictionary holding the variable annotations gathered as the class body ran. See also: `__annotations__ attributes`. For guidance on handling `__annotations__` well, kindly consult `annotationlib`. Rather than reaching for this attribute directly, employ `annotationlib.get_annotations()`. Warning Reading the `__annotations__` attribute straight off a class object can hand back annotations belonging to a different class, particularly when the class, one of its bases, or a metaclass sits under `from __future__ import annotations`. Consult **749** for the specifics. Certain builtin classes lack this attribute. For user-defined classes that have no `__annotations__`, it amounts to an empty dictionary. Changed in version 3.14: Annotations now undergo lazy evaluation. See **PEP 649**. |
| type.__annotate__() | This class’s annotate function, or `None` where the class carries no annotations. See also: `__annotate__ attributes`. Added in version 3.14. |
| type.__type_params__ | A `tuple` holding the type parameters belonging to a generic class. Added in version 3.12. |
| type.__static_attributes__ | A `tuple` holding the names of this class’s attributes that get assigned via `self.X` within any function in its body. Added in version 3.13. |
| type.__firstlineno__ | The line number where the class definition begins, decorators included. Assigning the `__module__` attribute drops the `__firstlineno__` entry from the type’s dictionary. Added in version 3.13. |
| type.__mro__ | The `tuple` of classes weighed while searching for base classes throughout method resolution. |

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](custom-classes.md) · [Previous source section](custom-classes.md) · [Following source section](special-methods.md)
