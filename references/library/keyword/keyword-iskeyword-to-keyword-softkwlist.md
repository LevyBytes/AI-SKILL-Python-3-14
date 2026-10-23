# keyword`keyword` - Testing for Python keywords

### `keyword` - Testing for Python keywords

**Source code:** [Lib/keyword.py](https://github.com/python/cpython/tree/3.14/Lib/keyword.py)

---

With this module a Python program can find out whether a given string counts as a [keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#keywords) or a [soft keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords).

 keyword.iskeyword(*s*)

Gives back `True` when *s* names a Python [keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#keywords).

 keyword.kwlist

A sequence holding every one of the [keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#keywords) the interpreter defines. Where certain keywords take effect only while specific [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) statements are active, those appear here too.

 keyword.issoftkeyword(*s*)

Gives back `True` when *s* names a Python [soft keyword](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords).

Added in version 3.9.

 keyword.softkwlist

A sequence holding every one of the [soft keywords](https://docs.python.org/3.14/reference/lexical_analysis.html#soft-keywords) the interpreter defines. Where certain soft keywords take effect only while specific [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) statements are active, those appear here too.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous](testing-for-python-keywords.md) · [Continue](../language/python-language-services.md)
