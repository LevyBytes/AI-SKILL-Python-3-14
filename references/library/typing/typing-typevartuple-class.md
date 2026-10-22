# typing: `typing.TypeVarTuple`

*class *typing.TypeVarTuple(*name*, ***, *default=typing.NoDefault*)

Type variable tuple. This specialized kind of type variable makes *variadic* generics possible.

You can declare type variable tuples within [type parameter lists](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) by placing a lone asterisk (`*`) ahead of the name:

```python
def move_first_element_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])

```

Alternatively, you can call the `TypeVarTuple` constructor explicitly:

```python
T = TypeVar("T")
Ts = TypeVarTuple("Ts")

def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])

```

An ordinary type variable supports parameterization by a single type. By contrast, a type variable tuple permits parameterization by an *arbitrary* count of types, behaving as though it were an *arbitrary* count of type variables packed inside a tuple. For instance:

```python
# T is bound to int, Ts is bound to ()
# Return value is (1,), which has type tuple[int]
move_first_element_to_last(tup=(1,))

# T is bound to int, Ts is bound to (str,)
# Return value is ('spam', 1), which has type tuple[str, int]
move_first_element_to_last(tup=(1, 'spam'))

# T is bound to int, Ts is bound to (str, float)
# Return value is ('spam', 3.0, 1), which has type tuple[str, float, int]
move_first_element_to_last(tup=(1, 'spam', 3.0))

# This fails to type check (and fails at runtime)
# because tuple[()] is not compatible with tuple[T, *Ts]
# (at least one element is required)
move_first_element_to_last(tup=())

```

Observe the unpacking operator `*` appearing in `tuple[T, *Ts]`. You can picture `Ts` as a tuple of type variables `(T1, T2, ...)`. From there `tuple[T, *Ts]` turns into `tuple[T, *(T1, T2, ...)]`, which is the same as `tuple[T, T1, T2, ...]`. (Be aware that earlier Python releases may instead render this with `Unpack`, as `Unpack[Ts]`.)

Type variable tuples have to be unpacked *every* time. Doing so keeps type variable tuples distinct from ordinary type variables:

```python
x: Ts          # Not valid
x: tuple[Ts]   # Not valid
x: tuple[*Ts]  # The correct way to do it

```

You may apply type variable tuples in the very same settings as ordinary type variables. Take class definitions, arguments, and return types, for example:

```python
class Array[*Shape]:
    def __getitem__(self, key: tuple[*Shape]) -> float: ...
    def __abs__(self) -> "Array[*Shape]": ...
    def get_shape(self) -> tuple[*Shape]: ...

```

Type variable tuples mix together perfectly well with ordinary type variables:

```python
class Array[DType, *Shape]:  # This is fine
    pass

class Array2[*Shape, DType]:  # This would also be fine
    pass

class Height: ...
class Width: ...

float_array_1d: Array[float, Height] = Array()     # Totally fine
int_array_2d: Array[int, Height, Width] = Array()  # Yup, fine too

```

[Subject index](INDEX.md) · [Previous](typing-typevar-evaluate-bound-to-typing-typevar-has-default.md) · [Continue](typevartuple-variadic-constraints.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)
