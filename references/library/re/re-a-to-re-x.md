# re — Regular Expression Syntax — Contract: A range of characters is given by naming two characters and putting a `'-'` between them, so `[a-z]` matches any lowercase ASCII letter, `[0-5][0-9]` matches every two-digit number from `00` through `59`, and `[0-9A-Fa-f]` matches any hexadecimal digit.

A range of characters is given by naming two characters and putting a `'-'` between them, so `[a-z]` matches any lowercase ASCII letter, `[0-5][0-9]` matches every two-digit number from `00` through `59`, and `[0-9A-Fa-f]` matches any hexadecimal digit. When `-` is escaped (for instance `[a\-z]`), or when it sits as the first or last character (for instance `[-a]` or `[a-]`), it matches a literal `'-'`.

- Inside a set, special characters other than backslash shed their special meaning. For instance, `[(+*)]` matches any of the literal characters `'('`, `'+'`, `'*'`, or `')'`.

- Backslash either escapes characters that hold special meaning within a set — `'-'`, `']'`, `'^'`, and `'\\'` itself — or marks a special sequence. Such a sequence may denote one character, like `\xa0` or `\n`, or one of the character classes covered further down, like `\w` or `\S`. Bear in mind that `\b` here denotes a single "backspace" character rather than a word boundary as it does outside a set, and numeric escapes such as `\1` always mean octal escapes, never group references. Special sequences that don't match a single character, such as `\A` and `\z`, are disallowed.

- You can match characters falling outside a range by *complementing* the set. When `'^'` is the set's first character, every character *not* in the set gets matched. For example, `[^5]` matches any character besides `'5'`, and `[^^]` matches any character besides `'^'`. The `^` carries no special meaning unless it leads the set.

- To match a literal `']'` within a set, put a backslash before it, or set it at the very start of the set. For example, `[()[\]{}]` and `[]()[{}]` both match a right bracket, plus a left bracket, braces, and parentheses.

- Down the line, support may arrive for nested sets and set operations along the lines of [Unicode Technical Standard #18](https://unicode.org/reports/tr18/). Because that would alter the syntax, a [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) is raised meanwhile in cases that are ambiguous, easing the transition. Covered by that are sets that open with a literal `'['` or that hold the literal character sequences `'--'`, `'&&'`, `'~~'`, and `'||'`. Escape them with a backslash to head off a warning.

Changed in version 3.7: a [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) now fires whenever a character set holds constructs whose meaning is set to shift in later releases.

`|`

`A|B`, in which *A* and *B* may be arbitrary REs, builds a regular expression matching either *A* or *B*. Any number of REs can be joined by the `'|'` like this. It works inside groups (covered below) just as well. While the target string is scanned, the REs split by `'|'` are attempted left to right. As soon as one alternative fully matches, that branch is taken. So once *A* matches, *B* goes untested thereafter, even where it might yield a longer overall match. Put differently, the `'|'` operator is never greedy. For a literal `'|'`, write `\|`, or wrap it within a character class, like `[|]`.

`(...)`

Matches whatever regular expression sits inside the parentheses, and marks where a group begins and ends; once a match has run, a group's contents are retrievable, and they can be matched again later in the string through the `\number` special sequence covered below. For the literals `'('` or `')'`, write `\(` or `\)`, or wrap them within a character class: `[(]`, `[)]`.

`(?...)`

This is an extension notation (outside this, a `'?'` after a `'('` has no meaning). Whatever the first character is after the `'?'` decides the construct's meaning and remaining syntax. As a rule, extensions don't form a new group; the sole exception is `(?P<name>...)`. The extensions presently supported follow.

`(?aiLmsux)`

(One or more letters drawn from the set `'a'`, `'i'`, `'L'`, `'m'`, `'s'`, `'u'`, `'x'`.) This group matches the empty string; the letters turn on the matching flags for the whole regular expression:

- `re.A` (ASCII-only matching)

- `re.I` (ignore case)

- `re.L` (locale dependent)

- `re.M` (multi-line)

- `re.S` (dot matches all)

- `re.U` (Unicode matching)

- `re.X` (verbose)

(Module Contents describes the flags.) This comes in handy when you'd like the flags built into the regular expression itself, rather than handing a *flag* argument to the `re.compile()` function. Put the flags at the very front of the expression string.

Changed in version 3.11: this construction is now permitted only where the expression begins.

`(?:...)`

A non-capturing form of regular parentheses. Matches whatever regular expression lies inside the parentheses, but the substring the group matched *cannot* be fetched once a match runs or referred to later in the pattern.

`(?aiLmsux-imsx:...)`

(Zero or more letters from the set `'a'`, `'i'`, `'L'`, `'m'`, `'s'`, `'u'`, `'x'`, with an optional `'-'` after them followed by one or more letters from `'i'`, `'m'`, `'s'`, `'x'`.) The letters turn the corresponding flags on or off for that part of the expression:

- `re.A` (ASCII-only matching)

[Subject index](INDEX.md) · [Previous](regular-expression-syntax-overview.md) · [Continue](re-i-to-re-x.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Regular Expression Syntax](regular-expression-syntax-overview.md)
