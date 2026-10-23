# What’s New in Python 2.6 / New and Improved Modules - datetime, unicodedata, urllib.request, warnings, xmlrpc.client, xmlrpc.server

A `turtle.cfg` file lets you tailor the initial look of the turtle's screen.

  - The module's docstrings can be swapped out for new docstrings translated into a different language.

([bpo-1513695](https://bugs.python.org/issue?@action=redirect&bpo=1513695))

- An optional `timeout` parameter was tacked onto the [`urllib.urlopen`](https://docs.python.org/3.14/library/urllib.request.html#urllib.request.urlopen) function and the `urllib.ftpwrapper` class constructor, as well as the `urllib2.urlopen` function. That parameter names a timeout in seconds. For instance:

```python
>>> u = urllib2.urlopen("http://slow.example.com",
                        timeout=3)
Traceback (most recent call last):
  ...
urllib2.URLError: <urlopen error timed out>
>>>

```

(Added by Facundo Batista.)

- The Unicode database that the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module supplies has been brought up to version 5.1.0. (Updated by Martin von Löwis; [bpo-3811](https://bugs.python.org/issue?@action=redirect&bpo=3811).)

- The `formatwarning()` and `showwarning()` functions in the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module gained an optional *line* argument usable for providing the line of source code. (Added as part of [bpo-1631171](https://bugs.python.org/issue?@action=redirect&bpo=1631171), which rebuilt part of the `warnings` module in C code.)

There's a new `catch_warnings()` function, a context manager meant for testing that lets you briefly adjust the warning filters and afterward restore their original values ([bpo-3781](https://bugs.python.org/issue?@action=redirect&bpo=3781)).

- By handing `False` to the *bind_and_activate* constructor parameter, you can keep the XML-RPC [`SimpleXMLRPCServer`](https://docs.python.org/3.14/library/xmlrpc.server.html#module-xmlrpc.server) and `DocXMLRPCServer` classes from opening and binding their socket right away. This lets you tweak the instance's `allow_reuse_address` attribute before the `server_bind()` and `server_activate()` methods run to open the socket and start listening for connections. (Contributed by Peter Parente; [bpo-1599845](https://bugs.python.org/issue?@action=redirect&bpo=1599845).)

`SimpleXMLRPCServer` also carries a `_send_traceback_header` attribute; when true, the exception and a formatted traceback come back as the HTTP headers "X-Exception" and "X-Traceback". This capability exists strictly for debugging and ought to stay off production servers, since those tracebacks risk leaking sensitive details such as passwords. (Contributed by Alan McIntyre, who built it during his Google's Summer of Code 2007 project.)

- The [`xmlrpclib`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) module no longer turns [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) into the [`xmlrpclib.DateTime`](https://docs.python.org/3.14/library/xmlrpc.client.html#xmlrpc.client.DateTime) type on its own; that conversion's semantics weren't necessarily right for every application. Code relying on `xmlrpclib` should convert its `date` and `time` instances itself. ([bpo-1330538](https://bugs.python.org/issue?@action=redirect&bpo=1330538)) The code can also cope with dates earlier than 1900 (contributed by Ralf Schmitt; [bpo-2014](https://bugs.python.org/issue?@action=redirect&bpo=2014)) and with 64-bit integers carried via `<i8>` inside XML-RPC responses (contributed by Riku Lindblad; [bpo-2985](https://bugs.python.org/issue?@action=redirect&bpo=2985)).

-

[Subject index](INDEX.md) · [Previous source section](new-and-improved-modules-whitespace-to-whitespace.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](attribute-lookup-and-process-module-changes.md) · [Following release/subject continuation](new-and-improved-modules-unpack-all-the-files-in-the-archive.md)
