# List indexing, concatenation, mutation and append

### 3.1.3. Lists

Python provides several *compound* data types for bundling other values together. The handiest of these is the *list*, expressed as comma-separated values (items) wrapped in square brackets. Although a list may hold items of varying types, most of the time the items share one type.

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]

```

Just as with strings (and every other built-in [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) type), lists accept indexing and slicing:

```python
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]

```

Concatenation and similar operations work on lists as well:

```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

```

Strings stay [immutable](https://docs.python.org/3.14/glossary.html#term-immutable), but lists differ: a list is a [mutable](https://docs.python.org/3.14/glossary.html#term-mutable) type, meaning its contents can be altered:

```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]

```

Tacking fresh items onto the tail of the list is also possible through the [`list.append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append) *method* (methods get covered more fully later):

```python
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]

```

[Subject index](INDEX.md) · [Previous source section](string-bounds-immutability-length-and-further-operations.md) · [Following source section](list-aliasing-shallow-copies-slice-assignment-and-nesting.md) · [Related tutorial example and explanation](list-aliasing-shallow-copies-slice-assignment-and-nesting.md)
