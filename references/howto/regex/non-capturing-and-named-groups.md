# Non-capturing and named groups

### Non-capturing and named groups

Sophisticated REs can employ a great many groups, partly to capture interesting substrings and partly to give the RE itself shape and structure. Across intricate REs it grows hard to stay on top of which number goes with which group. Two features exist to ease this trouble. Because both lean on a shared syntax for regular expression extensions, we'll examine that syntax to start with.

Perl 5 enjoys a strong name for the potent extras it layers over standard regular expressions. To bring in those additions, the Perl developers had no way to select brand-new single-keystroke metacharacters or brand-new special sequences led off by a `without making Perl’s regular expressions confusingly different from standard REs. If they chose` `&` `as a new metacharacter, for example, old expressions would be assuming that` `&` `was a regular character and wouldn’t have escaped it by writing` `\&` `or` `[&]`.

What the Perl developers settled on was adopting `(?...)` for the extension syntax. Placing `?` right after a parenthesis used to be a syntax error, because the `?` would have had nothing to repeat, and so this raised no compatibility issues. The characters that follow the `?` signal which extension is in play, so `(?=foo)` is one construct (a positive lookahead assertion) while `(?:foo)` is a different one (a non-capturing group wrapping the subexpression `foo`).

Python carries several of Perl's extensions and tacks an extension syntax onto Perl's own extension syntax. Whenever the first character following the question mark is a `P`, that tells you the extension is one peculiar to Python.

With the general extension syntax now behind us, we can come back to the features that ease the handling of groups within intricate REs.

There are times when you want a group to mark off a chunk of a regular expression yet have no interest in fetching back that group's contents. You can spell this out by reaching for a non-capturing group: `(?:...)`, where the `...` may stand in for any other regular expression.

```python
>>> m = re.match("([abc])+", "abc")
>>> m.groups()
('c',)
>>> m = re.match("(?:[abc])+", "abc")
>>> m.groups()
()

```

Aside from being unable to fetch back whatever the group matched, a non-capturing group acts precisely like a capturing one; you may stuff anything in it, repeat it via a repetition metacharacter like `*`, and embed it inside other groups (capturing or not). `(?:...)` proves especially handy while editing an existing pattern, because you can drop in new groups without disturbing the numbering of all the rest. Worth noting is that searching shows no performance gap between capturing and non-capturing groups; neither shape outruns the other.

A weightier feature is named groups: in place of pointing to them by number, groups can be addressed by a name.

A named group's syntax is among the Python-specific extensions: `(?P<name>...)`. *name*, naturally, is the group's name. A named group acts just like a capturing group and on top of that ties a name to the group. Every [match object](https://docs.python.org/3.14/library/re.html#match-objects) method that handles capturing groups takes either integers pointing to a group by number or strings holding the wanted group's name. Because named groups still receive numbers as well, you have two routes to fetch a group's information:

```python
>>> p = re.compile(r'(?P<word>\b\w+\b)')
>>> m = p.search( '(((( Lots of punctuation )))' )
>>> m.group('word')
'Lots'
>>> m.group(1)
'Lots'

```

On top of that, you can pull back named groups as a dictionary by means of [`groupdict()`](https://docs.python.org/3.14/library/re.html#re.Match.groupdict):

```python
>>> m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')
>>> m.groupdict()
{'first': 'Jane', 'last': 'Doe'}

```

Named groups come in useful because they let you lean on names that stick in memory instead of forcing you to recall numbers. Below is a sample RE drawn from the [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) module:

```python
InternalDate = re.compile(r'INTERNALDATE "'
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
        r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        r'"')

```

Plainly it is far simpler to fetch `m.group('zonem')` than to keep in mind that group 9 is the one to fetch.

A backreference whose syntax is like `(...)\1` points at the group's number. Predictably there is also a form that relies on the group's name instead of its number. This is a further Python extension: `(?P=name)` says the contents of the group named *name* are to be matched once more at the present point. That regular expression for spotting doubled words, `\b(\w+)\s+\1\b`, may equally be written as `\b(?P<word>\w+)\s+(?P=word)\b`:

```python
>>> p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
>>> p.search('Paris in the the spring').group()
'the the'

```

[Subject index](INDEX.md) · [Previous source context](grouping.md) · [Following source context](lookahead-assertions.md)
