# enum.EnumType: `__call__()`, `__contains__()`, `__dir__()`

__call__(*cls*, *value*, *names=None*, ***, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)

There are two distinct ways this method gets invoked:

- to find an already-existing member:

>

cls:

The enum class on which the call is made.

value:

The value to lookup.

- to have the `cls` enum build a fresh enum (applicable only when the current enum holds no members):

>

cls:

The enum class on which the call is made.

value:

The name of the new Enum to create.

names:

The names/values of the members for the new Enum.

module:

The name of the module the new Enum is created in.

qualname:

The actual location in the module where this Enum can be found.

type:

A mix-in type for the new Enum.

start:

The first integer value for the Enum (used by `auto`).

boundary:

How to handle out-of-range values from bit operations (`Flag` only).

 __contains__(*cls*, *member*)

Yields `True` when member is part of the `cls`:

```python
>>> some_var = Color.RED
>>> some_var in Color
True
>>> Color.RED.value in Color
True

```

Changed in version 3.12: Earlier than Python 3.12, a `TypeError` would be raised whenever a non-Enum-member appeared in a containment check.

 __dir__(*cls*)

Yields `['__class__', '__doc__', '__members__', '__module__']` together with the names of the members in *cls*:

```python
>>> dir(Color)
['BLUE', 'GREEN', 'RED', '__class__', '__contains__', '__doc__', '__getitem__', '__init_subclass__', '__iter__', '__len__', '__members__', '__module__', '__name__', '__qualname__']

```

[Subject index](INDEX.md) · [Previous](enum-enumtype-class.md) · [Continue](enum-enumtype-getitem-to-enum-enumtype-reversed.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: enum.EnumType](enum-enumtype-class.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
