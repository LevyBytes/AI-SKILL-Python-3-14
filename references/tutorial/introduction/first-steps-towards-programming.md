# 3.2. First Steps Towards Programming

### 3.2. First Steps Towards Programming

Naturally, Python handles jobs far beyond summing two and two. To illustrate, here is how to produce the opening stretch of the [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_sequence):

```python
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8

```

A handful of new features turn up in this example.

- That opening line carries a *multiple assignment*: variables `a` and `b` take on the new values 0 and 1 at the same moment. The closing line reuses the idea, showing that everything on the right-hand side is computed first, ahead of any assignment happening. Those right-hand side expressions are evaluated working left to right.

- The [`while`](https://docs.python.org/3.14/reference/compound_stmts.html#while) loop keeps running for as long as its condition (in this case `a < 10`) holds true. As is the case in C, Python treats every non-zero integer as true and zero as false. A string, a list, or really any sequence may serve as the condition too; whatever has a non-zero length counts as true, and empty sequences count as false. What the example tests is a plain comparison. The familiar comparison operators are spelled the same way they are within C: `<` checks for a smaller value, `>` checks for a larger one, `==` checks for equality, `<=` permits values up to and including, `>=` permits values from a bound upward, and `!=` checks for inequality.

- The loop's *body* sits *indented*: indentation is the mechanism Python uses for grouping statements together. While at the interactive prompt, you must enter a tab or some spaces for every indented line. Out in the real world you will compose more elaborate Python input inside a text editor; every respectable text editor sports an auto-indent capability. Entering a compound statement interactively means you must trail it with a blank line to signal that it is done (the parser has no way to tell which line will be your last). Note too that each line belonging to one basic block has to share the same level of indentation.

- The [`print()`](https://docs.python.org/3.14/library/functions.html#print) function emits the value of whichever argument(s) you pass it. It is not the same as merely writing out the expression you want shown (the way the earlier calculator examples did) — it behaves differently around multiple arguments, floating-point quantities, and strings. Strings get printed minus their quotes, and a space goes in between items, which lets you lay things out neatly, like so:

```python
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536

```

Supplying the keyword argument *end* lets you skip the newline that normally trails the output, or cap the output off with a string of your choosing:

```python
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

```

Footnotes

[Subject index](INDEX.md) · [Previous source section](list-aliasing-shallow-copies-slice-assignment-and-nesting.md)
