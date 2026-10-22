# re: `re.compile()`, `re.search()`, `re.match()`, `re.fullmatch()`

### Functions

 re.compile(*pattern*, *flags=0*)

Turn a regular expression pattern into a regular expression object, which then supports matching through its `match()`, `search()` and the additional methods covered further on.

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

This sequence

```python
prog = re.compile(pattern)
result = prog.match(string)

```

is equivalent to

```python
result = re.match(pattern, string)

```

yet calling `re.compile()` and keeping the produced regular expression object around for reuse pays off when the expression is applied repeatedly throughout one program.

Note

Because the compiled forms of the patterns most recently supplied to `re.compile()` and to the module-level matching functions are cached, programs working with only a handful of regular expressions at once have no need to fret about compiling regular expressions.

 re.search(*pattern*, *string*, *flags=0*)

Look through *string* for the earliest spot where the regular expression *pattern* yields a match, returning a matching `Match`. Hand back `None` when no position in the string matches the pattern; observe that this differs from turning up a zero-length match somewhere inside the string.

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

 re.match(*pattern*, *string*, *flags=0*)

When some or all of the leading characters of *string* match the regular expression *pattern*, give back a matching `Match`. Return `None` if the string fails to match the pattern; observe that this differs from a zero-length match.

Keep in mind that, even under `MULTILINE` mode, `re.match()` only matches at the string's start rather than at the start of each line.

To find a match somewhere within *string*, reach for `search()` instead (see also search() vs. match()).

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

 re.fullmatch(*pattern*, *string*, *flags=0*)

When the entire *string* matches the regular expression *pattern*, hand back a matching `Match`. Return `None` if the string fails to match the pattern; observe that this differs from a zero-length match.

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](re-u-to-re-verbose.md) · [Continue](re-split-to-re-finditer.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
