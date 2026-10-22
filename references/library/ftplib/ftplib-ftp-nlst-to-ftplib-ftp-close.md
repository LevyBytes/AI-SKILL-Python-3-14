# ftplib.FTP: `nlst()`, `dir()`, `rename()`, `delete()`, `cwd()`, `mkd()`, `pwd()`, `rmd()`, `size()`, `quit()`, `close()`

nlst(*argument*[, *...*])

Give back a list of file names as produced by the `NLST` command. The optional *argument* names a directory to enumerate (the current server directory by default). Several arguments may be supplied to feed non-standard options into the `NLST` command.

Note

If your server supports the command, `mlsd()` offers a better API.

 dir(*argument*[, *...*])

Generate a directory listing as produced by the `LIST` command and print it to standard output. The optional *argument* names a directory to enumerate (the current server directory by default). Several arguments may be supplied to feed non-standard options into the `LIST` command. When the final argument is a function, it serves as a *callback* function the way it does for `retrlines()`; by default output goes to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout). The return value of this method is `None`.

Note

If your server supports the command, `mlsd()` offers a better API.

 rename(*fromname*, *toname*)

Rename file *fromname* on the server to *toname*.

 delete(*filename*)

Delete the file called *filename* from the server. On success it returns the response text; otherwise it raises `error_perm` for permission failures or `error_reply` for other failures.

 cwd(*pathname*)

Set the current directory on the server.

 mkd(*pathname*)

Create a new directory on the server.

 pwd()

Return the pathname of the current directory on the server.

 rmd(*dirname*)

Remove the directory named *dirname* on the server.

 size(*filename*)

Ask for the size of the file called *filename* on the server. When this succeeds, the file’s size comes back as an integer; otherwise `None` is returned. Keep in mind that the `SIZE` command is not standardized, though plenty of widespread server implementations support it.

 quit()

Issue a `QUIT` command to the server and shut the connection. This counts as the “polite” means of closing a connection, but it can raise an exception when the server answers the `QUIT` command with an error. Doing so entails a call to the `close()` method, which leaves the `FTP` instance unusable for later calls (see below).

 close()

Shut the connection one-sidedly. Do not apply this to a connection that is already closed, such as after a successful `quit()` call. Once this runs, the `FTP` instance should no longer be used (following a call to `close()` or `quit()` you cannot reopen the connection by invoking another `login()` method).

[Subject index](INDEX.md) · [Previous](ftplib-ftp-retrbinary-to-ftplib-ftp-mlsd.md) · [Continue](ftplib-ftp-tls-class.md) · [Owning module, declaration or section: ftplib](ftplib-ftp-protocol-client.md) · [Owning module, declaration or section: ftplib.FTP](ftplib-ftp-class.md) · [Owning module, declaration or section: FTP objects](ftplib-ftp-class.md)
