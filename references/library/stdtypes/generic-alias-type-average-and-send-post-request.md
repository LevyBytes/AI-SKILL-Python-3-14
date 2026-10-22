# stdtypes: Parameterized container annotations and usage examples

T[X, Y, ...]

Produces a `GenericAlias` that stands for a type `T` parameterized by the types *X*, *Y*, and however many more the chosen `T` calls for. Take, for instance, a function that expects a `list` whose elements are [`float`](https://docs.python.org/3.14/library/functions.html#float):

```python
def average(values: list[float]) -> float:
    return sum(values) / len(values)

```

Here is another example for [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) objects, drawing on a `dict`, a generic type that takes two type parameters standing for the key type and the value type. In this case, the function looks for a `dict` whose keys are of type `str` and whose values are of type [`int`](https://docs.python.org/3.14/library/functions.html#int):

```python
def send_post_request(url: str, body: dict[str, int]) -> None:
    ...

```

For their second argument, the builtin functions [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) will not take `GenericAlias` types:

```python
>>> isinstance([1, 2], list[str])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: isinstance() argument 2 cannot be a parameterized generic

```

[Type annotations](https://docs.python.org/3.14/glossary.html#term-annotation) carry no enforcement from the Python runtime. That holds for generic types and their type parameters as well. As a container object is built from a `GenericAlias`, no check verifies the container's elements against their declared type. For instance, the code below is not recommended, yet it runs without raising errors:

```python
>>> t = list[str]
>>> t([1, 2, 3])
[1, 2, 3]

```

On top of that, parameterized generics shed their type parameters as the object is created:

```python
>>> t = list[str]
>>> type(t)
<class 'types.GenericAlias'>

>>> l = t()
>>> type(l)
<class 'list'>

```

At runtime, instances of `GenericAlias` are not classes, despite acting like classes (they can be instantiated and subclassed):

```python
>>> import inspect
>>> inspect.isclass(list[int])
False

```

The same goes for [user-defined generics](https://docs.python.org/3.14/library/typing.html#user-defined-generics).

Calling [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) or `str()` on a generic shows the parameterized type:

```python
>>> repr(list[int])
'list[int]'

>>> str(list[int])
'list[int]'

```

To head off slip-ups such as `dict[str][str]`, the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method of generic containers raises an exception:

```python
>>> dict[str][str]
Traceback (most recent call last):
  ...
TypeError: dict[str] is not a generic class

```

That said, expressions of this kind are legitimate once [type variables](https://docs.python.org/3.14/library/typing.html#generics) come into the picture. The index must carry as many elements as there are type variable items within the `GenericAlias` object's `__args__`.

```python
>>> from typing import TypeVar
>>> Y = TypeVar('Y')
>>> dict[str, Y][int]
dict[str, int]

```

[Subject index](INDEX.md) · [Previous](generic-alias-creation.md) · [Continue](asyncio-future-to-collections-abc-iterator.md) · [Owning module, declaration or section: Generic Alias Type](generic-alias-creation.md)
