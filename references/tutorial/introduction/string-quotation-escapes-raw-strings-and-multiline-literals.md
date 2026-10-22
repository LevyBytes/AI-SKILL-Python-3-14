# String quotation, escapes, raw strings and multiline literals

### 3.1.2. Text

Alongside numbers, Python is able to work with text — captured by the type [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and known as "strings". That covers characters such as "`!`", words such as "`rabbit`", names such as "`Paris`", full sentences such as "`Got your back.`", and so on, even "`Yay! :)`". You may wrap them in single quotes (`'...'`) or in double quotes (`"..."`) and get the identical outcome [2].

```pycon
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
>>> '1975'  # digits and numerals enclosed in quotes are also strings
'1975'

```

Placing a quote inside a quote calls for an "escape", accomplished by putting a `\` ahead of it. As an alternative, switch to the opposite style of quotation mark:

```python
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'

```

Within the Python shell, how a string is defined and how it is shown can diverge. The [`print()`](https://docs.python.org/3.14/library/functions.html#print) function yields friendlier output: it drops the surrounding quotes and renders escaped and special characters:

```python
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s)  # with print(), special characters are interpreted, so \n produces new line
First line.
Second line.

```

> When you would rather not have a `\` to be interpreted as special characters, you can use *raw strings* by adding an `r` at the very start of the literal.

```python
>>> print('C:\this\name')  # here \t means tab, \n means newline
C:      his
ame
>>> print(r'C:\this\name')  # note the r before the quote
C:\this\name

```

One delicate point applies to raw strings: such a string cannot finish with an odd count of `\` characters; consult [the FAQ entry](https://docs.python.org/3.14/faq/programming.html#faq-programming-raw-string-backslash) for further detail and ways around it.

A string literal is allowed to stretch across several lines. Triple-quoting is one approach: `"""..."""` or `'''...'''`. The newline characters become part of the string on their own, though you can suppress that by tacking a `\` onto the line's end. The sample below keeps the leading newline out:

```python
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>>

```

[Subject index](INDEX.md) · [Previous source section](numbers.md) · [Following source section](string-repetition-and-literal-versus-variable-concatenation.md) · [Related tutorial example and explanation](string-repetition-and-literal-versus-variable-concatenation.md) · [Related tutorial example and explanation](string-indexing-slicing-defaults-and-slice-boundaries.md) · [Related tutorial example and explanation](string-bounds-immutability-length-and-further-operations.md)
