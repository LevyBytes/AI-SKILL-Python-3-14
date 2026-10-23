# What’s New In Python 3.5 / http.client - http.client

### http.client

Should a remote server connection drop unexpectedly, [`HTTPConnection.getresponse()`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection.getresponse) now raises a [`RemoteDisconnected`](https://docs.python.org/3.14/library/http.client.html#http.client.RemoteDisconnected) exception. On top of that, whenever a [`ConnectionError`](https://docs.python.org/3.14/library/exceptions.html#ConnectionError) gets raised (and `RemoteDisconnected` derives from it), the client socket closes by itself and a new connection is established on the following request:

```python
import http.client
conn = http.client.HTTPConnection('www.python.org')
for retries in range(3):
    try:
        conn.request('GET', '/')
        resp = conn.getresponse()
    except http.client.RemoteDisconnected:
        pass

```

(Contributed by Martin Panter in [bpo-3566](https://bugs.python.org/issue?@action=redirect&bpo=3566).)

[Subject index](INDEX.md) · [Previous source section](http.md) · [Next source section](idlelib-and-idle.md) · [Release/subject declaration](summary-release-highlights.md)
