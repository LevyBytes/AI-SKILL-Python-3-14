# What’s New in Python 2.0 / List Comprehensions

### List Comprehensions

Lists are a hardworking data type in Python, and a great many programs handle a list somewhere along the way. Two frequent things you do with lists are iterate through them and either select the elements satisfying some test, or apply a function to every element. As an example, with a list of strings on hand, you might wish to extract all the strings holding a particular substring, or trim trailing whitespace off each line.

The existing [`map()`](https://docs.python.org/3.14/library/functions.html#map) and [`filter()`](https://docs.python.org/3.14/library/functions.html#filter) functions can serve this need, but they demand a function among their arguments. That’s acceptable when a suitable built-in function exists to hand over directly, but absent one, you must write a tiny function to perform the needed work, and Python’s scoping rules make the outcome unsightly whenever that tiny function requires extra information. Consider the opening example from the prior paragraph, locating every string in the list that contains a given substring. You might write the following to accomplish it:

```python
# Given the list L, make a list of all strings
# containing the substring S.
sublist = filter( lambda s, substring=S:
                     string.find(s, substring) != -1,
                  L)

```

Owing to Python’s scoping rules, a default argument gets employed so the anonymous function produced by the [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expression is aware of which substring it’s hunting for. List comprehensions tidy this up:

```python
sublist = [ s for s in L if string.find(s, S) != -1 ]

```

List comprehensions take the shape:

```python
[ expression for expr in sequence1
             for expr2 in sequence2 ...
             for exprN in sequenceN
             if condition ]

```

The `for`…`in` clauses supply the sequences to iterate across. Those sequences needn’t share the same length, because they’re *not* traversed in parallel but rather from left to right; the paragraphs below spell this out more plainly. Each element of the produced list becomes the successive values of *expression*. That closing `if` clause is optional; when present, *expression* is evaluated and appended to the result only if *condition* holds true.

For maximum clarity on the semantics, a list comprehension corresponds to the following Python code:

```python
for expr1 in sequence1:
    for expr2 in sequence2:
    ...
        for exprN in sequenceN:
             if (condition):
                  # Append the value of
                  # the expression to the
                  # resulting list.

```

What this implies is that with several `for`…`in` clauses, the resulting list comes out equal to the product of the lengths of all the sequences. Given two lists each of length 3, the output list contains 9 elements:

```python
seq1 = 'abc'
seq2 = (1,2,3)
>>> [ (x,y) for x in seq1 for y in seq2]
[('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1),
('c', 2), ('c', 3)]

```

So as not to add an ambiguity to Python’s grammar, whenever *expression* builds a tuple, it has to be wrapped in parentheses. The first list comprehension below is a syntax error, whereas the second is valid:

```python
# Syntax error
[ x,y for x in seq1 for y in seq2]
# Correct
[ (x,y) for x in seq1 for y in seq2]

```

The concept of list comprehensions traces back to the functional programming language Haskell ([https://www.haskell.org](https://www.haskell.org)). Greg Ewing made the most persuasive case for bringing them into Python and authored the initial list comprehension patch, which was then debated for what felt like an eternity on the python-dev mailing list and kept current by Skip Montanaro.

[Subject index](INDEX.md) · [Previous source section](unicode.md) · [Next source section](augmented-assignment.md) · [Release/subject declaration](introduction.md)
