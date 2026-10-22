# Nested iteration products and tuple-expression syntax

The `for...in` clauses hold the sequences to iterate across. These sequences need not share the same length, since they're iterated from left to right **rather** than simultaneously. For every element of `sequence1`, `sequence2` is traversed from its start. `sequence3` is then traversed for each resulting pairing of elements drawn from `sequence1` and `sequence2`.

Said differently, a list comprehension or generator expression corresponds to the following Python code:

```python
for expr1 in sequence1:
    if not (condition1):
        continue   # Skip this element
    for expr2 in sequence2:
        if not (condition2):
            continue   # Skip this element
        ...
        for exprN in sequenceN:
            if not (conditionN):
                continue   # Skip this element

            # Output the value of
            # the expression.

```

What this implies is that when multiple `for...in` clauses appear with no `if` clauses, the length of the produced output equals the product of the lengths of every sequence. Given two lists each of length 3, the output list runs 9 elements long:

```python
>>> seq1 = 'abc'
>>> seq2 = (1, 2, 3)
>>> [(x, y) for x in seq1 for y in seq2]
[('a', 1), ('a', 2), ('a', 3),
 ('b', 1), ('b', 2), ('b', 3),
 ('c', 1), ('c', 2), ('c', 3)]

```

So as not to bring an ambiguity into Python's grammar, when `expression` produces a tuple, it has to be wrapped in parentheses. Of the two examples that follow, the first list comprehension raises a syntax error, whereas the second is written correctly:

```python
# Syntax error
[x, y for x in seq1 for y in seq2]
# Correct
[(x, y) for x in seq1 for y in seq2]

```

[Subject index](INDEX.md) · [Generator expressions and list comprehensions syntax and filtering](generator-expression-and-comprehension-filtering.md) · [Previous source context](generator-expression-and-comprehension-filtering.md) · [Following source context](generators.md)
