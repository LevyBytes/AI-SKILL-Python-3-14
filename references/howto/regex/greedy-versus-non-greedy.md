# Greedy versus non-greedy

### Greedy versus non-greedy

Repeating a regular expression, the way `a*` does, leads it to swallow as much of the pattern as it can. That trait often trips you up when you set out to match a pair of balanced delimiters, like the angle brackets wrapping an HTML tag. A naive pattern aimed at one HTML tag falls short precisely because `.*` is greedy.

```python
>>> s = '<html><head><title>Title</title>'
>>> len(s)
32
>>> print(re.match('<.*>', s).span())
(0, 32)
>>> print(re.match('<.*>', s).group())
<html><head><title>Title</title>

```

The RE lands on the `'<'` within `'<html>'`, after which `.*` gobbles up everything else in the string. But the RE still has more to go, and `>` cannot match at the string's end, so the regular expression engine must walk back one character at a time until it lands a match for `>`. The match it settles on runs from the `'<'` in `'<html>'` all the way to the `'>'` in `'</title>'` — not at all what you were after.

The remedy here is to employ the non-greedy quantifiers `*?`, `+?`, `??`, or `{m,n}?`, which grab as *little* text as they can. In that earlier example, `'>'` is attempted the instant the first `'<'` matches, and on failing, the engine inches forward one character, re-attempting `'>'` at each move. The outcome is exactly right:

```python
>>> print(re.match('<.*?>', s).group())
<html>

```

(Bear in mind that wrangling HTML or XML through regular expressions is a misery. Slapdash patterns cover the everyday cases, yet HTML and XML harbor edge cases that shatter the obvious regular expression; once you've crafted one that copes with every conceivable case, the patterns turn *very* tangled. For such work, lean on an HTML or XML parser module.)

[Subject index](INDEX.md) · [Previous source context](match-versus-search.md) · [Following source context](using-re-verbose.md)
