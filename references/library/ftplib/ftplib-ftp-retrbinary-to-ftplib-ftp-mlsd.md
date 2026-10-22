# ftplib.FTP: `retrbinary()`, `retrlines()`, `set_pasv()`, `storbinary()`, `storlines()`, `transfercmd()`, `ntransfercmd()`, `mlsd()`

retrbinary(*cmd*, *callback*, *blocksize=8192*, *rest=None*)

Fetch a file using binary transfer mode.

Parameters:

- **cmd** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – A suitable `RETR` command, namely `"RETR *filename*"`.

- **callback** ([callable](https://docs.python.org/3.14/glossary.html#term-callable)) – A one-argument callable invoked on every block of incoming data, whose sole argument carries that data as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

- **blocksize** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – The largest chunk read from the low-level [`socket`](https://docs.python.org/3.14/library/socket.html#socket.socket) object built to carry out the actual transfer. It likewise sets the biggest amount of data handed to *callback*. Defaults to `8192`.

- **rest** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – A `REST` command dispatched to the server. Refer to the docs covering the *rest* parameter of the `transfercmd()` method.

 retrlines(*cmd*, *callback=None*)

Pull down a file or a directory listing, decoded with whatever the *encoding* parameter specified at startup. For *cmd*, pass a suitable `RETR` command (see `retrbinary()`), or else something like `LIST` or `NLST` (most often plain `'LIST'`). With `LIST` you obtain the files plus details about them, while `NLST` yields only their names. For each line the *callback* function is invoked, handed a string holding that line minus its trailing CRLF. The default *callback* emits the line to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout).

 set_pasv(*val*)

Turn on “passive” mode when *val* is true; otherwise switch passive mode off. By default passive mode is enabled.

 storbinary(*cmd*, *fp*, *blocksize=8192*, *callback=None*, *rest=None*)

Upload a file using binary transfer mode.

Parameters:

- **cmd** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – A suitable `STOR` command, namely `"STOR *filename*"`.

- **fp** ([file object](https://docs.python.org/3.14/glossary.html#term-file-object)) – A file object (opened in binary mode) read through to EOF, drawing the data to store via its [`read()`](https://docs.python.org/3.14/library/io.html#io.RawIOBase.read) method in chunks of *blocksize* bytes.

- **blocksize** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – Size of each read block. Defaults to `8192`.

- **callback** ([callable](https://docs.python.org/3.14/glossary.html#term-callable)) – A one-argument callable invoked on every block of outgoing data, whose sole argument carries that data as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes).

- **rest** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – A `REST` command dispatched to the server. Refer to the docs covering the *rest* parameter of the `transfercmd()` method.

Changed in version 3.2: The *rest* parameter was added.

 storlines(*cmd*, *fp*, *callback=None*)

Send a file using line mode. Supply for *cmd* a suitable `STOR` command (see `storbinary()`). The [file object](https://docs.python.org/3.14/glossary.html#term-file-object) *fp* (opened in binary mode) is read line by line through to EOF via its [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) method to furnish the data being stored. *callback* is an optional one-argument callable that fires on each line once it has been sent.

 transfercmd(*cmd*, *rest=None*)

Begin a transfer across the data connection. In the active case, issue an `EPRT` or `PORT` command along with the transfer command named by *cmd*, then accept the incoming connection. When the server is passive, issue an `EPSV` or `PASV` command, connect to it, and launch the transfer command. In both situations, give back the socket for the connection.

When the optional *rest* is supplied, a `REST` command goes to the server with *rest* passed as an argument. Typically *rest* is a byte offset into the requested file, instructing the server to resume sending the file’s bytes from that offset and skip the leading bytes. Be aware, though, that the `transfercmd()` method turns *rest* into a string using the *encoding* parameter named at initialization, while performing no validation on the string’s contents. Should the server fail to recognize the `REST` command, an `error_reply` exception gets raised. In that event, just invoke `transfercmd()` without supplying a *rest* argument.

 ntransfercmd(*cmd*, *rest=None*)

Behaves like `transfercmd()`, except it gives back a tuple holding the data connection together with the anticipated size of the data. When the expected size cannot be determined, the size returned is `None`. Here *cmd* and *rest* carry the same meaning as in `transfercmd()`.

 mlsd(*path=''*, *facts=[]*)

Enumerate a directory in a standardized format via the `MLSD` command ([**RFC 3659**](https://datatracker.ietf.org/doc/html/rfc3659.html)). When *path* is left out, the current directory is taken. *facts* is a list of strings naming the kind of information you want (for example `["type", "size", "perm"]`). Yields a generator object that, for each file located under path, produces a tuple of two elements. The first element holds the file name, while the second is a dictionary of facts about that file name. The *facts* argument may narrow the dictionary’s contents, although the server is not obliged to return every requested fact.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous](ftplib-ftp-set-debuglevel-to-ftplib-ftp-voidcmd.md) · [Continue](ftplib-ftp-nlst-to-ftplib-ftp-close.md) · [Owning module, declaration or section: ftplib](ftplib-ftp-protocol-client.md) · [Owning module, declaration or section: ftplib.FTP](ftplib-ftp-class.md) · [Owning module, declaration or section: FTP objects](ftplib-ftp-class.md)
