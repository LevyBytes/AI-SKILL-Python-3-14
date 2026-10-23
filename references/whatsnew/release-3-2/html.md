# What's New In Python 3.2 / html - html

### html

The fresh [`html`](https://docs.python.org/3.14/library/html.html#module-html) module arrives carrying just one function, [`escape()`](https://docs.python.org/3.14/library/html.html#html.escape), whose job is escaping the reserved characters found in HTML markup:

```python
>>> import html
>>> html.escape('x > 2 && x < 7')
'x &gt; 2 &amp;&amp; x &lt; 7'
```

[Subject index](INDEX.md) · [Previous source section](sqlite3.md) · [Next source section](socket.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
