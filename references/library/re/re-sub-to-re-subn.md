# re: `re.sub()`, `re.subn()`

re.sub(*pattern*, *repl*, *string*, *count=0*, *flags=0*)

Produce the string you get when the leftmost non-overlapping occurrences of *pattern* in *string* are swapped for the replacement *repl*. Should the pattern not turn up, *string* comes back untouched. *repl* may be a string or a function; when it is a string, any backslash escapes within it are handled. That means `\n` becomes a single newline character, `\r` becomes a carriage return, and so on. Unknown escapes of ASCII letters are held back for later use and treated as errors. Other unknown escapes such as `\&` stay as they are. Backreferences like `\6` are swapped for whatever substring group 6 matched in the pattern. For instance:

```python
>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
...        r'static PyObject*\npy_\1(void)\n{',
...        'def myfunc():')
'static PyObject*\npy_myfunc(void)\n{'

```

When *repl* is a function, it gets invoked for each non-overlapping occurrence of *pattern*. That function accepts one `Match` argument and gives back the replacement string. For instance:

```python
>>> def dashrepl(matchobj):
...     if matchobj.group(0) == '-': return ' '
...     else: return '-'
...
>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
'pro--gram files'
>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
'Baked Beans & Spam'

```

The pattern may be a string or a `Pattern`.

The optional argument *count* caps how many pattern occurrences get replaced; *count* has to be a non-negative integer. Leaving it out or setting it to zero replaces every occurrence.

Two empty matches cannot sit side by side, though an empty match may follow right on the heels of a non-empty one. Because of this, `sub('x*', '-', 'abxd')` produces `'-a-b--d-'` rather than `'-a-b-d-'`.

Within string-type *repl* arguments, on top of the character escapes and backreferences already covered, `\g<name>` pulls in the substring matched by the group called `name`, as set up by the `(?P<name>...)` syntax. `\g<number>` brings in the matching group number; `\g<2>` is thus the same as `\2`, yet stays unambiguous in a replacement like `\g<2>0`. `\20` would be read as a reference to group 20 rather than a reference to group 2 trailed by the literal character `'0'`. The backreference `\g<0>` substitutes the full substring that the RE matched.

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

Changed in version 3.1: introduced the optional flags argument.

Changed in version 3.5: groups that go unmatched are swapped for an empty string.

Changed in version 3.6: inside *pattern*, an unknown escape made of `'\'` plus an ASCII letter is now an error.

Changed in version 3.7: inside *repl*, an unknown escape made of `'\'` plus an ASCII letter is now an error. An empty match may land right after a non-empty one.

Changed in version 3.12: a group *id* is limited to ASCII digits. Within [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) replacement strings, a group *name* may hold only bytes inside the ASCII range (`b'\x00'`-`b'\x7f'`).

Deprecated since version 3.13: handing *count* and *flags* over as positional arguments is now deprecated. Upcoming Python releases will make them [keyword-only parameters](https://docs.python.org/3.14/glossary.html#keyword-only-parameter).

 re.subn(*pattern*, *repl*, *string*, *count=0*, *flags=0*)

Carry out the very same operation as `sub()`, but give back a tuple `(new_string, number_of_subs_made)`.

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

[Subject index](INDEX.md) · [Previous](re-split-to-re-finditer.md) · [Continue](re-escape-to-re-purge.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Functions](re-compile-to-re-fullmatch.md)
