# urllib.request — Examples — Section introduction and initial examples

### Examples

Beyond the examples shown below, you'll find further examples in [HOWTO Fetch Internet Resources Using The urllib Package](https://docs.python.org/3.14/howto/urllib2.html#urllib-howto).

This example retrieves the python.org main page and shows its first 300 bytes:

```python
>>> import urllib.request
>>> with urllib.request.urlopen('https://www.python.org/') as f:
...     # The response may be compressed (for example, 'gzip').
...     print(f.headers.get('Content-Encoding'))
...     data = f.read()
...     if f.headers.get('Content-Encoding') == 'gzip':
...         import gzip
...         data = gzip.decompress(data)
...     print(data[:300].decode('utf-8', errors='replace'))

```

Be aware that urlopen hands back a bytes object. The reason is that urlopen has no means of working out on its own the encoding of the byte stream it gets from the HTTP server. As a rule, a program will turn the returned bytes object into a string once it has worked out or guessed the right encoding.

The HTML spec document at [https://html.spec.whatwg.org/#charset](https://html.spec.whatwg.org/#charset) catalogs the several methods by which an HTML or XML document might have declared its encoding information.

For further detail, consult the W3C document at [https://www.w3.org/International/questions/qa-html-encoding-declarations](https://www.w3.org/International/questions/qa-html-encoding-declarations).

Since the python.org site declares *utf-8* encoding in its meta tag, we'll apply that same encoding to decode the bytes object:

```python
>>> with urllib.request.urlopen('https://www.python.org/') as f:
...     # Check for compression and decode appropriately.
...     enc = f.headers.get('Content-Encoding')
...     data = f.read()
...     if enc == 'gzip':
...         import gzip
...         data = gzip.decompress(data)
...     print(data[:100].decode('utf-8', errors='replace'))
...

```

The very same outcome can equally be reached without resorting to the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) approach:

```python
>>> import urllib.request
>>> f = urllib.request.urlopen('https://www.python.org/')
>>> try:
...     enc = f.headers.get('Content-Encoding')
...     data = f.read()
...     if enc == 'gzip':
...         import gzip
...         data = gzip.decompress(data)
...     print(data[:100].decode('utf-8', errors='replace'))
... finally:
...     f.close()

```

The example that follows sends a data-stream into the stdin of a CGI and reads back the data it hands us in return. Be aware that this example runs only when the Python installation has SSL support.

```python
>>> import urllib.request
>>> req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi',
...                       data=b'This data is passed to stdin of the CGI')
>>> with urllib.request.urlopen(req) as f:
...     print(f.read().decode('utf-8'))
...
Got Data: "This data is passed to stdin of the CGI"

```

The code for the sample CGI used in the above example is:

```python
#!/usr/bin/env python
import sys
data = sys.stdin.read()
print('Content-type: text/plain\n\nGot Data: "%s"' % data)

```

Here is an example of doing a `PUT` request using `Request`:

[Subject index](INDEX.md) · [Previous](http-and-https-error-response-processing.md) · [Continue](examples-code-example-import-urllib-request-pass.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
