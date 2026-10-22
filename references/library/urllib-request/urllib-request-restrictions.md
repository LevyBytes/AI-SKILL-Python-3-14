# urllib.request — `urllib.request` Restrictions

### `urllib.request` Restrictions

- For now, support extends only to these protocols: HTTP (in versions 0.9 and 1.0), FTP, local files, and data URLs.

Changed in version 3.4: Support for data URLs arrived here.

- Caching in `urlretrieve()` stays switched off until somebody gets around to implementing proper handling of Expiration time headers.

- A function for checking whether a given URL sits in the cache ought to exist.

- To preserve backward compatibility, a URL that seems to indicate a local file which then refuses to open gets reread through the FTP protocol instead. Now and then that produces puzzling error messages.

- Both the `urlopen()` and `urlretrieve()` functions may stall for any length of time as they wait on a network connection coming up. Consequently, putting together an interactive web client from these functions is hard unless you bring threads into play.

- Whatever `urlopen()` or `urlretrieve()` gives back is the server's raw data. It could be binary content (an image, for instance), plain text, or HTML among other things. Type details come from the HTTP protocol within the reply header, which you can examine by checking the *Content-Type* header. When the data that comes back is HTML, the [`html.parser`](https://docs.python.org/3.14/library/html.parser.html#module-html.parser) module is available for parsing it.

- Whatever code drives the FTP protocol has no way to tell a file apart from a directory. That can yield surprising behavior whenever you go to read a URL aimed at a file you cannot reach. A URL closing with a `/` is taken to mean a directory and is dealt with on that basis. Yet when reading a file hits a 550 error (signaling that the URL is missing or out of reach, frequently over permissions), the path is then handled as a directory, covering the situation where a URL names a directory but its trailing `/` was omitted. The upshot can mislead you while fetching a file whose read permissions block access: the FTP code attempts the read, runs into a 550 error, and goes on to list the directory for that unreadable file. Where you require finer control, look to the [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib) module.

[Subject index](INDEX.md) · [Previous](urllib-request-urlretrieve-to-urllib-request-urlcleanup.md) · [Continue](../urllib-response/urllib-response-addinfourl-class.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
