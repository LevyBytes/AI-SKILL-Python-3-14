# re - Checking for a Pair

### Regular Expression Examples

### Checking for a Pair

For this walkthrough, the helper routine below renders match objects in a slightly tidier form:

```python
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

```

Imagine coding a poker program in which each player's hand is held as a 5-character string, every character standing for one card: “a” marks an ace, “k” a king, “q” a queen, “j” a jack, “t” a 10, and the digits “2” through “9” the cards of those values.

Checking whether some string forms a legal hand could be done like so:

```python
>>> valid = re.compile(r"^[a2-9tjqk]{5}$")
>>> displaymatch(valid.match("akt5q"))  # Valid.
"<Match: 'akt5q', groups=()>"
>>> displaymatch(valid.match("akt5e"))  # Invalid.
>>> displaymatch(valid.match("akt"))    # Invalid.
>>> displaymatch(valid.match("727ak"))  # Valid.
"<Match: '727ak', groups=()>"

```

The final hand there, `"727ak"`, held a pair — that is, two cards sharing a value. Spotting that with a regular expression is a job for backreferences, written this way:

```python
>>> pair = re.compile(r".*(.).*\1")
>>> displaymatch(pair.match("717ak"))     # Pair of 7s.
"<Match: '717', groups=('7',)>"
>>> displaymatch(pair.match("718ak"))     # No pairs.
>>> displaymatch(pair.match("354aa"))     # Pair of aces.
"<Match: '354aa', groups=('a',)>"

```

To learn which card forms the pair, you can call the match object's `group()` method like this:

```python
>>> pair = re.compile(r".*(.).*\1")
>>> pair.match("717ak").group(1)
'7'

# Error because re.match() returns None, which doesn't have a group() method:
>>> pair.match("718ak").group(1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    re.match(r".*(.).*\1", "718ak").group(1)
AttributeError: 'NoneType' object has no attribute 'group'

>>> pair.match("354aa").group(1)
'a'

```

[Subject index](INDEX.md) · [Continue](simulating-scanf.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
