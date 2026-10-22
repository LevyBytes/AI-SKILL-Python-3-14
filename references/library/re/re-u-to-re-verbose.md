# re: `re.U`, `re.UNICODE`, `re.X`, `re.VERBOSE`

re.U

 re.UNICODE

Within Python 3, `str` patterns match Unicode characters automatically. As a result this flag is redundant with **no effect** and survives purely for backward compatibility.

See `ASCII` to restrict matching to ASCII characters instead.

 re.X

 re.VERBOSE

With this flag you can compose regular expressions that read more cleanly, since it lets you visually break the pattern into logical chunks and attach comments. Within the pattern, whitespace is disregarded, save for whitespace inside a character class, whitespace following an unescaped backslash, or whitespace within tokens such as `*?`, `(?:` or `(?P<...>`. As an illustration, `(? :` and `* ?` are disallowed. Should a line carry a `#` that sits outside a character class and is not preceded by an unescaped backslash, every character running from that leftmost `#` to the line's end is disregarded.

Consequently, the next two regular expression objects, both matching a decimal number, are functionally identical:

```python
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

```

Corresponds to the inline flag `(?x)`.

[Subject index](INDEX.md) · [Previous](re-regexflag-class-to-re-dotall.md) · [Continue](re-compile-to-re-fullmatch.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Flags](re-regexflag-class-to-re-dotall.md)
