# http.server / HTTP servers: `http.server.CGIHTTPRequestHandler`, `do_POST()`

*class *http.server.CGIHTTPRequestHandler(*request*, *client_address*, *server*)

This class serves either files or the output of CGI scripts taken from the current directory and its subtree. Note that the HTTP hierarchic structure is mapped onto the local directory structure precisely as `SimpleHTTPRequestHandler` does it.

Note

CGI scripts launched by the `CGIHTTPRequestHandler` class are unable to perform redirects (HTTP code 302), since code 200 (script output follows) goes out before the CGI script runs. That overrides the status code.

The class will nonetheless run the CGI script — rather than serving it as a file — when it determines that the file is a CGI script. Only directory-based CGI is supported; the other widespread server configuration treats particular extensions as marking CGI scripts.

The `do_GET()` and `do_HEAD()` functions are adapted to execute CGI scripts and deliver their output, instead of serving files, when the request points somewhere beneath the `cgi_directories` path.

This data member is defined by `CGIHTTPRequestHandler`:

 cgi_directories

This defaults to `['/cgi-bin', '/htbin']` and names the directories regarded as holding CGI scripts.

This method is defined by `CGIHTTPRequestHandler`:

 do_POST()

This method handles the `'POST'` request type, permitted only for CGI scripts. Error 501, "Can only POST to CGI scripts", is emitted on any attempt to POST to a non-CGI url.

Be aware that CGI scripts will execute under the UID of user nobody, as a security measure. Failures within the CGI script will be reported as error 403.

Deprecated since version 3.13, will be removed in version 3.15: Removal of `CGIHTTPRequestHandler` is scheduled for 3.15. For more than ten years CGI has been viewed as a poor approach. The code has gone without maintenance for some time and gets little real-world usage. Keeping it around risks adding more security concerns.

[Subject index](INDEX.md) · [Previous](simple-http-file-request-handler.md) · [Continue](command-line-file-server.md) · [Owning module, declaration or section: http.server](http-server-httpserver-class.md)
