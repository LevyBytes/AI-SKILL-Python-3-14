# Using re.VERBOSE

### Using re.VERBOSE

At this point it's likely clear to you that regular expressions form an extremely terse notation, though one that's hardly easy on the eyes. Even moderately involved REs can swell into long strings of backslashes, parentheses, and metacharacters, leaving them hard to parse and grasp.

With REs like those, handing the [`re.VERBOSE`](https://docs.python.org/3.14/library/re.html#re.VERBOSE) flag to the compile step can pay off, since it lets you lay the regular expression out far more legibly.

Several things follow from the `re.VERBOSE` flag. Any whitespace in the regular expression that *isn't* tucked inside a character class gets disregarded. So an expression like `dog | cat` comes out equivalent to the harder-to-read `dog|cat`, while `[a b]` keeps matching the characters `'a'`, `'b'`, or a space. On top of that, you may drop comments into a RE; a comment runs from a `#` character up to the following newline. Paired with triple-quoted strings, this lets REs be laid out far more tidily:

```python
pat = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)

```

That reads a great deal more easily than:

```python
pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")

```

[Subject index](INDEX.md) · [Previous source context](greedy-versus-non-greedy.md) · [Following source context](feedback.md)
