# ftplib — `ftplib` — FTP protocol client

# Ftplib, Functional

## Overview

Covers: ftplib — FTP protocol client; Functional Programming Modules.

## ftplib — FTP protocol client

### `ftplib` — FTP protocol client

**Source code:** [Lib/ftplib.py](https://github.com/python/cpython/tree/3.14/Lib/ftplib.py)

---

The class `FTP` plus a handful of supporting items live in this module. On the FTP protocol, the `FTP` class supplies the client half. With it you can author Python programs that carry out assorted automated FTP tasks, mirroring other FTP servers being one example. The module [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) also relies on it to deal with URLs that use FTP. Internet [**RFC 959**](https://datatracker.ietf.org/doc/html/rfc959.html) holds further detail about FTP (File Transfer Protocol).

UTF-8 is the default encoding, in keeping with [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

Below is an example session that exercises the `ftplib` module:

```python
>>> from ftplib import FTP
>>> ftp = FTP('ftp.us.debian.org')  # connect to host, default port
>>> ftp.login()                     # user anonymous, passwd anonymous@
'230 Login successful.'
>>> ftp.cwd('debian')               # change into "debian" directory
'250 Directory successfully changed.'
>>> ftp.retrlines('LIST')           # list directory contents
-rw-rw-r--    1 1176     1176         1063 Jun 15 10:18 README
...
drwxr-sr-x    5 1176     1176         4096 Dec 19  2000 pool
drwxr-sr-x    4 1176     1176         4096 Nov 17  2008 project
drwxr-xr-x    3 1176     1176         4096 Oct 10  2012 tools
'226 Directory send OK.'
>>> with open('README', 'wb') as fp:
>>>     ftp.retrbinary('RETR README', fp.write)
'226 Transfer complete.'
>>> ftp.quit()
'221 Goodbye.'

```

[Subject index](INDEX.md) · [Continue](ftplib-ftp-class.md)
