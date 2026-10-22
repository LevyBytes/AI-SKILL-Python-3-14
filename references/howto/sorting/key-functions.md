# Key Functions

### Key Functions

Both the [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method and the functions [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted), [`min()`](https://docs.python.org/3.14/library/functions.html#min), [`max()`](https://docs.python.org/3.14/library/functions.html#max), [`heapq.nsmallest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nsmallest), and [`heapq.nlargest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nlargest) expose a *key* parameter, which names a function (or any callable) to apply to each element before comparisons take place.

As an illustration, the snippet below performs a case-insensitive string ordering by way of [`str.casefold()`](https://docs.python.org/3.14/library/stdtypes.html#str.casefold):

```pycon
>>> sorted("This is a test string from Andrew".split(), key=str.casefold)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

```

Whatever you assign to the *key* parameter must be a function (or other callable) that accepts one argument and yields the value to sort on. The approach stays fast because each input record triggers the key function only a single time.

It is frequently useful to order intricate objects by drawing on a few of an object’s indices as the sort keys. Consider:

```pycon
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

An identical approach applies just as well to objects that carry named attributes. For instance:

```pycon
>>> class Student:
...     def __init__(self, name, grade, age):
...         self.name = name
...         self.grade = grade
...         self.age = age
...     def __repr__(self):
...         return repr((self.name, self.grade, self.age))

>>> student_objects = [
...     Student('john', 'A', 15),
...     Student('jane', 'B', 12),
...     Student('dave', 'B', 10),
... ]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

You can build objects that have named attributes via an ordinary class, as demonstrated above, or instead as instances of a [`dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) or a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple).

[Subject index](INDEX.md) · [Previous source context](sorting-basics.md) · [Following source context](operator-module-functions-and-partial-function-evaluation.md)
