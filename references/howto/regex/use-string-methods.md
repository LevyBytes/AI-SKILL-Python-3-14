# Use string methods

### Use string methods

Reaching for the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module is occasionally the wrong call. When you're matching a fixed string or one character class and you're not drawing on any `re` capabilities like the [`IGNORECASE`](https://docs.python.org/3.14/library/re.html#re.IGNORECASE) flag, the full might of regular expressions may simply be overkill. Strings offer a handful of methods that operate on fixed strings, and they generally run far quicker, since the machinery behind them is one compact C loop tuned for exactly that, rather than the sprawling, more general-purpose regular expression engine.

Take the case of swapping one fixed string for another — say you want `word` exchanged for `deed`. While [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) looks like the obvious tool, weigh the [`replace()`](https://docs.python.org/3.14/library/stdtypes.html#str.replace) method instead. Mind that `replace()` will swap `word` even where it sits within other words, making `swordfish` into `sdeedfish` — though the naive RE `word` would have tripped on that just the same. (Keeping the substitution off partial words means the pattern must read `\bword\b`, forcing `word` to sit between word boundaries on both sides. That demand reaches past what `replace()` can do.)

A further routine chore is wiping out every instance of a lone character from a string, or trading it for some other single character. One way is to write something along the lines of `re.sub('\n', ' ', S)`, yet [`translate()`](https://docs.python.org/3.14/library/stdtypes.html#str.translate) handles both of those jobs and outpaces anything a regular expression operation can manage.

The upshot: ahead of reaching for the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, ask yourself whether a quicker, plainer string method could crack your problem.

[Subject index](INDEX.md) · [Previous source context](common-problems.md) · [Following source context](match-versus-search.md)
