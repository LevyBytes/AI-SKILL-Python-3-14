# Subclassing other types - PyTypeObject

### 2.5. Subclassing other types

You can build brand-new extension types that descend from types already in existence. Deriving from the built in types is the simplest route, because an extension can readily reuse the [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) it requires. Sharing such `PyTypeObject` structures across extension modules, by contrast, can prove tricky.

Here we'll build a `SubList` type descended from the built-in [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) type. The new type stays fully interoperable with ordinary lists, yet gains one extra `increment()` method that bumps an internal counter:

```pycon
>>> import sublist
>>> s = sublist.SubList(range(3))
>>> s.extend(s)
>>> print(len(s))
6
>>> print(s.increment())
1
>>> print(s.increment())
2

```

[Subject index](INDEX.md) · [Previous source section](supporting-cyclic-garbage-collection-and-pytypeobject.md) · [Required Subclassing list with SubList continuation](subclassing-list-with-sublist-and-pymoduledef-init.md)
