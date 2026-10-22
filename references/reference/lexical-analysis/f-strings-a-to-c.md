# lexical analysis: F-string syntax and replacement fields

### 2.5.7. f-strings

Added in version 3.6.

Changed in version 3.7: Both [`await`](https://docs.python.org/3.14/reference/expressions.html#await) and [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) became usable inside the expressions of an f-string.

Changed in version 3.8: Added the debug specifier (`=`)

Changed in version 3.12: A great deal of the limits placed on f-string expressions were lifted. In particular, backslashes, comments, and nested strings are allowed from then on.

A *formatted string literal*, or *f-string*, is a string literal carrying the ‘`f`’ or ‘`F`’ prefix. Setting them apart from other string literals, f-strings hold no constant value. They are able to hold *replacement fields* bounded by curly braces `{}`. Inside replacement fields sit expressions that get evaluated when the program runs. To illustrate:

```python
>>> who = 'nobody'
>>> nationality = 'Spanish'
>>> f'{who.title()} expects the {nationality} Inquisition!'
'Nobody expects the Spanish Inquisition!'

```

Wherever doubled curly braces (`{{` or `}}`) sit beyond replacement fields, each is swapped for the matching single curly brace:

```python
>>> print(f'{{...}}')
{...}

```

Beyond replacement fields, the remaining characters behave as they do in plain string literals. So escape sequences get decoded (other than when a literal also bears the raw marking), and triple-quoted f-strings allow newlines:

```python
>>> name = 'Galahad'
>>> favorite_color = 'blue'
>>> print(f'{name}:\t{favorite_color}')
Galahad:       blue
>>> print(rf"C:\Users\{name}")
C:\Users\Galahad
>>> print(f'''Three shall be the number of the counting
... and the number of the counting shall be three.''')
Three shall be the number of the counting
and the number of the counting shall be three.

```

Inside formatted string literals, expressions behave just like ordinary Python expressions. Each one is evaluated within the context surrounding the formatted string literal, proceeding from left to right. Leaving an expression empty is disallowed, and both [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) and assignment expressions `:=` have to be wrapped in explicit parentheses:

```python
>>> f'{(half := 1/2)}, {half * 42}'
'0.5, 21.0'

```

You are allowed to reuse the outer f-string's quoting style inside a replacement field:

```python
>>> a = dict(x=2)
>>> f"abc {a["x"]} def"
'abc 2 def'

```

Replacement fields may also hold backslashes, and these get evaluated exactly as they would anywhere else:

```python
>>> a = ["a", "b", "c"]
>>> print(f"List a contains:\n{"\n".join(a)}")
List a contains:
a
b
c

```

Nesting one f-string inside another is achievable:

```python
>>> name = 'world'
>>> f'Repeated:{f' hello {name}' * 3}'
'Repeated: hello world hello world hello world'

```

For portability, Python programs ought to keep nesting at 5 levels or fewer.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](string-and-bytes-literals.md) · [Previous source section](raw-string-literals.md) · [Following source section](fstring-nesting-implementation-limit.md)
