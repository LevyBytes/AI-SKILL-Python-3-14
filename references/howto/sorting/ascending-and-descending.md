# Ascending and Descending

### Ascending and Descending

Each of [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) and [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) takes a *reverse* parameter holding a boolean. Setting it signals that you want a descending order. To take the student records in descending *age* sequence, for instance:

```pycon
>>> sorted(student_tuples, key=itemgetter(2), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

>>> sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

```

[Subject index](INDEX.md) · [Previous source context](operator-module-functions-and-partial-function-evaluation.md) · [Following source context](sort-stability-and-complex-sorts.md)
