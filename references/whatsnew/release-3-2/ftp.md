# What's New In Python 3.2 / ftp - fileinput, ftplib, mmap, socket, ssl

### ftp

To swallow [`socket.error`](https://docs.python.org/3.14/library/socket.html#socket.error) exceptions unconditionally and shut the FTP connection once finished, the [`ftplib.FTP`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP) class now honors the context management protocol:

```python
>>> from ftplib import FTP
>>> with FTP("ftp1.at.proftpd.org") as ftp:
        ftp.login()
        ftp.dir()

'230 Anonymous login ok, restrictions apply.'
dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 .
dr-xr-xr-x   9 ftp      ftp           154 May  6 10:43 ..
dr-xr-xr-x   5 ftp      ftp          4096 May  6 10:43 CentOS
dr-xr-xr-x   3 ftp      ftp            18 Jul 10  2008 Fedora

```

Comparable auto-closing context managers were granted to other file-like objects too, among them [`mmap.mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) and [`fileinput.input()`](https://docs.python.org/3.14/library/fileinput.html#fileinput.input):

```python
with fileinput.input(files=('log1.txt', 'log2.txt')) as f:
    for line in f:
        process(line)

```

(Contributed by Tarek Ziad? and Giampaolo Rodol? in [bpo-4972](https://bugs.python.org/issue?@action=redirect&bpo=4972), and by Georg Brandl in [bpo-8046](https://bugs.python.org/issue?@action=redirect&bpo=8046) and [bpo-1286](https://bugs.python.org/issue?@action=redirect&bpo=1286).)

A *context* parameter is now taken by the [`FTP_TLS`](https://docs.python.org/3.14/library/ftplib.html#ftplib.FTP_TLS) class; it is an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object that lets you gather SSL configuration choices, certificates and private keys into one (possibly long-lived) structure.

(Contributed by Giampaolo Rodol?; [bpo-8806](https://bugs.python.org/issue?@action=redirect&bpo=8806).)

[Subject index](INDEX.md) · [Previous source section](decimal-and-fractions.md) · [Next source section](popen.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
