# re: `re.escape()`, `re.purge()`

re.escape(*pattern*)

Escape the special characters found in *pattern*. This comes in handy when you need to match some arbitrary literal string that might carry regular expression metacharacters. For instance:

```python
>>> print(re.escape('https://www.python.org'))
https://www\.python\.org

>>> legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
>>> print('[%s]+' % re.escape(legal_chars))
[abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+

>>> operators = ['+', '-', '*', '/', '**']
>>> print('|'.join(map(re.escape, sorted(operators, reverse=True))))
/|\-|\+|\*\*|\*

```

Never apply this function to the replacement string for `sub()` and `subn()`; there, only backslashes ought to be escaped. For instance:

```python
>>> digits_re = r'\d+'
>>> sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
>>> print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))
/usr/sbin/sendmail - \d+ errors, \d+ warnings

```

Changed in version 3.3: the `'_'` character no longer gets escaped.

Changed in version 3.7: escaping is now limited to characters able to carry special meaning within a regular expression. Consequently, `'!'`, `'"'`, `'%'`, `"'"`, `','`, `'/'`, `':'`, `';'`, `'<'`, `'='`, `'>'`, `'@'`, and `"`"` are no longer escaped.

 re.purge()

Clear the regular expression cache.

[Subject index](INDEX.md) · [Previous](re-sub-to-re-subn.md) · [Continue](re-patternerror.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Functions](re-compile-to-re-fullmatch.md)
