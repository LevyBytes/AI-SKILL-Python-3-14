# What's New In Python 3.10 / Optional `EncodingWarning` and `encoding="locale"` option - io, sys

### Optional `EncodingWarning` and `encoding="locale"` option

How [`TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) and [`open()`](https://docs.python.org/3.14/library/functions.html#open) encode by default hinges on the platform and the locale. Given that UTF-8 prevails across most Unix platforms, leaving out the `encoding` option while opening UTF-8 files (e.g. JSON, YAML, TOML, Markdown) ranks among the most frequent bugs. As an illustration:

```python
# BUG: "rb" mode or encoding="utf-8" should be used.
with open("data.json") as f:
    data = json.load(f)

```

So that this category of bug can be spotted, an optional `EncodingWarning` was introduced. It fires whenever [`sys.flags.warn_default_encoding`](https://docs.python.org/3.14/library/sys.html#sys.flags) holds true and the locale-driven default encoding gets used.

To turn the warning on, the `-X warn_default_encoding` option and [`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING) were added.

Consult [Text Encoding](https://docs.python.org/3.14/library/io.html#io-text-encoding) for additional detail.

[Subject index](INDEX.md) · [Previous source section](pep-634-structural-pattern-matching-other-key-features.md) · [Next source section](new-features-related-to-type-hints.md) · [Release/subject declaration](summary-release-highlights.md)
