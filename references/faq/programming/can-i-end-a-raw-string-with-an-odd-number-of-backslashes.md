# Can I end a raw string with an odd number of backslashes?

### Can I end a raw string with an odd number of backslashes?

If a raw string finishes with an odd count of backslashes, it will escape the string’s closing quote:

```python
>>> r'C:\this\will\not\work\'
  File "<stdin>", line 1
    r'C:\this\will\not\work\'
    ^
SyntaxError: unterminated string literal (detected at line 1)

```

A few workarounds exist. The first is to switch to regular strings and double up the backslashes:

```python
>>> 'C:\\this\\will\\work\\'
'C:\\this\\will\\work\\'

```

A second is to join a regular string holding an escaped backslash onto the raw string:

```python
>>> r'C:\this\will\work' '\\'
'C:\\this\\will\\work\\'

```

You can also rely on [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join) to tack a backslash on under Windows:

```python
>>> os.path.join(r'C:\this\will\work', '')
'C:\\this\\will\\work\\'

```

Bear in mind that although a backslash will “escape” a quote when it comes to deciding where the raw string finishes, no escaping takes place when the raw string’s value is interpreted. In other words, the backslash stays in the raw string’s value:

```python
>>> r'backslash\'preserved'
"backslash\\'preserved"

```

Consult the specification in the [language reference](https://docs.python.org/3.14/reference/lexical_analysis.html#strings) as well.

[Subject index](INDEX.md)
