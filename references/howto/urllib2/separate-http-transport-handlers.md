# Separate HTTP and transport error handlers

Call `fetch(url)` with an HTTP or HTTPS URL. It returns response bytes on success, or `None` for an HTTP or URL error. Failures while reading the response propagate; the response is still closed.

```python
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch(url):
    request = Request(url)
    try:
        response = urlopen(request, timeout=30)
    except HTTPError as error:
        print("HTTP request failed:", error.code)
        error.close()
    except URLError as error:
        print("Could not reach the server:", error.reason)
    else:
        with response:
            return response.read()
    return None
```

Catch `HTTPError` before `URLError`: HTTP errors are also URL errors.

[Subject index](INDEX.md)
