# urllib.request - HTTPErrorProcessor Objects

### HTTPErrorProcessor Objects

 HTTPErrorProcessor.http_response(*request*, *response*)

Process HTTP error responses.

For 200 error codes, the response object is returned immediately.

For error codes other than 200, this just hands the work off to the `http_error_<type>()` handler methods by way of `OpenerDirector.error()`. In the end, `HTTPDefaultErrorHandler` raises an [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) should no other handler take care of the error.

 HTTPErrorProcessor.https_response(*request*, *response*)

Process HTTPS error responses.

The behavior is same as `http_response()`.

[Subject index](INDEX.md) · [Previous](unknownhandler-unknown-open.md) · [Continue](examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
