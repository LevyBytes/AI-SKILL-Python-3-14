# Python 3.6.0 alpha 2 / library / keep http server basehttprequesthandler send error emitting message body reset content

[bpo-25738](https://bugs.python.org/issue?@action=redirect&bpo=25738): Keep http.server.BaseHTTPRequestHandler.send_error() from emitting a message body for 205 Reset Content. On top of that, omit Content header fields from responses lacking a body. Susumu Koshiba wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
