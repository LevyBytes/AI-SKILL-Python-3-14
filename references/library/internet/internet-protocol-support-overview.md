# Internet Protocols and Support - Section introduction and initial examples

# Internet, Intro

## Overview

Covers: Internet Protocols and Support; Introduction.

## Internet Protocols and Support

### Internet Protocols and Support

This chapter's modules supply internet protocols together with support for the technologies built around them. Every one of them is written in Python. The majority depend on the platform-specific module [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket), which today works on the platforms in widest use. The list that follows gives a summary:

- [`webbrowser` - Convenient web-browser controller](https://docs.python.org/3.14/library/webbrowser.html)
  - [Command-line interface](https://docs.python.org/3.14/library/webbrowser.html#command-line-interface)
  - [Browser controller objects](https://docs.python.org/3.14/library/webbrowser.html#browser-controller-objects)

- [`wsgiref` - WSGI Utilities and Reference Implementation](https://docs.python.org/3.14/library/wsgiref.html)
  - [`wsgiref.util` – WSGI environment utilities](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.util)
  - [`wsgiref.headers` – WSGI response header tools](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.headers)
  - [`wsgiref.simple_server` – a simple WSGI HTTP server](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.simple_server)
  - [`wsgiref.validate` - WSGI conformance checker](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.validate)
  - [`wsgiref.handlers` – server/gateway base classes](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.handlers)
  - [`wsgiref.types` – WSGI types for static type checking](https://docs.python.org/3.14/library/wsgiref.html#module-wsgiref.types)
  - [Examples](https://docs.python.org/3.14/library/wsgiref.html#examples)

- [`urllib` - URL handling modules](https://docs.python.org/3.14/library/urllib.html)
- [`urllib.request` - Extensible library for opening URLs](https://docs.python.org/3.14/library/urllib.request.html)
  - [Request Objects](https://docs.python.org/3.14/library/urllib.request.html#request-objects)
  - [OpenerDirector Objects](https://docs.python.org/3.14/library/urllib.request.html#openerdirector-objects)
  - [BaseHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#basehandler-objects)
  - [HTTPRedirectHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#httpredirecthandler-objects)
  - [HTTPCookieProcessor Objects](https://docs.python.org/3.14/library/urllib.request.html#httpcookieprocessor-objects)
  - [ProxyHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#proxyhandler-objects)
  - [HTTPPasswordMgr Objects](https://docs.python.org/3.14/library/urllib.request.html#httppasswordmgr-objects)
  - [HTTPPasswordMgrWithPriorAuth Objects](https://docs.python.org/3.14/library/urllib.request.html#httppasswordmgrwithpriorauth-objects)
  - [AbstractBasicAuthHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#abstractbasicauthhandler-objects)
  - [HTTPBasicAuthHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#httpbasicauthhandler-objects)
  - [ProxyBasicAuthHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#proxybasicauthhandler-objects)
  - [AbstractDigestAuthHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#abstractdigestauthhandler-objects)
  - [HTTPDigestAuthHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#httpdigestauthhandler-objects)
  - [ProxyDigestAuthHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#proxydigestauthhandler-objects)
  - [HTTPHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#httphandler-objects)
  - [HTTPSHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#httpshandler-objects)
  - [FileHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#filehandler-objects)
  - [DataHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#datahandler-objects)
  - [FTPHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#ftphandler-objects)
  - [CacheFTPHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#cacheftphandler-objects)
  - [UnknownHandler Objects](https://docs.python.org/3.14/library/urllib.request.html#unknownhandler-objects)
  - [HTTPErrorProcessor Objects](https://docs.python.org/3.14/library/urllib.request.html#httperrorprocessor-objects)
  - [Examples](https://docs.python.org/3.14/library/urllib.request.html#examples)
  - [Legacy interface](https://docs.python.org/3.14/library/urllib.request.html#legacy-interface)
  - [`urllib.request` Restrictions](https://docs.python.org/3.14/library/urllib.request.html#urllib-request-restrictions)

- [`urllib.response` - Response classes used by urllib](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.response)
- [`urllib.parse` - Parse URLs into components](https://docs.python.org/3.14/library/urllib.parse.html)
  - [URL Parsing](https://docs.python.org/3.14/library/urllib.parse.html#url-parsing)
  - [URL parsing security](https://docs.python.org/3.14/library/urllib.parse.html#url-parsing-security)
  - [Parsing ASCII Encoded Bytes](https://docs.python.org/3.14/library/urllib.parse.html#parsing-ascii-encoded-bytes)
  - [Structured Parse Results](https://docs.python.org/3.14/library/urllib.parse.html#structured-parse-results)
  - [URL Quoting](https://docs.python.org/3.14/library/urllib.parse.html#url-quoting)

- [`urllib.error` - Exception classes raised by urllib.request](https://docs.python.org/3.14/library/urllib.error.html)
- [`urllib.robotparser` - Parser for robots.txt](https://docs.python.org/3.14/library/urllib.robotparser.html)
- [`http` - HTTP modules](https://docs.python.org/3.14/library/http.html)
  - [HTTP status codes](https://docs.python.org/3.14/library/http.html#http-status-codes)
  - [HTTP status category](https://docs.python.org/3.14/library/http.html#http-status-category)
  - [HTTP methods](https://docs.python.org/3.14/library/http.html#http-methods)

- [`http.client` - HTTP protocol client](https://docs.python.org/3.14/library/http.client.html)
  - [HTTPConnection Objects](https://docs.python.org/3.14/library/http.client.html#httpconnection-objects)
  - [HTTPResponse Objects](https://docs.python.org/3.14/library/http.client.html#httpresponse-objects)
  - [Examples](https://docs.python.org/3.14/library/http.client.html#examples)
  - [HTTPMessage Objects](https://docs.python.org/3.14/library/http.client.html#httpmessage-objects)

- [`ftplib` - FTP protocol client](https://docs.python.org/3.14/library/ftplib.html)
  - [Reference](https://docs.python.org/3.14/library/ftplib.html#reference)
    - [FTP objects](https://docs.python.org/3.14/library/ftplib.html#ftp-objects)
    - [FTP_TLS objects](https://docs.python.org/3.14/library/ftplib.html#ftp-tls-objects)
    - [Module variables](https://docs.python.org/3.14/library/ftplib.html#module-variables)

- [`poplib` - POP3 protocol client](https://docs.python.org/3.14/library/poplib.html)
  - [POP3 Objects](https://docs.python.org/3.14/library/poplib.html#pop3-objects)
  - [POP3 Example](https://docs.python.org/3.14/library/poplib.html#pop3-example)

- [`imaplib` - IMAP4 protocol client](https://docs.python.org/3.14/library/imaplib.html)
  - [IMAP4 Objects](https://docs.python.org/3.14/library/imaplib.html#imap4-objects)
  - [IMAP4 Example](https://docs.python.org/3.14/library/imaplib.html#imap4-example)

- [`smtplib` - SMTP protocol client](https://docs.python.org/3.14/library/smtplib.html)
  - [SMTP Objects](https://docs.python.org/3.14/library/smtplib.html#smtp-objects)
  - [SMTP Example](https://docs.python.org/3.14/library/smtplib.html#smtp-example)

[Subject index](INDEX.md) · [Continue](internet-protocols-and-support.md)
