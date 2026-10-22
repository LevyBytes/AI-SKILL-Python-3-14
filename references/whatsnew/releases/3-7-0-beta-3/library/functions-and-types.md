# Python 3.7.0 beta 3 / library / functions and types

[bpo-33009](https://bugs.python.org/issue?@action=redirect&bpo=33009): Correct inspect.signature() for single-parameter partialmethods.

[bpo-32873](https://bugs.python.org/issue?@action=redirect&bpo=32873): Treat type variables and special typing forms as immutable under copy and pickle. This corrects several small issues and inconsistencies while improving backwards compatibility with Python 3.6.

[bpo-32505](https://bugs.python.org/issue?@action=redirect&bpo=32505): Raise TypeError whenever a dataclass member variable has type Field yet carries no type annotation.

[bpo-32896](https://bugs.python.org/issue?@action=redirect&bpo=32896): Correct an error in which subclassing a dataclass that has a field using a default_factory produced an incorrect class.

[bpo-32953](https://bugs.python.org/issue?@action=redirect&bpo=32953): When a non-dataclass derives from a frozen dataclass, permit attributes to be added on the derived class. Only the attributes belonging to the frozen dataclass may not be assigned. Insist that every dataclass throughout a hierarchy be either all frozen or all non-frozen.

[bpo-33064](https://bugs.python.org/issue?@action=redirect&bpo=33064): lib2to3 now correctly handles trailing commas following `*args` and `**kwargs` in function signatures.

[bpo-32999](https://bugs.python.org/issue?@action=redirect&bpo=32999): Resolve the C implementation of `ABC.__subclasscheck__(cls, subclass)` crashing whenever `subclass` is not a type object.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
