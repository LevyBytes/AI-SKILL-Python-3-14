# smtplib: `SMTP.set_debuglevel()`, `SMTP.docmd()`, `SMTP.connect()`, `SMTP.helo()`, `SMTP.ehlo()`, `SMTP.ehlo_or_helo_if_needed()`, `SMTP.has_extn()`, `SMTP.verify()`, `SMTP.login()`

### SMTP Objects

An `SMTP` instance offers the following methods:

 SMTP.set_debuglevel(*level*)

Set the debug output level. Passing 1 or `True` for *level* produces debug messages covering the connection and every message exchanged with the server. Passing 2 for *level* makes those messages timestamped.

Changed in version 3.5: Added debuglevel 2.

 SMTP.docmd(*cmd*, *args=''*)

Send a command *cmd* to the server. The optional argument *args* is just appended to the command, with a space between them.

It returns a 2-tuple holding a numeric response code together with the actual response line (multiline responses get joined into a single long line.)

Under ordinary operation there should be no need to invoke this method directly. It backs the implementation of other methods and can be handy when testing private extensions.

Should the connection to the server drop while it awaits the reply, `SMTPServerDisconnected` is raised.

 SMTP.connect(*host='localhost'*, *port=0*)

Connect to a host on a particular port. By default it connects to the local host at the standard SMTP port (25). When the hostname concludes with a colon (`':'`) followed by a number, that suffix is removed and the number is read as the port number to apply. The constructor calls this method automatically when a host is named at instantiation. Returns a 2-tuple holding the response code and message the server sends in its connection response.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `smtplib.connect` with arguments `self`, `host`, `port`.

 SMTP.helo(*name=''*)

Announce yourself to the SMTP server with `HELO`. By default the hostname argument takes the local host's fully qualified domain name. Whatever message the server returns is kept as the object's `helo_resp` attribute.

Under ordinary operation there should be no need to invoke this method directly. `sendmail()` calls it implicitly when required.

 SMTP.ehlo(*name=''*)

Announce yourself to an ESMTP server with `EHLO`. By default the hostname argument takes the local host's fully qualified domain name. Inspect the response for ESMTP options and retain them so `has_extn()` can use them. It also fills in several informational attributes: the message the server returns is held as the `ehlo_resp` attribute, `does_esmtp` is set to `True` or `False` according to whether the server supports ESMTP, and `esmtp_features` becomes a dictionary listing the names of the SMTP service extensions this server supports, along with their parameters (if any).

Unless you intend to call `has_extn()` ahead of sending mail, there should be no need to invoke this method directly. `sendmail()` calls it implicitly when required.

 SMTP.ehlo_or_helo_if_needed()

This method invokes `ehlo()` and/or `helo()` whenever no `EHLO` or `HELO` command has yet been sent during this session. It attempts ESMTP `EHLO` first.

`SMTPHeloError`

The server failed to respond correctly to the `HELO` greeting.

 SMTP.has_extn(*name*)

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) when *name* belongs to the set of SMTP service extensions the server reported, [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise. Case does not matter.

 SMTP.verify(*address*)

Verify that an address on this server is valid using SMTP `VRFY`. Returns a tuple made up of code 250 and a complete [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html) address (human name included) when the user address checks out. Otherwise it returns an SMTP error code of 400 or higher along with an error string.

Note

Plenty of sites turn off SMTP `VRFY` to thwart spammers.

 SMTP.login(*user*, *password*, ***, *initial_response_ok=True*)

Authenticate against an SMTP server that requires it. The arguments are the username and the password to authenticate with. When no `EHLO` or `HELO` command has yet been sent during this session, the method attempts ESMTP `EHLO` first. The method returns normally once authentication succeeds, or it may raise the following exceptions:

`SMTPHeloError`

The server failed to respond correctly to the `HELO` greeting.

`SMTPAuthenticationError`

The server rejected the username/password combination.

`SMTPNotSupportedError`

The `AUTH` command is not supported by the server.

`SMTPException`

No appropriate authentication method could be found.

Every authentication method that `smtplib` supports is attempted one after another provided the server advertises it as supported. See `auth()` for the roster of supported authentication methods. *initial_response_ok* is forwarded to `auth()`.

The optional keyword argument *initial_response_ok* indicates whether, for authentication methods that allow it, an “initial response” as defined in [**RFC 4954**](https://datatracker.ietf.org/doc/html/rfc4954.html) may accompany the `AUTH` command, instead of requiring a challenge/response.

Changed in version 3.5: `SMTPNotSupportedError` may be raised, and the *initial_response_ok* parameter was added.

[Subject index](INDEX.md) · [Previous](smtplib-smtpexception-to-smtplib-smtpauthenticationerror.md) · [Continue](smtp-auth-to-smtp-starttls.md) · [Owning module, declaration or section: smtplib](smtplib-smtp-class.md)
