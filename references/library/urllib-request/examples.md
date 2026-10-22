# urllib.request — Examples

```python
>>> import urllib.request
>>> proxies = {'http': 'http://proxy.example.com:8080/'}
>>> opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
>>> with opener.open("https://www.python.org") as f:
...     f.read().decode('utf-8')
...

```

In the next example, no proxies are used whatsoever, which overrides what the environment settings dictate:

```python
>>> import urllib.request
>>> opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
>>> with opener.open("https://www.python.org/") as f:
...     f.read().decode('utf-8')
...

```

[Subject index](INDEX.md) · [Continue](urllib-request-urlretrieve-to-urllib-request-urlcleanup.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md) · [Owning module, declaration or section: Examples](examples-section-introduction-and-initial-examples.md) · [Preceding source contract and version conditions](url-request-post-example.md)
