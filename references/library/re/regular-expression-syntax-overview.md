# re — Regular Expression Syntax — Section introduction and initial examples

### Regular Expression Syntax

What a regular expression (or RE) describes is a set of strings it matches; with this module's functions you can test whether some particular string matches a given regular expression (equivalently, whether a given regular expression matches a particular string — the same question either way).

Joining regular expressions end to end yields new ones; given that *A* and *B* are each regular expressions, *AB* is a regular expression too. As a rule, when one string *p* matches *A* and a second string *q* matches *B*, then *pq* matches AB. The exception is when *A* or *B* involve low precedence operations; boundary conditions between *A* and *B*; or include numbered group references. In this way, intricate expressions are readily assembled out of simpler primitive ones such as those covered here. To dig into the theory and implementation behind regular expressions, turn to the Friedl book [Frie09], or to nearly any compiler-construction textbook.

What follows is a short account of how regular expressions are formatted. For a fuller and more gradual treatment, see the [Regular expression HOWTO](https://docs.python.org/3.14/howto/regex.html#regex-howto).

Both special and ordinary characters may appear in regular expressions. The bulk of ordinary characters — `'A'`, `'a'`, or `'0'` among them — count as the most basic regular expressions, simply matching themselves. Since ordinary characters concatenate, `last` matches the string `'last'`. (Throughout the remainder of this section, RE's appear in `this special style`, generally unquoted, with target strings shown `'in single quotes'`.)

A handful of characters, such as `'|'` or `'('`, carry special meaning. Special characters either denote whole classes of ordinary characters, or change how the surrounding regular expressions are read.

You cannot directly nest the repetition operators or quantifiers (`*`, `+`, `?`, `{m,n}`, etc). Doing so would create ambiguity with the non-greedy modifier suffix `?` and with modifiers found in other implementations. Should you need to apply one repetition on top of another, wrap it in parentheses. As an illustration, `(?:a{6})*` matches any multiple of six `'a'` characters.

The special characters are:

`.`

(Dot.) Under the default mode it matches any character apart from a newline. When the `DOTALL` flag is set, it matches any character, newline included. `(?s:.)` matches any character no matter the flags.

`^`

(Caret.) Matches at the string's start, and under `MULTILINE` mode also right after every newline.

`$`

Matches at the string's end or just ahead of a terminal newline, and under `MULTILINE` mode also ahead of any newline. `foo` matches both "foo" and "foobar", whereas the regular expression `foo$` matches "foo" alone. More tellingly, a search for `foo.$` within `'foo1\nfoo2\n'` matches "foo2" in the ordinary case, but "foo1" when `MULTILINE` mode is active; a search for a lone `$` in `'foo\n'` turns up two (empty) matches: one immediately before the newline and one at the string's end.

`*`

Makes the resulting RE match 0 or more repetitions of the RE that precedes it, taking as many repetitions as it can. `ab*` matches "a", "ab", or "a" trailed by any quantity of `b` characters.

`+`

Makes the resulting RE match 1 or more repetitions of the RE preceding it. `ab+` matches "a" trailed by any nonzero number of `b` characters; it won't match a bare "a".

`?`

Makes the resulting RE match 0 or 1 repetitions of the RE that comes before. `ab?` matches either "a" or "ab".

`*?`, `+?`, `??`

Each of the `'*'`, `'+'`, and `'?'` quantifiers is *greedy*, consuming as much text as it can. At times that's unwanted; should the RE `<.*>` run against `'<a> b <c>'`, it grabs the whole string rather than only `'<a>'`. Placing `?` after the quantifier makes the match proceed in a *non-greedy* or *minimal* way, taking *few* characters as it can. The RE `<.*?>` then matches only `'<a>'`.

`*+`, `++`, `?+`

Just like the `'*'`, `'+'`, and `'?'` quantifiers, the variants with `'+'` appended also match as many times as they can. Yet unlike the genuine greedy quantifiers, they refuse to back-track once whatever follows them fails to match. They go by the name *possessive* quantifiers. Take `a*a` against `'aaaa'`: it matches because `a*` first grabs all 4 `'a'`s, then, upon reaching the final `'a'`, the engine backtracks so that ultimately `a*` settles for 3 `'a'`s total while the fourth `'a'` is taken by the closing `'a'`. By contrast, applying `a*+a` to `'aaaa'` has `a*+` claim all 4 `'a'`, and when the trailing `'a'` finds no further characters to match, no backtracking is possible and the whole thing fails to match. `x*+`, `x++` and `x?+` correspond respectively to `(?>x*)`, `(?>x+)` and `(?>x?)`.

Added in version 3.11.

`{m}`

Requires that exactly *m* copies of the preceding RE be matched; with fewer matches the entire RE fails. To illustrate, `a{6}` matches exactly six `'a'` characters, but not five.

`{m,n}`

Makes the resulting RE match between *m* and *n* repetitions of the preceding RE, trying for as many as it can. For instance, `a{3,5}` matches from 3 to 5 `'a'` characters. Leaving out *m* sets the lower bound to zero, and leaving out *n* sets an unbounded upper limit. As an example, `a{4,}b` matches `'aaaab'` or a thousand `'a'` characters then a `'b'`, yet not `'aaab'`. You can't drop the comma or the modifier gets mistaken for the earlier form just described.

`{m,n}?`

Makes the resulting RE match between *m* and *n* repetitions of the preceding RE, trying for as *few* as it can. This is the non-greedy counterpart of the prior quantifier. So, on the 6-character string `'aaaaaa'`, `a{3,5}` matches 5 `'a'` characters, while `a{3,5}?` matches only 3 characters.

`{m,n}+`

Makes the resulting RE match between *m* and *n* repetitions of the preceding RE, trying for as many as it can *without* laying down any backtracking points. This is the possessive counterpart of the quantifier above. So, on the 6-character string `'aaaaaa'`, `a{3,5}+aa` tries to match 5 `'a'` characters, then, needing 2 further `'a'`s, runs short of available characters and so fails, whereas `a{3,5}aa` succeeds with `a{3,5}` taking 5, then 4 `'a'`s via backtracking, and the closing `aa` in the pattern matches the last 2 `'a'`s. `x{m,n}+` corresponds to `(?>x{m,n})`.

Added in version 3.11.

`\`

Either escapes special characters (so you can match characters such as `'*'`, `'?'`, and the like), or introduces a special sequence; special sequences appear below.

When you aren't using a raw string for the pattern, keep in mind that Python likewise treats the backslash as an escape sequence within string literals; if Python's parser doesn't recognize the escape sequence, the backslash and the following character stay in the resulting string. But if Python would recognize the resulting sequence, then the backslash ought to be doubled. All of this is intricate and hard to follow, which is why raw strings come strongly recommended for everything beyond the simplest expressions.

`[]`

Used to denote a set of characters. Within a set:

- Characters may be enumerated one by one, e.g. `[amk]` matches `'a'`, `'m'`, or `'k'`.

-

[Subject index](INDEX.md) · [Previous](re-regular-expression-operations.md) · [Continue](re-a-to-re-x.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
