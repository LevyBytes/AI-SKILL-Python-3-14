# re — Regular Expression Syntax — Contract: `re.I` (ignore case)

- `re.I` (ignore case)

- `re.L` (locale dependent)

- `re.M` (multi-line)

- `re.S` (dot matches all)

- `re.U` (Unicode matching)

- `re.X` (verbose)

(Module Contents describes the flags.)

As inline flags the letters `'a'`, `'L'` and `'u'` exclude one another, so none can be combined nor placed after `'-'`. Rather, whenever one of them shows up in an inline group, it overrides the matching mode of the surrounding group. Within Unicode patterns `(?a:...)` flips to ASCII-only matching, while `(?u:...)` flips to Unicode matching (default). Within bytes patterns `(?L:...)` flips to locale dependent matching, while `(?a:...)` flips to ASCII-only matching (default). This override applies solely inside the narrow inline group, and the original matching mode resumes beyond the group.

Added in version 3.6.

Changed in version 3.7: a group may now also carry the letters `'a'`, `'L'` and `'u'`.

`(?>...)`

Tries to match `...` as though it were a standalone regular expression, and on success carries on matching the rest of the pattern after it. Should the following pattern fail to match, the stack can only rewind to a spot *before* the `(?>...)`, because on exit the expression — termed an *atomic group* — has discarded every stack point inside itself. Thus `(?>.*).` could never match anything, since `.*` would first take every character it can, and then, with nothing remaining to match, the closing `.` would fail to match. Because no stack points are kept inside the Atomic Group, and none exists before it either, the whole expression therefore fails to match.

Added in version 3.11.

`(?P<name>...)`

Akin to ordinary parentheses, except the substring the group matched is reachable through the symbolic group name *name*. A group name has to be a valid Python identifier, and within [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) patterns it may hold only bytes in the ASCII range. Within one regular expression each group name is allowed to be defined just once. A symbolic group also counts as a numbered group, exactly as though it had no name.

There are three contexts in which named groups may be referenced. Suppose the pattern is `(?P<quote>['"]).*?(?P=quote)` (that is, it matches a string quoted with either single or double quotes):

| Context of reference to group "quote" | Ways to reference it |
| --- | --- |
| in the same pattern itself | - `(?P=quote)` (as shown) - `\1` |
| when processing match object *m* | - `m.group('quote')` - `m.end('quote')` (etc.) |
| in a string passed to the *repl* argument of `re.sub()` | - `\g<quote>` - `\g<1>` - `\1` |

Changed in version 3.12: within [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) patterns, a group *name* may hold nothing but bytes drawn from the ASCII range (`b'\x00'`-`b'\x7f'`).

`(?P=name)`

A backreference pointing to a named group; it matches whatever text the earlier group called *name* matched.

`(?#...)`

A comment; whatever sits inside the parentheses is just ignored.

`(?=...)`

Matches when `...` matches next, though it consumes none of the string. This goes by the name *lookahead assertion*. For example, `Isaac (?=Asimov)` matches `'Isaac '` only where it's followed by `'Asimov'`.

`(?!...)`

Matches when `...` does not match next. This is a *negative lookahead assertion*. For example, `Isaac (?!Asimov)` matches `'Isaac '` only where it's *not* followed by `'Asimov'`.

`(?<=...)`

Matches when the current position in the string has a match for `...` directly before it that ends at the current position. This goes by the name *positive lookbehind assertion*. `(?<=abc)def` finds a match in `'abcdef'`, because the lookbehind backs up 3 characters and tests whether the inner pattern matches. That contained pattern is required to match only strings of some fixed length, so `abc` or `a|b` are permitted while `a*` and `a{3,4}` are not. Note that a pattern opening with a positive lookbehind assertion won't match at the start of the string under search; you'll most often want the `search()` function instead of the `match()` function:

```python
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'

```

Here is an example that hunts for a word coming after a hyphen:

[Subject index](INDEX.md) · [Previous](re-a-to-re-x.md) · [Continue](regex-lookbehind-example.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Regular Expression Syntax](regular-expression-syntax-overview.md)
