# What’s New In Python 3.12 / PEP 701: Syntactic formalization of f-strings

### PEP 701: Syntactic formalization of f-strings

A number of curbs on how [f-strings](https://docs.python.org/3.14/glossary.html#term-f-string) may be used are removed by [**PEP 701**](https://peps.python.org/pep-0701/). The expression parts within f-strings may now be any well-formed Python expression — that includes strings that reuse the very quote of the surrounding f-string, expressions across several lines, comments, backslashes, and unicode escape sequences. We’ll go through each one closely:

- Quote reuse: under Python 3.11, repeating the very quotes of the surrounding f-string triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), which pushes the user toward whatever other quotes remain (say double quotes, or triple quotes, when the f-string already employs single quotes). With Python 3.12, constructs such as the following become possible:

```python
>>> songs = ['Take me back to Eden', 'Alkaline', 'Ascensionism']
>>> f"This is the playlist: {", ".join(songs)}"
'This is the playlist: Take me back to Eden, Alkaline, Ascensionism'

```

Be aware that prior to this change no formal cap existed on f-string nesting, yet because quotes could not be reused inside an f-string’s expression part, nesting f-strings without bound was not achievable. Indeed, the deepest nesting one could express was this:

```python
>>> f"""{f'''{f'{f"{1+1}"}'}'''}"""
'2'

```

Now that an f-string’s expression parts accept any well-formed Python expression, nesting f-strings to any depth has become feasible:

```python
>>> f"{f"{f"{f"{f"{f"{1+1}"}"}"}"}"}"
'2'

```

- Multi-line expressions and comments: with Python 3.11, an f-string expression had to sit on one line, even where that expression would ordinarily stretch over several lines (such as a literal list laid out across multiple lines), which hurt readability. Python 3.12 lets you write f-strings that run across several lines and tuck in inline comments:

```python
>>> f"This is the playlist: {", ".join([
...     'Take me back to Eden',  # My, my, those eyes like fire
...     'Alkaline',              # Not acid nor alkaline
...     'Ascensionism'           # Take to the broken skies at last
... ])}"
'This is the playlist: Take me back to Eden, Alkaline, Ascensionism'

```

- > Backslashes and unicode characters: before Python 3.12 f-string expressions couldn’t contain any `\` character. This also affected unicode [escape sequences](https://docs.python.org/3.14/reference/lexical_analysis.html#escape-sequences) (such as `\N{snowman}`) as these contain the `\N` part that previously could not be part of expression components of f-strings. Now, you can define expressions like this:

```python
>>> print(f"This is the playlist: {"\n".join(songs)}")
This is the playlist: Take me back to Eden
Alkaline
Ascensionism
>>> print(f"This is the playlist: {"\N{BLACK HEART SUIT}".join(songs)}")
This is the playlist: Take me back to Eden♥Alkaline♥Ascensionism

```

See [**PEP 701**](https://peps.python.org/pep-0701/) for more details.

A welcome by-product of the way this was built (f-strings are parsed using [**the PEG parser**](https://peps.python.org/pep-0617/)) is that f-string error messages now pinpoint the exact spot of the problem. To take one case, under Python 3.11 the f-string below raises a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError):

```python
>>> my_string = f"{x z y}" + f"{1 + 1}"
  File "<stdin>", line 1
    (x z y)
     ^^^
SyntaxError: f-string: invalid syntax. Perhaps you forgot a comma?

```

but the message neither marks where in the line the error sits nor avoids wrapping the expression in artificial parentheses. Under Python 3.12, since the PEG parser handles f-strings, the messages can be sharper and display the whole line:

```python
>>> my_string = f"{x z y}" + f"{1 + 1}"
  File "<stdin>", line 1
    my_string = f"{x z y}" + f"{1 + 1}"
                   ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

```

[Subject index](INDEX.md) · [Previous source section](pep-695-type-parameter-syntax.md) · [Next source section](pep-684-a-per-interpreter-gil.md) · [Release/subject declaration](summary-release-highlights.md)
