# stdtypes: `tuple`

### Tuples

Tuples are immutable sequences, generally serving to hold collections of heterogeneous data (such as the 2-tuples the [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) built-in yields). Tuples also fit cases calling for an immutable sequence of homogeneous data (for instance, to permit storage inside a `set` or `dict` instance).

 *class *tuple(*iterable=()*, */*)

Tuples can be constructed in several ways:

- Writing a pair of parentheses for the empty tuple: `()`

- Writing a trailing comma for a singleton tuple: `a,` or `(a,)`

- Separating items with commas: `a, b, c` or `(a, b, c)`

- Calling the `tuple()` built-in: `tuple()` or `tuple(iterable)`

The constructor produces a tuple with the same items, in the same order, as *iterable*'s items. *iterable* can be a sequence, a container that allows iteration, or an iterator object. Where *iterable* is already a tuple, it gets returned unaltered. To illustrate, `tuple('abc')` returns `('a', 'b', 'c')` and `tuple( [1, 2, 3] )` returns `(1, 2, 3)`. With no argument supplied, the constructor makes a new empty tuple, `()`.

[Subject index](INDEX.md) · [Previous](list-sort.md) · [Required continuation of the source contract](tuples.md)
