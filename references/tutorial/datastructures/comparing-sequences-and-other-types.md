# 5.8. Comparing Sequences and Other Types

### 5.8. Comparing Sequences and Other Types

A sequence object can generally be measured against another object that shares its sequence type. What governs that measurement is *lexicographical* ordering: the leading pair of elements is checked first, and any difference there settles the result outright; should they match, evaluation moves to the following pair, repeating this way until one of the operands runs out of elements. Whenever a pair under examination consists of nested sequences of identical kind, the same lexicographical rule applies in a recursive fashion. Two sequences whose every element matches are treated as equal. Where one acts as a leading prefix of its counterpart, the briefer of the pair counts as the lesser. For text, individual letters are ranked by their Unicode code point number. Below are a few illustrations of how same-typed sequences stack up against one another:

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

```

Keep in mind that pitting objects of unlike types against each other through `<` or `>` is permitted, so long as each object supplies suitable comparison methods. Take blended numeric kinds, for instance: they are weighed by what they numerically amount to, which makes 0 equal to 0.0, and similar cases follow. When no such method exists, the interpreter declines to invent some random order and instead throws a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception.

Footnotes

[Subject index](INDEX.md) · [Previous source section](more-on-conditions.md)
