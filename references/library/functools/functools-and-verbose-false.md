# functools — `functools` — Higher-order functions and operations on callable objects — Code example: >>> def nothing(arg, verbose=False):

```python
>>> def nothing(arg, verbose=False):
...     print("Nothing.")
...
>>> fun.register(type(None), nothing)

```

The `register()` attribute gives back the undecorated function. That permits stacking decorators, [`pickling`](https://docs.python.org/3.14/library/pickle.html#module-pickle), and writing unit tests for each variant on its own:

```python
>>> @fun.register(float)
... @fun.register(Decimal)
... def fun_num(arg, verbose=False):
...     if verbose:
...         print("Half of your number:", end=" ")
...     print(arg / 2)
...
>>> fun_num is fun
False

```

Once called, the generic function dispatches according to the first argument's type:

```python
>>> fun("Hello, world.")
Hello, world.
>>> fun("test.", verbose=True)
Let me just say, test.
>>> fun(42, verbose=True)
Strength in numbers, eh? 42
>>> fun(['spam', 'spam', 'eggs', 'spam'], verbose=True)
Enumerate this:
0 spam
1 spam
2 eggs
3 spam
>>> fun(None)
Nothing.
>>> fun(1.23)
0.615

```

Whenever no implementation is registered for a particular type, that type's method resolution order is consulted to locate a more generic implementation. The original function carrying the `@singledispatch` decorator is registered against the base [`object`](https://docs.python.org/3.14/library/functions.html#object) type, so it serves as the fallback when nothing better turns up.

Where an implementation has been registered against an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class), virtual subclasses of that base class get dispatched to the same implementation:

```python
>>> from collections.abc import Mapping
>>> @fun.register
... def _(arg: Mapping, verbose=False):
...     if verbose:
...         print("Keys & Values")
...     for key, value in arg.items():
...         print(key, "=>", value)
...
>>> fun({"a": "b"})
a => b

```

To find out which implementation the generic function picks for a given type, consult the `dispatch()` attribute:

```python
>>> fun.dispatch(float)
<function fun_num at 0x1035a2840>
>>> fun.dispatch(dict)    # note: default implementation
<function fun at 0x103fe0000>

```

To reach every registered implementation, consult the read-only `registry` attribute:

[Subject index](INDEX.md) · [Previous](callable-utilities-signatures-and-contract.md) · [Owning module, declaration or section: functools](cached-factorial-and-dataset-examples.md) · [Owning module, declaration or section: @functools.singledispatch](callable-utilities-signatures-and-contract.md) · [Required continuation of the source contract](functools-singledispatch-registry.md)
