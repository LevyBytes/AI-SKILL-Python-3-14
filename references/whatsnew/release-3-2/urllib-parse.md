# What's New In Python 3.2 / urllib.parse — urllib.parse

### urllib.parse

The [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) module received a batch of usability refinements.

The [`urlparse()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlparse) function now handles [IPv6](https://en.wikipedia.org/wiki/IPv6) addresses of the kind laid out in [**RFC 2732**](https://datatracker.ietf.org/doc/html/rfc2732.html):

```python
>>> import urllib.parse
>>> urllib.parse.urlparse('http://[dead:beef:cafe:5417:affe:8FA3:deaf:feed]/foo/')
ParseResult(scheme='http',
            netloc='[dead:beef:cafe:5417:affe:8FA3:deaf:feed]',
            path='/foo/',
            params='',
            query='',
            fragment='')

```

The [`urldefrag()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urldefrag) function hands back a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) these days:

```python
>>> r = urllib.parse.urldefrag('http://python.org/about/#target')
>>> r
DefragResult(url='http://python.org/about/', fragment='target')
>>> r[0]
'http://python.org/about/'
>>> r.fragment
'target'

```

On top of that, the [`urlencode()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlencode) function has grown far more adaptable, taking the *query* argument as either a string or a bytes type. Should it be a string, the *safe*, *encoding*, and *error* parameters get forwarded onward to [`quote_plus()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.quote_plus) so encoding can happen:

```python
>>> urllib.parse.urlencode([
...      ('type', 'telenovela'),
...      ('name', '¿Dónde Está Elisa?')],
...      encoding='latin-1')
'type=telenovela&name=%BFD%F3nde+Est%E1+Elisa%3F'

```

As spelled out under [Parsing ASCII Encoded Bytes](https://docs.python.org/3.14/library/urllib.parse.html#parsing-ascii-encoded-bytes), every [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) function will now take ASCII-encoded byte strings as its input, provided you do not intermix them with ordinary strings. When you feed ASCII-encoded byte strings in as parameters, whatever comes back will likewise be ASCII-encoded byte strings:

```python
>>> urllib.parse.urlparse(b'http://www.python.org:80/about/')
ParseResultBytes(scheme=b'http', netloc=b'www.python.org:80',
                 path=b'/about/', params=b'', query=b'', fragment=b'')

```

(Work by Nick Coghlan, Dan Mahn, and Senthil Kumaran in [bpo-2987](https://bugs.python.org/issue?@action=redirect&bpo=2987), [bpo-5468](https://bugs.python.org/issue?@action=redirect&bpo=5468), and [bpo-9873](https://bugs.python.org/issue?@action=redirect&bpo=9873).)

[Subject index](INDEX.md) · [Previous source section](configparser.md) · [Next source section](mailbox.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
