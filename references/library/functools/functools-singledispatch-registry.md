# functools — functools.singledispatch registry

```python
>>> fun.registry.keys()
dict_keys([<class 'NoneType'>, <class 'int'>, <class 'object'>,
          <class 'decimal.Decimal'>, <class 'list'>,
          <class 'float'>])
>>> fun.registry[float]
<function fun_num at 0x1035a2840>
>>> fun.registry[object]
<function fun at 0x103fe0000>

```

Added in version 3.4.

Changed in version 3.7: Type annotations are now accepted by the `register()` attribute.

Changed in version 3.11: The `register()` attribute now accepts [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union) in the role of a type annotation.

[Subject index](INDEX.md) · [Continue](functools-singledispatchmethod-class.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md) · [Owning module, declaration or section: functools.singledispatch registry](callable-utilities-signatures-and-contract.md) · [Preceding source contract and version conditions](functools-and-verbose-false.md)
