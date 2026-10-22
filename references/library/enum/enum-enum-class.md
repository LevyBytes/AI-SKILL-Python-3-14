# enum: `enum.Enum`

*class *enum.Enum

*Enum* is the foundation class underlying all *enum* enumerations.

 name

The name that was used when defining the `Enum` member:

```python
>>> Color.BLUE.name
'BLUE'

```

 value

The value assigned to the `Enum` member:

```python
>>> Color.RED.value
1

```

Value of the member, can be set in `__new__()`.

Note

Enum member values

A member value may be of any kind: [`int`](https://docs.python.org/3.14/library/functions.html#int), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), and so forth. When the precise value does not matter, reach for `auto` instances and a suitable value gets picked on your behalf. Refer to `auto` for the specifics.

Mutable/unhashable values — for instance [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), or a mutable [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) — are allowed, yet they incur a quadratic performance cost at creation time, scaling with the overall count of mutable/unhashable values present in the enum.

 _name_

Name of the member.

 _value_

Value of the member, can be set in `__new__()`.

 _order_

Now obsolete, retained only for backward compatibility. (A class attribute that gets stripped while the class is being built.)

You may supply the `_order_` attribute as an aid to keeping Python 2 / Python 3 code aligned. Its contents get compared against the enumeration's genuine ordering, and a mismatch between the two triggers an error:

```python
>>> class Color(Enum):
...     _order_ = 'RED GREEN BLUE'
...     RED = 1
...     BLUE = 3
...     GREEN = 2
...
Traceback (most recent call last):
...
TypeError: member order does not match _order_:
   ['RED', 'BLUE', 'GREEN']
   ['RED', 'GREEN', 'BLUE']

```

Note

Within Python 2 code the `_order_` attribute is required, since definition order disappears before there is any chance to capture it.

Added in version 3.6.

 _ignore_

`_ignore_` applies solely during creation and gets stripped from the enumeration after creation finishes.

`_ignore_` holds a list of names that will neither become members nor remain in the finished enumeration once creation completes. Refer to [TimePeriod](https://docs.python.org/3.14/howto/enum.html#enum-time-period) for an illustration.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](enum-enumtype-getitem-to-enum-enumtype-reversed.md) · [Continue](enum-enum-dir-to-enum-enum-init.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
