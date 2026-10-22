# Unicode Objects

### Unicode Objects and Codecs

### Unicode Objects

Ever since [**PEP 393**](https://peps.python.org/pep-0393/) landed in Python 3.3, the internal storage of Unicode objects relies on several representations, which lets the runtime cover every Unicode character while keeping memory use low. Dedicated paths exist for strings whose code points all fall under 128, 256, or 65536; beyond those, code points have to remain under 1114112 (the entire Unicode range).

The UTF-8 form is generated lazily and then held within the Unicode object.

Note

As of Python 3.12 the `Py_UNICODE` representation, along with its deprecated APIs, no longer exists. Consult [**PEP 623**](https://peps.python.org/pep-0623/) for additional details.

[Subject index](INDEX.md) · [Following source contract](pyunicode-type-to-pyunicodeiter-type.md)
