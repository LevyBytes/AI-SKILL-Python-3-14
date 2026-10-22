# Unicode Regular Expressions

### Unicode Regular Expressions

You can hand the regular expressions that the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module supports to it as either bytes or strings. Several of the special character sequences such as `\d` and `\w` carry different meanings according to whether the pattern arrives as bytes or as a string. For instance, `\d` matches the characters `[0-9]` in bytes but in strings matches any character belonging to the `'Nd'` category.

In the following example the string holds the number 57 written out in both Thai and Arabic numerals:

```python
import re
p = re.compile(r'\d+')

s = "Over \u0e55\u0e57 57 flavours"
m = p.search(s)
print(repr(m.group()))

```

Once run, `\d+` matches the Thai numerals and prints them out. Pass the [`re.ASCII`](https://docs.python.org/3.14/library/re.html#re.ASCII) flag to [`compile()`](https://docs.python.org/3.14/library/re.html#re.compile) and `\d+` matches the substring “57” instead.

In the same vein, `\w` matches a broad assortment of Unicode characters but only `[a-zA-Z0-9_]` in bytes or when [`re.ASCII`](https://docs.python.org/3.14/library/re.html#re.ASCII) is given, and `\s` matches either Unicode whitespace characters or `[ \t\n\r\f\v]`.

[Subject index](INDEX.md) · [Previous source context](comparing-strings.md) · [Following source context](references.md)
