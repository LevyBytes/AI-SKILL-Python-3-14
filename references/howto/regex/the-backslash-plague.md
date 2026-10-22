# The backslash plague

### The backslash plague

Recall from earlier that regular expressions lean on the backslash character (`'\'`) to mark special forms or to let special characters be used without triggering their special meaning. That collides with how Python already uses the very same character inside string literals.

Suppose you want a RE that matches the string `\section`, the sort of thing you might run across in a LaTeX file. Working out what to put in your program code starts from the target string you mean to match. After that, every backslash and other metacharacter has to be escaped by sticking a backslash in front of it, which gives the string `\\section`. Then the string handed over to [`re.compile()`](https://docs.python.org/3.14/library/re.html#re.compile) has to be `\\section`. But rendering that as a Python string literal demands escaping both backslashes *yet again*.

| Characters | Stage |
| --- | --- |
| `\section` | Text string to be matched |
| `\\section` | Escaped backslash for `re.compile()` |
| `"\\\\section"` | Escaped backslashes for a string literal |

Put briefly, matching one literal backslash forces you to write `'\\\\'` for the RE string, since the regular expression itself must be `\\`, and each backslash has to appear as `\\` within an ordinary Python string literal. For REs that lean on backslashes again and again, this piles up backslash upon backslash and renders the resulting strings hard to read.

The remedy is Python’s raw string notation for regular expressions; inside a string literal carrying the `'r'` prefix, backslashes receive no special treatment, so `r"\n"` is a two-character string holding `'\'` and `'n'`, whereas `"\n"` is a single-character string holding a newline. People often write regular expressions in Python code using this raw string notation.

On top of that, special escape sequences that are legal in regular expressions but illegal as Python string literals now trigger a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) and are slated to turn into a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) down the line, meaning those sequences are invalid unless you use raw string notation or escape the backslashes.

| Regular String | Raw string |
| --- | --- |
| `"ab*"` | `r"ab*"` |
| `"\\\\section"` | `r"\\section"` |
| `"\\w+\\s+\\1"` | `r"\w+\s+\1"` |

[Subject index](INDEX.md) · [Previous source context](compiling-regular-expressions.md) · [Following source context](compile-a-pattern-match-strings-and-inspect-match-objects.md)
