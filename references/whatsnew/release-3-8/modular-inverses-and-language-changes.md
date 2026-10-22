# What’s New In Python 3.8 / Other Language Changes

- With integers, the three-argument flavor of the [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) function will now tolerate a negative exponent whenever the base shares no common factor with the modulus. In that situation it works out a modular inverse of the base when the exponent equals `-1`, and an appropriate power of that inverse for the remaining negative exponents. As an example, to work out the [modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of 38 modulo 137, you write:

```python
>>> pow(38, -1, 137)
119
>>> 119 * 38 % 137
1

```

These modular inverses show up while solving [linear Diophantine equations](https://en.wikipedia.org/wiki/Diophantine_equation). Suppose you want integer solutions to `4258𝑥 + 147𝑦 = 369`; you first restate it as `4258𝑥 ≡ 369 (mod 147)` and then solve:

```python
>>> x = 369 * pow(4258, -1, 147) % 147
>>> y = (4258 * x - 369) // -147
>>> 4258 * x + 147 * y
369

```

(Mark Dickinson contributed this in [bpo-36027](https://bugs.python.org/issue?@action=redirect&bpo=36027).)

- Dict comprehensions now line up with dict literals, so the key gets evaluated first and the value afterward:

```python
>>> # Dict comprehension
>>> cast = {input('role? '): input('actor? ') for i in range(2)}
role? King Arthur
actor? Chapman
role? Black Knight
actor? Cleese

>>> # Dict literal
>>> cast = {input('role? '): input('actor? ')}
role? Sir Robin
actor? Eric Idle

```

Pinning down the evaluation order pairs nicely with assignment expressions, since a variable bound inside the key expression becomes usable within the value expression:

```python
>>> names = ['Martin von Löwis', 'Łukasz Langa', 'Walter Dörwald']
>>> {(n := normalize('NFC', name)).casefold() : n for name in names}
{'martin von löwis': 'Martin von Löwis',
 'łukasz langa': 'Łukasz Langa',
 'walter dörwald': 'Walter Dörwald'}

```

(Jörn Heissler contributed this in [bpo-35224](https://bugs.python.org/issue?@action=redirect&bpo=35224).)

-

[Subject index](INDEX.md) · [Previous source section](other-language-changes.md) · [Release/subject declaration](assignment-expressions.md) · [Release/subject declaration](other-language-changes.md) · [Following release/subject continuation](object-reduction-and-pickle-protocol.md)
