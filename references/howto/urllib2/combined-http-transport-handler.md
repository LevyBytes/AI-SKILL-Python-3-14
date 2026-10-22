# Combined HTTP and transport error handler

Call `fetch(url)` with an HTTP or HTTPS URL. It returns response bytes on success, or `None` for an HTTP or URL error. Failures while reading the response propagate; the response is still closed.

```python
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch(url):
    request = Request(url)
    try:
        response = urlopen(request, timeout=30)
    except URLError as error:
        if isinstance(error, HTTPError):
            print("HTTP request failed:", error.code)
            error.close()
        else:
            print("Could not reach the server:", error.reason)
    else:
        with response:
            return response.read()
    return None
```

Test `HTTPError` first. It has both `code` and `reason`; checking for `reason` alone does not distinguish an HTTP response from a transport failure.

[Subject index](INDEX.md)
