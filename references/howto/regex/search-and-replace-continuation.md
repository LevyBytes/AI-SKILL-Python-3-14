# Search and replace continuation

```python
>>> p = re.compile('(blue|white|red)')
>>> p.subn('colour', 'blue socks and red shoes')
('colour socks and colour shoes', 2)
>>> p.subn('colour', 'no colours at all')
('no colours at all', 0)

```

A substitution happens for an empty match only if it doesn't butt up against the empty match that came before it.

```python
>>> p = re.compile('x*')
>>> p.sub('-', 'abxd')
'-a-b--d-'

```

Should *replacement* be a string, whatever backslash escapes it holds get handled. Concretely, `\n` becomes one newline character, `\r` turns into a carriage return, and the like. Escapes it doesn't recognize, `\&` among them, are passed through untouched. A backreference like `\6` is swapped for the substring that the matching group in the RE captured. This is what lets you fold pieces of the original text into the replacement string you end up with.

In the following example, the word `section` trailed by a string wrapped in `{`, `}` is matched, and `section` gets turned into `subsection`:

```python
>>> p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
>>> p.sub(r'subsection{\1}','section{First} section{second}')
'subsection{First} subsection{second}'

```

A separate notation exists for pointing at named groups, the ones set up through the `(?P<name>...)` syntax. Here `\g<name>` pulls in the substring captured by the group called `name`, while `\g<number>` draws on the matching group number. So `\g<2>` amounts to the same thing as `\2`, yet it stays unambiguous within a replacement string like `\g<2>0`. (Otherwise `\20` would read as pointing to group 20 rather than group 2 trailed by the literal character `'0'`.) Each of the substitutions below produces the identical result, though they run through all three forms of the replacement string.

```python
>>> p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
>>> p.sub(r'subsection{\1}','section{First}')
'subsection{First}'
>>> p.sub(r'subsection{\g<1>}','section{First}')
'subsection{First}'
>>> p.sub(r'subsection{\g<name>}','section{First}')
'subsection{First}'

```

A function may serve as *replacement* too, handing you still greater command. When *replacement* is a function, it fires once for each non-overlapping appearance of *pattern*. Every invocation receives a [match object](https://docs.python.org/3.14/library/re.html#match-objects) argument standing for the match, and from that the function can work out the replacement string it wants and return it.

Below, the replacement function converts decimal numbers into hexadecimal:

```python
>>> def hexrepl(match):
...     "Return the hex string for a decimal number"
...     value = int(match.group())
...     return hex(value)
...
>>> p = re.compile(r'\d+')
>>> p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
'Call 0xffd2 for printing, 0xc000 for user code.'

```

With the module-level [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) function, the pattern goes in as the first argument. You may hand the pattern over either as an object or as a string; and if regular expression flags need stating, you have to either feed a pattern object as that first parameter or fold embedded modifiers into the pattern string — for instance, `sub("(?i)b+", "x", "bbbb BBBB")` yields `'x x'`.

[Subject index](INDEX.md) · [Previous source owning section](search-and-replace.md) · [Following source context](common-problems.md)
