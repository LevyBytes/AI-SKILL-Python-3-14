# Python 3.5.2 release candidate 1 / library / keep http server basehttprequesthandler send error emitting message body reset content

[bpo-25738](https://bugs.python.org/issue?@action=redirect&bpo=25738): Keep http.server.BaseHTTPRequestHandler.send_error() from emitting a message body for 205 Reset Content. In addition, Content header fields are no longer sent on responses that lack a body. Susumu Koshiba contributed this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
