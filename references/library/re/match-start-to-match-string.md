# re: `Match.start()`, `Match.end()`, `Match.span()`, `Match.pos`, `Match.endpos`, `Match.lastindex`, `Match.lastgroup`, `Match.re`, `Match.string`

Match.start([*group*])

 Match.end([*group*])

Hand back the starting and ending positions of the substring that *group* matched; *group* falls back to zero, which stands for the entire matched substring. When *group* is present yet played no part in the match, the result is `-1`. Given a match object *m* together with a group *g* that did take part, the substring captured by group *g* (the same as `m.group(g)`) works out to

```python
m.string[m.start(g):m.end(g)]

```

Bear in mind that `m.start(group)` comes out equal to `m.end(group)` whenever *group* matched an empty string. By way of illustration, following `m = re.search('b(c?)', 'cba')`, `m.start(0)` is 1, `m.end(0)` is 2, both `m.start(1)` and `m.end(1)` are 2, and `m.start(2)` throws an [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception.

Here is a snippet that strips *remove_this* out of email addresses:

```python
>>> email = "tony@tiremove_thisger.net"
>>> m = re.search("remove_this", email)
>>> email[:m.start()] + email[m.end():]
'tony@tiger.net'

```

 Match.span([*group*])

For a match *m*, give back the 2-tuple `(m.start(group), m.end(group))`. Keep in mind that when *group* took no part in the match, this comes out as `(-1, -1)`. The *group* argument falls back to zero, the whole match.

 Match.pos

Holds the *pos* value handed to a regex object's `search()` or `match()` method. It marks the position within the string where the RE engine began its search for a match.

 Match.endpos

Holds the *endpos* value handed to a regex object's `search()` or `match()` method. It marks the position within the string past which the RE engine refuses to advance.

 Match.lastindex

The numeric index of whichever capturing group matched last, or `None` when nothing matched. To take a case, run against the string `'ab'`, the expressions `(a)b`, `((a)(b))`, and `((ab))` each give `lastindex == 1`, whereas `(a)(b)` gives `lastindex == 2` on that same string.

 Match.lastgroup

The name attached to whichever capturing group matched last, or `None` either when that group carried no name or when nothing matched.

 Match.re

The regular expression object whose call to `match()` or `search()` gave rise to this match instance.

 Match.string

The string passed to `match()` or `search()`.

Changed in version 3.7: Gained support for [`copy.copy()`](https://docs.python.org/3.14/library/copy.html#copy.copy) and [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy). A Match object is treated as atomic.

[Subject index](INDEX.md) · [Previous](match-getitem-to-match-groupdict.md) · [Continue](checking-for-a-pair.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: re.Match](re-match-class.md) · [Owning module, declaration or section: Match Objects](re-match-class.md)
