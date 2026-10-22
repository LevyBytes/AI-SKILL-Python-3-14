# Decorate-Sort-Undecorate

### Decorate-Sort-Undecorate

The name Decorate-Sort-Undecorate comes straight from the three stages of the technique:

- To begin, each entry of the starting list is paired with fresh values that dictate how the ordering should go.

- Next, that decorated list gets sorted.

- At the end, those added values are stripped away, leaving a list that holds only the original entries arranged in the freshly determined order.

To order the student records by *grade* with the DSU method, for example:

```pycon
>>> decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
>>> decorated.sort()
>>> [student for grade, i, student in decorated]               # undecorate
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

```

The reason this works is that tuples compare lexicographically: their leading items are weighed against one another first, and only when those tie are the next items considered, and so forth.

Strictly speaking you don't always have to put the index *i* into the decorated list, yet doing so yields a couple of advantages:

- The ordering stays stable – when two entries carry the same key, the sorted list keeps them in their original sequence.

- The underlying entries need not be comparable themselves, because at most the first two slots of the decorated tuples settle the ordering. Thus the starting list might, for instance, hold complex numbers, which on their own cannot be sorted.

This same pattern also goes by the label [Schwartzian transform](https://en.wikipedia.org/wiki/Schwartzian_transform), named for Randal L. Schwartz, the person who made it well known within the Perl community.

Since Python's sorting now offers key-functions, you rarely have call for this older technique.

[Subject index](INDEX.md) · [Previous source context](sort-stability-and-complex-sorts.md) · [Following source context](comparison-functions.md)
