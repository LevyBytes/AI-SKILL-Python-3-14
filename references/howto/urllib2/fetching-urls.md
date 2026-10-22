# Fetching URLs

### Fetching URLs

At its most minimal, urllib.request is used like this:

```python
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

```

Should you want to grab a resource by URL and drop it into a temporary file, the [`shutil.copyfileobj()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfileobj) and [`tempfile.NamedTemporaryFile()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.NamedTemporaryFile) functions make that easy:

```python
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass

```

Plenty of urllib usage stays exactly this short (and note that in place of an ‘http:’ URL we might just as well have supplied one beginning with ‘ftp:’, ‘file:’, and so forth). That said, this tutorial exists to cover the harder cases, with HTTP as our focus.

The HTTP model revolves around requests and responses — clients issue requests and servers reply with responses. urllib.request reflects that design through a `Request` object standing in for the HTTP request you intend to send. The barest version simply names the URL you'd like to retrieve in a Request object. Hand that Request object to `urlopen` and you get back a response object for the URL you asked about. Because the response behaves like a file, you can, for example, invoke `.read()` on it:

```python
import urllib.request

req = urllib.request.Request('http://python.org/')
with urllib.request.urlopen(req) as response:
   the_page = response.read()

```

Bear in mind that urllib.request relies on this one Request interface no matter which URL scheme is involved. An FTP request, for instance, looks like this:

```python
req = urllib.request.Request('ftp://example.com/')

```

With HTTP specifically, Request objects unlock two additional abilities. The first is sending data along to the server. The second is conveying supplementary information (“metadata”) *about* that data or about the request itself, delivered to the server in the form of HTTP “headers”. We'll take these one at a time.

[Subject index](INDEX.md) · [Previous source context](introduction.md) · [Following source context](data.md)
