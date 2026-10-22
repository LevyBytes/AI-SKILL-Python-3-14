# 2.5. String and Bytes literals

### 2.5. String and Bytes literals

Text wrapped in single quotes (`'`) or double quotes (`"`) forms a string literal. As an example:

```python
"spam"
'eggs'

```

Whichever quote opens the literal also closes it, which is why a string literal may include only the other quote (escape sequences aside, see below). As an example:

```python
'Say "Hello", please.'
"Don't do that!"

```

Beyond that restriction, picking one quote character over the other (`'` or `"`) has no bearing on how the literal gets parsed.

Within a string literal, a leading backslash (the `) character introduces an *escape sequence*, which has special meaning depending on the character after the backslash. For example,` `\"` form) marks a double quote and keeps the string open instead of ending it:

```pycon
>>> print("Say \"Hello\" to everyone!")
Say "Hello" to everyone!

```

For the complete list of such sequences plus further detail, see escape sequences below.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Previous source section](literals.md) · [Following source section](triple-quoted-strings.md)
