# Compilation flags continuation

re.M

 re.MULTILINE

(we have not yet covered `^` and `$`; the section More metacharacters will bring them in.)

By default `^` matches solely at the string's start, while `$` matches solely at the string's end and right before a trailing newline (when one exists) at the string's end. With this flag turned on, `^` matches at the string's start as well as at the start of each line inside the string, just after every newline. In the same way, the `$` metacharacter matches at the string's end and likewise at the end of every line (right before each newline).

 re.S

 re.DOTALL

Causes the `'.'` special character to match every character whatsoever, the newline included; lacking this flag, `'.'` matches anything *except* a newline.

 re.A

 re.ASCII

Make `\w`, `\W`, `\b`, `\B`, `\s` and `\S` carry out ASCII-only matching rather than complete Unicode matching. That has meaning only for Unicode patterns and gets disregarded for byte patterns.

 re.X

 re.VERBOSE

By granting extra freedom in how you lay them out, this flag lets you compose regular expressions that read more easily. Once it is turned on, whitespace inside the RE string gets dropped, the exception being whitespace within a character class or whitespace that follows an unescaped backslash; this gives you room to lay out and indent the RE more legibly. The flag additionally permits comments inside a RE which the engine skips; a comment begins with a `'#'` that sits neither inside a character class nor right after an unescaped backslash.

As an illustration, the following RE makes use of [`re.VERBOSE`](https://docs.python.org/3.14/library/re.html#re.VERBOSE); notice how much more readable it becomes:

```python
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

```

Lacking the verbose setting, that same RE would appear as follows:

```python
charref = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")

```

In that previous example, Python's habit of automatically joining adjacent string literals was leveraged to chop the RE into smaller chunks, yet it remains harder to follow than the [`re.VERBOSE`](https://docs.python.org/3.14/library/re.html#re.VERBOSE) form.

[Subject index](INDEX.md) · [Previous source owning section](compilation-flags.md) · [re.L / re.LOCALE aliases and locale matching caveats](re-l-re-locale-aliases-and-locale-matching-caveats.md) · [Following source context](re-l-re-locale-aliases-and-locale-matching-caveats.md) · [Previous source context](re-l-re-locale-aliases-and-locale-matching-caveats.md) · [Following source context](more-pattern-power.md)
