# ftplib - Module variables

### Module variables

 *exception *ftplib.error_reply

Raised when the server sends back an unexpected reply.

 *exception *ftplib.error_temp

Raised when an error code denoting a temporary error (response codes within 400–499) arrives.

 *exception *ftplib.error_perm

Raised when an error code denoting a permanent error (response codes within 500–599) arrives.

 *exception *ftplib.error_proto

Raised when the server returns a reply that breaks the response rules of the File Transfer Protocol, that is, one beginning with a digit within 1–5.

 ftplib.all_errors

The collection of every exception (given as a tuple) that `FTP` instance methods can raise because of trouble with the FTP connection (as distinct from programming mistakes the caller makes). Alongside the four exceptions named above, this collection takes in [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) and [`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError).

See also

Module [`netrc`](https://docs.python.org/3.14/library/netrc.html#module-netrc)

Parser for the `.netrc` file format. FTP clients commonly read the `.netrc` file to pick up user authentication details ahead of prompting the user.

[Subject index](INDEX.md) · [Previous](ftplib-ftp-tls-auth-to-ftplib-ftp-tls-prot-c.md) · [Continue](../functional/functional-programming-modules.md) · [Owning module, declaration or section: ftplib](ftplib-ftp-protocol-client.md)
