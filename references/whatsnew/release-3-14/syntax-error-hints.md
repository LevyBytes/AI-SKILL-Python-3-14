# Python 3.14 changes: Syntax error hints

> (Contributed by Sam Gross, Matt Page, Neil Schemenauer, Thomas Wouters, Donghee Na, Kirill Podoprigora, Ken Jin, Itamar Oren, Brett Simmers, Dino Viehland, Nathan Goldbaum, Ralf Gommers, Lysandros Nikolaou, Kumar Aditya, Edgar Margffoy, and many others. Some of these contributors are employed by Meta, which has continued to provide significant engineering resources to support this project.)

### Improved error messages

- Spotting typos in Python keywords now prompts the interpreter to offer helpful hints. Whenever it meets a token bearing a strong resemblance to a keyword, the recommended keyword appears within the error text. The result helps coders catch and repair everyday typing slips fast. Here's an example:

```pycon
>>> whille True:
...     pass
Traceback (most recent call last):
  File "<stdin>", line 1
    whille True:
    ^^^^^^
SyntaxError: invalid syntax. Did you mean 'while'?

```

The feature targets the most frequent situations, so certain misspelling variants can still surface as ordinary syntax errors. (Contributed by Pablo Galindo in [gh-132449](https://github.com/python/cpython/issues/132449).)

- An [`elif`](https://docs.python.org/3.14/reference/compound_stmts.html#elif) clause placed after an [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) block now yields a dedicated, tailored error message. (Contributed by Steele Farnsworth in [gh-129902](https://github.com/python/cpython/issues/129902).)

```pycon
>>> if who == "me":
...     print("It's me!")
... else:
...     print("It's not me!")
... elif who is None:
...     print("Who is it?")
File "<stdin>", line 5
  elif who is None:
  ^^^^
SyntaxError: 'elif' block follows an 'else' block

```

- Should a statement appear after [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) in a [Conditional expressions](https://docs.python.org/3.14/reference/expressions.html#if-expr), or should any of [`pass`](https://docs.python.org/3.14/reference/simple_stmts.html#pass), [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break), or [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) precede the [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if), the error text pinpoints the spot demanding an [`expression`](https://docs.python.org/3.14/reference/expressions.html#grammar-token-python-grammar-expression). (Contributed by Sergey Miryanov in [gh-129515](https://github.com/python/cpython/issues/129515).)

```pycon
>>> x = 1 if True else pass
Traceback (most recent call last):
  File "<string>", line 1
    x = 1 if True else pass
                       ^^^^
SyntaxError: expected expression after 'else', but statement is given

>>> x = continue if True else break
Traceback (most recent call last):
  File "<string>", line 1
    x = continue if True else break
        ^^^^^^^^
SyntaxError: expected expression before 'if', but statement is given

```

- Whenever an improperly terminated string is found, the message hints that the text might be meant as part of the string. (Contributed by Pablo Galindo in [gh-88535](https://github.com/python/cpython/issues/88535).)

```pycon
>>> "The interesting object "The important object" is very important"
Traceback (most recent call last):
SyntaxError: invalid syntax. Is this intended to be part of the string?

```

- For strings carrying clashing prefixes, the error now spells out exactly which prefixes don't go together. (Contributed by Nikita Sobolev in [gh-133197](https://github.com/python/cpython/issues/133197).)

```pycon
>>> ub'abc'
  File "<python-input-0>", line 1
    ub'abc'
    ^^
SyntaxError: 'u' and 'b' prefixes are incompatible

```

[Subject index](INDEX.md) · [Previous source section](free-threaded-mode-improvements.md) · [Next source section](invalid-as-target-errors.md) · [Release/subject declaration](summary-release-highlights.md)
