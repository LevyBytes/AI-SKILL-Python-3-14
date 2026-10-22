# Operator Module Functions and Partial Function Evaluation

### Operator Module Functions and Partial Function Evaluation

Because the [key function](https://docs.python.org/3.14/glossary.html#term-key-function) idioms above come up so often, Python ships convenience helpers that render accessor functions both quicker and tidier. Within the [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator) module you will find [`itemgetter()`](https://docs.python.org/3.14/library/operator.html#operator.itemgetter), [`attrgetter()`](https://docs.python.org/3.14/library/operator.html#operator.attrgetter), as well as a [`methodcaller()`](https://docs.python.org/3.14/library/operator.html#operator.methodcaller) function.

Rewritten with those helpers, the earlier examples grow both leaner and faster:

```pycon
>>> from operator import itemgetter, attrgetter

>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

These operator module helpers also support sorting across several tiers at once. As an example, to order first on *grade* and then on *age*:

```pycon
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

```

The [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) module supplies one more handy device for constructing key-functions. Its [`partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) function can trim the [arity](https://en.wikipedia.org/wiki/Arity) of a function that takes several arguments, turning it into something fit to serve as a key-function.

```pycon
>>> from functools import partial
>>> from unicodedata import normalize

>>> names = 'Zoë Åbjørn Núñez Élana Zeke Abe Nubia Eloise'.split()

>>> sorted(names, key=partial(normalize, 'NFD'))
['Abe', 'Åbjørn', 'Eloise', 'Élana', 'Nubia', 'Núñez', 'Zeke', 'Zoë']

>>> sorted(names, key=partial(normalize, 'NFC'))
['Abe', 'Eloise', 'Nubia', 'Núñez', 'Zeke', 'Zoë', 'Åbjørn', 'Élana']

```

[Subject index](INDEX.md) · [Previous source context](key-functions.md) · [Following source context](ascending-and-descending.md)
