# URLError

### URLError

A common trigger for URLError is the absence of a network connection (no route exists to the named server) or the named server not being a real one. When that happens, the exception comes with a ‘reason’ attribute holding a tuple made up of an error code together with a textual error message.

e.g.

```python
>>> req = urllib.request.Request('http://www.pretend_server.org')
>>> try: urllib.request.urlopen(req)
... except urllib.error.URLError as e:
...     print(e.reason)
...
(4, 'getaddrinfo failed')

```

[Subject index](INDEX.md) · [Previous source context](handling-exceptions.md) · [Following source context](httperror.md)
