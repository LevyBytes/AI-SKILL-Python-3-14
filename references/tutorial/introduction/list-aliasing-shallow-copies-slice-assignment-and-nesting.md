# List aliasing, shallow copies, slice assignment and nesting

In Python, a plain assignment never duplicates data. Bind a list to a variable and that variable points at the *existing list*. Whatever you alter through one variable shows up through every other variable pointing at the same list.:

```python
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]

```

Every slice operation yields a fresh list holding the elements you asked for. Consequently the slice below produces a [shallow copy](https://docs.python.org/3.14/library/copy.html#shallow-vs-deep-copy) of the list:

```python
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
["Red", "Green", "Blue", "Alpha"]
>>> rgba
["Red", "Green", "Blue", "Alph"]

```

You can also assign into slices, and that move can even resize the list or wipe it out completely:

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]

```

The built-in [`len()`](https://docs.python.org/3.14/library/functions.html#len) function applies to lists too:

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4

```

Lists can be nested as well (lists holding other lists), for instance:

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'

```

[Subject index](INDEX.md) · [Previous source section](list-indexing-concatenation-mutation-and-append.md) · [Following source section](first-steps-towards-programming.md) · [Related tutorial example and explanation](list-indexing-concatenation-mutation-and-append.md)
