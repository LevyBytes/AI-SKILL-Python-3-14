# io - Text Encoding

### Text Encoding

By default, `TextIOWrapper` and [`open()`](https://docs.python.org/3.14/library/functions.html#open) use a locale-specific encoding ([`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding)).

That said, plenty of programmers neglect to state the encoding while opening text files stored in UTF-8 (JSON, TOML, Markdown, and the like), because the majority of Unix platforms default to a UTF-8 locale. The result is bugs, since for most Windows users the locale encoding isn't UTF-8. Take this case:

```python
# May not work on Windows when non-ASCII characters in the file.
with open("README.md") as f:
    long_description = f.read()

```

For that reason, stating the encoding outright whenever you open text files is strongly advised. For UTF-8, supply `encoding="utf-8"`. For the current locale encoding, `encoding="locale"` has been supported since Python 3.10.

See also

[Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode)

Python UTF-8 Mode lets you switch the default encoding away from a locale-specific one and over to UTF-8.

[**PEP 686**](https://peps.python.org/pep-0686/)

In Python 3.15, [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) becomes the default.

[Subject index](INDEX.md) · [Previous](raw-i-o.md) · [Continue](opt-in-encodingwarning.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)
