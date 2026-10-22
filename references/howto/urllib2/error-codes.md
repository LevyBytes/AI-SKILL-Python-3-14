# Error Codes

#### Error Codes

Since redirects (codes in the 300 range) are absorbed by the default handlers and codes from 100 through 299 signal success, the error codes you actually encounter normally fall in the 400–599 band.

A handy mapping of response codes is [`http.server.BaseHTTPRequestHandler.responses`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler.responses), which lists every response code defined by [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html). A portion of that dictionary appears below

```python
responses = {
    ...
    <HTTPStatus.OK: 200>: ('OK', 'Request fulfilled, document follows'),
    ...
    <HTTPStatus.FORBIDDEN: 403>: ('Forbidden',
                                  'Request forbidden -- authorization will '
                                  'not help'),
    <HTTPStatus.NOT_FOUND: 404>: ('Not Found',
                                  'Nothing matches the given URI'),
    ...
    <HTTPStatus.IM_A_TEAPOT: 418>: ("I'm a Teapot",
                                    'Server refuses to brew coffee because '
                                    'it is a teapot'),
    ...
    <HTTPStatus.SERVICE_UNAVAILABLE: 503>: ('Service Unavailable',
                                            'The server cannot process the '
                                            'request due to a high load'),
    ...
    }

```

Whenever an error fires, the server's reply includes both an HTTP error code *and* an accompanying error page. The [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) instance can serve as that returned page's response. So, on top of the code attribute, it likewise offers the read, geturl, and info methods that the `urllib.response` module provides:

```python
>>> req = urllib.request.Request('http://www.python.org/fish.html')
>>> try:
...     urllib.request.urlopen(req)
... except urllib.error.HTTPError as e:
...     print(e.code)
...     print(e.read())
...
404
b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n\n<html
  ...
  <title>Page Not Found</title>\n
  ...

```

[Subject index](INDEX.md) · [Previous source context](httperror.md) · [Following source context](wrapping-it-up.md)
