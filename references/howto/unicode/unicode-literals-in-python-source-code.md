# Unicode Literals in Python Source Code

### Unicode Literals in Python Source Code

Within Python source code, particular Unicode code points can be expressed through the `\u` escape sequence, trailed by four hex digits that give the code point. The `\U` escape sequence works similarly, except it wants eight hex digits rather than four:

```python
>>> s = "a\xac\u1234\u20ac\U00008000"
... #     ^^^^ two-digit hex escape
... #         ^^^^^^ four-digit Unicode escape
... #                     ^^^^^^^^^^ eight-digit Unicode escape
>>> [ord(c) for c in s]
[97, 172, 4660, 8364, 32768]

```

Relying on escape sequences for code points above 127 works fine in small amounts, yet it turns into a nuisance once you are dealing with many accented characters, as you would in a program carrying messages in French or another accent-using language. Strings can also be assembled with the [`chr()`](https://docs.python.org/3.14/library/functions.html#chr) built-in function, but doing so is even more tedious.

In an ideal world, you would be able to compose literals in the natural encoding of your language. You could then work on Python source code in your preferred editor, which would render the accented characters naturally, and the proper characters would be used at runtime.

By default Python lets you write source code in UTF-8, but practically any encoding is available so long as you declare which one is in use. You do this by adding a special comment as the first or second line of the source file:

```python
#!/usr/bin/env python
# -*- coding: latin-1 -*-

u = 'abcdé'
print(ord(u[-1]))

```

The syntax draws on Emacs’s notation for declaring variables local to a file. Many different variables are supported by Emacs, whereas Python recognizes only ‘coding’. The `-*-` symbols tell Emacs the comment is special; they mean nothing to Python but follow a convention. Python scans for `coding: name` or `coding=name` within the comment.

Leaving out such a comment means the default encoding, UTF-8, is used as already noted. Consult [**PEP 263**](https://peps.python.org/pep-0263/) as well for further details.

[Subject index](INDEX.md) · [Previous source context](converting-to-bytes.md) · [Following source context](unicode-properties.md)
