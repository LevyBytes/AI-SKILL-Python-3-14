# stdtypes: GenericAlias construction and annotation purpose

### Generic Alias Type

Usually a `GenericAlias` object comes about by [subscripting](https://docs.python.org/3.14/reference/expressions.html#subscriptions) a class. The most frequent pairing is with [container classes](https://docs.python.org/3.14/reference/datamodel.html#sequence-types), like `list` or `dict`. To illustrate, `list[int]` is a `GenericAlias` object made by subscripting the `list` class with the argument [`int`](https://docs.python.org/3.14/library/functions.html#int). The primary purpose of `GenericAlias` objects is use within [type annotations](https://docs.python.org/3.14/glossary.html#term-annotation).

Note

As a rule, subscripting a class is possible only when that class implements the special method [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__).

A `GenericAlias` object stands in as a proxy for a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type), bringing *parameterized generics* to life.

In the case of a container class, the argument(s) handed to a [subscription](https://docs.python.org/3.14/reference/expressions.html#subscriptions) of that class can declare the type(s) of the elements held by an object. To illustrate, `set[bytes]` works in type annotations to denote a `set` whose elements are all of type `bytes`.

When a class defines [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) yet is not itself a container, the argument(s) handed to a subscription of that class will frequently declare the return type(s) of one or more of the object's methods. For instance, [`regular expressions`](https://docs.python.org/3.14/library/re.html#module-re) work over both the `str` data type and the `bytes` data type:

- Given `x = re.search('foo', 'foo')`, `x` becomes a [re.Match](https://docs.python.org/3.14/library/re.html#match-objects) object whose `x.group(0)` and `x[0]` both yield results of type `str`. Within type annotations, the `GenericAlias` `re.Match[str]` captures an object of this sort.

- Given `y = re.search(b'bar', b'bar')` (observe the `b` marking `bytes`), `y` is likewise a `re.Match` instance, yet here `y.group(0)` and `y[0]` both yield results of type `bytes`. To express this flavor of [re.Match](https://docs.python.org/3.14/library/re.html#match-objects) object in type annotations, we write `re.Match[bytes]`.

Every `GenericAlias` object is an instance of the class [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias), which itself can also build `GenericAlias` objects on the spot. Specializations of user-defined [generic classes](https://docs.python.org/3.14/reference/compound_stmts.html#generic-classes) might not be instances of `types.GenericAlias`, yet they deliver comparable functionality.

[Subject index](INDEX.md) · [Previous](type-annotation-types-generic-alias-union.md) · [Continue](generic-alias-type-average-and-send-post-request.md)
