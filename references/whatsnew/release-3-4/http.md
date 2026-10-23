# What's New In Python 3.4 / http - http.server

### http

[`send_error()`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler.send_error) takes an optional extra *explain* parameter that lets you supply a longer error description, replacing any built-in default that may exist. That longer text is rendered through the [`error_message_format`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler.error_message_format) attribute and emitted as the error response body. (Contributed by Karl Cow in [bpo-12921](https://bugs.python.org/issue?@action=redirect&bpo=12921).)

The [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) [command line interface](https://docs.python.org/3.14/library/http.server.html#http-server-cli) gained a `-b/--bind` option that makes the server bind to a chosen address. (Contributed by Malte Swart in [bpo-17764](https://bugs.python.org/issue?@action=redirect&bpo=17764).)

[Subject index](INDEX.md) · [Previous source section](html.md) · [Next source section](idlelib-and-idle.md) · [Release/subject declaration](release-highlights.md)
