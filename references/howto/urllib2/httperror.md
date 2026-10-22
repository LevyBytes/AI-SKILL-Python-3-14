# HTTPError

### HTTPError

Each HTTP response the server returns carries a numeric “status code”. On occasion that code signals that the server can't satisfy what was asked. A subset of these responses gets dealt with for you by the default handlers (for instance, when the response is a “redirection” telling the client to fetch the document from another URL, urllib takes care of it). Anything the handlers can't resolve causes urlopen to throw an [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError). Errors you'll commonly hit include ‘404’ (page not found), ‘403’ (request forbidden), and ‘401’ (authentication required).

For a rundown of every HTTP error code, turn to section 10 of [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html).

Every [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) instance carries an integer ‘code’ attribute that matches the error the server reported.

[Subject index](INDEX.md) · [Previous source context](urlerror.md) · [Following source context](error-codes.md)
