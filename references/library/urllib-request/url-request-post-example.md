# urllib.request — Examples — Code example: >>> import urllib.request

```python
>>> import urllib.request
>>> import urllib.parse
>>> params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
>>> url = "https://www.python.org/?%s" % params
>>> with urllib.request.urlopen(url) as f:
...     print(f.read().decode('utf-8'))
...

```

The example that follows turns to the `POST` method in its place. Take note that the params output from urlencode is encoded to bytes prior to being sent on to urlopen as data:

```python
>>> import urllib.request
>>> import urllib.parse
>>> data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
>>> data = data.encode('ascii')
>>> with urllib.request.urlopen("https://httpbin.org/post", data) as f:
...     print(f.read().decode('utf-8'))
...

```

The following example uses an explicitly specified HTTP proxy, overriding environment settings:

[Subject index](INDEX.md) · [Previous](examples-code-example-import-urllib-request-pass.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md) · [Owning module, declaration or section: Examples](examples-section-introduction-and-initial-examples.md) · [Required continuation of the source contract](examples.md)
