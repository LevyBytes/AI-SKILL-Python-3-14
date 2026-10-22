# Python 3.12.0 alpha 3 / library / http server

[gh-100001](https://github.com/python/cpython/issues/100001): Escape backslashes in http.server BaseHTTPRequestHandler.log_message too, so the line can be parsed and the original payload reconstructed. Without that step a `\xHH` stays ambiguous between a hex substitution we inserted and the literal characters `r'\x'` that arrived in the original request line.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
