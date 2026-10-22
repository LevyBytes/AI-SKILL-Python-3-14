# 9.10. Generator Expressions

### 9.10. Generator Expressions

A number of basic generators can be written compactly as expressions, with a syntax echoing list comprehensions but swapping square brackets for parentheses. Such expressions suit cases where some surrounding function consumes the generator on the spot. Generator expressions run tighter though less flexible than fully spelled-out generator definitions, and they usually go easier on memory than the matching list comprehensions.

Examples:

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']

```

Footnotes

[Subject index](INDEX.md) · [Previous source section](generators.md)
