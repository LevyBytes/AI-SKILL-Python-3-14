# ftplib.FTP: `set_debuglevel()`, `connect()`, `getwelcome()`, `login()`, `abort()`, `sendcmd()`, `voidcmd()`

set_debuglevel(*level*)

Assign the instance’s debugging level as an [`int`](https://docs.python.org/3.14/library/functions.html#int). This governs how much debugging output gets printed. The debug levels are:

- `0` (default): No debug output.

- `1`: Emit a moderate volume of debug output, typically one line for each request.

- `2` or higher: Emit the fullest debugging output, recording every line sent and received over the control connection.

 connect(*host=''*, *port=0*, *timeout=None*, *source_address=None*)

Open a connection to the named host and port. Invoke this just once per instance; skip it when a *host* argument was supplied while the `FTP` instance was being built. Every other `FTP` method becomes usable only once a connection has been established successfully.

Parameters:

- **host** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The host you want to reach.

- **port** ([*int*](https://docs.python.org/3.14/library/functions.html#int)) – Which TCP port to reach (default: `21`, the value the FTP protocol specification mandates). Supplying a different port number is seldom necessary.

- **timeout** ([*float*](https://docs.python.org/3.14/library/functions.html#float)* | **None*) – How many seconds to allow the connection attempt before timing out (default: the global default timeout setting).

- **source_address** ([*tuple*](https://docs.python.org/3.14/library/stdtypes.html#tuple)* | **None*) – A 2-tuple `(host, port)` that the socket binds to as its own source address ahead of connecting.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ftplib.connect` with arguments `self`, `host`, `port`.

Changed in version 3.3: *source_address* parameter was added.

 getwelcome()

Hand back the greeting that the server returned when the connection first opened. (Disclaimers or help text useful to the user occasionally appear in this message.)

 login(*user='anonymous'*, *passwd=''*, *acct=''*)

Authenticate against the FTP server you are connected to. Call this just once per instance, once a connection exists; omit it when the *host* and *user* arguments were already passed during creation of the `FTP` instance. The bulk of FTP commands work only after the client logs in.

Parameters:

- **user** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The account name used at login (default: `'anonymous'`).

- **passwd** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – The credential supplied at login. When omitted, and where *passwd* equals the empty string or `"-"`, a password gets generated automatically.

- **acct** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)) – Account details fed to the `ACCT` FTP command. Hardly any systems implement it. Consult [RFC-959](https://datatracker.ietf.org/doc/html/rfc959.html) for further detail.

 abort()

Cancel a transfer that is currently underway. This is not guaranteed to succeed, yet it is worth attempting.

 sendcmd(*cmd*)

Transmit a plain command string to the server and give back the reply string.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ftplib.sendcmd` with arguments `self`, `cmd`.

 voidcmd(*cmd*)

Dispatch a plain command string to the server and process the reply. When the reply code indicates success (codes within 200–299), give back the reply string; otherwise raise `error_reply`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ftplib.sendcmd` with arguments `self`, `cmd`.

[Subject index](INDEX.md) · [Previous](ftplib-ftp-class.md) · [Continue](ftplib-ftp-retrbinary-to-ftplib-ftp-mlsd.md) · [Owning module, declaration or section: ftplib](ftplib-ftp-protocol-client.md) · [Owning module, declaration or section: ftplib.FTP](ftplib-ftp-class.md) · [Owning module, declaration or section: FTP objects](ftplib-ftp-class.md)
