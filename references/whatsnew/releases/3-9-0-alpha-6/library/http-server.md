# Python 3.9.0 alpha 6 / library / http server

[bpo-40094](https://bugs.python.org/issue?@action=redirect&bpo=40094): http.server's CGIHTTPRequestHandler now records the exit code of the CGI script instead of the exit status produced by os.waitpid(). To illustrate, a script terminated by signal 11 now produces this log entry: ?CGI script exit code -11.?

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
