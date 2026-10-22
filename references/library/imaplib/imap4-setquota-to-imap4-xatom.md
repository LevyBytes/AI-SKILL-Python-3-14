# imaplib: IMAP quotas, TLS, message flags and subscriptions

IMAP4.setquota(*root*, *limits*)

Set the `quota` *root*’s resource *limits*. This method forms part of the IMAP4 QUOTA extension defined in rfc2087.

 IMAP4.shutdown()

Tear down the connection that `open` set up. `IMAP4.logout()` invokes this method implicitly. Overriding it is permitted.

 IMAP4.socket()

Returns socket instance used to connect to server.

 IMAP4.sort(*sort_criteria*, *charset*, *search_criterion*[, *...*])

The `sort` command is a variant of `search` that applies sorting semantics to the results. The data returned holds a space separated list of matching message numbers.

Preceding the *search_criterion* argument(s), sort accepts two arguments: a parenthesized *sort_criteria* list, plus the searching *charset*. Keep in mind that the searching *charset* argument here is mandatory, in contrast to `search`. A `uid sort` command also exists, relating to `sort` just as `uid search` relates to `search`. First, `sort` scans the mailbox for messages satisfying the given searching criteria, applying the charset argument when interpreting strings within those criteria. After that, it hands back the numbers of the matching messages.

This is an `IMAP4rev1` extension command.

 IMAP4.starttls(*ssl_context=None*)

Send a `STARTTLS` command. The optional *ssl_context* argument should be a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object. Doing so turns on encryption for the IMAP connection. Please read [Security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security) for best practices.

Added in version 3.2.

Changed in version 3.4: Hostname checking via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname) and *Server Name Indication* (see [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)) is now handled by the method.

 IMAP4.status(*mailbox*, *names*)

Request named status conditions for *mailbox*.

 IMAP4.store(*message_set*, *command*, *flag_list*)

Alters flag dispositions for messages in mailbox. *command* is given by section 6.4.6 of [**RFC 2060**](https://datatracker.ietf.org/doc/html/rfc2060.html) as one of “FLAGS”, “+FLAGS”, or “-FLAGS”, optionally carrying a “.SILENT” suffix.

For instance, to apply the delete flag to every message:

```python
typ, data = M.search(None, 'ALL')
for num in data[0].split():
   M.store(num, '+FLAGS', '\\Deleted')
M.expunge()

```

Note

Building flags that contain ‘]’ (for example: “[test]”) breaches [**RFC 3501**](https://datatracker.ietf.org/doc/html/rfc3501.html) (the IMAP protocol). Even so, imaplib has long permitted the creation of such tags, and widely used IMAP servers, Gmail among them, accept and emit such flags. Non-Python programs that produce such tags exist as well. Despite being an RFC violation — and despite IMAP clients and servers being expected to be strict — imaplib goes on allowing such tags to be created for backward compatibility reasons, and since Python 3.6 it handles them when the server sends them, because doing so improves real-world compatibility.

 IMAP4.subscribe(*mailbox*)

Subscribe to new mailbox.

 IMAP4.thread(*threading_algorithm*, *charset*, *search_criterion*[, *...*])

The `thread` command is a variant of `search` that applies threading semantics to the results. The data returned holds a space separated list of thread members.

Thread members are made up of zero or more message numbers, separated by spaces, marking successive parent and child.

Preceding the *search_criterion* argument(s), thread accepts two arguments: a *threading_algorithm*, plus the searching *charset*. Keep in mind that the searching *charset* argument here is mandatory, in contrast to `search`. A `uid thread` command also exists, relating to `thread` just as `uid search` relates to `search`. First, `thread` scans the mailbox for messages satisfying the given searching criteria, applying the *charset* argument when interpreting strings within those criteria. After that, it gives back the matched messages, threaded by the threading algorithm that was specified.

This is an `IMAP4rev1` extension command.

 IMAP4.uid(*command*, *arg*[, *...*])

Execute command args against messages identified by UID rather than by message number. Returns the response that suits the command. At least one argument has to be given; when none are supplied, the server returns an error and an exception is raised.

 IMAP4.unsubscribe(*mailbox*)

Unsubscribe from old mailbox.

 IMAP4.unselect()

`imaplib.IMAP4.unselect()` releases the server’s resources tied to the selected mailbox and brings the server back to the authenticated state. It carries out the same actions as `imaplib.IMAP4.close()`, except that none of the messages in the currently selected mailbox are permanently removed.

Added in version 3.9.

 IMAP4.xatom(*name*[, *...*])

Allow simple extension commands notified by server in `CAPABILITY` response.

These attributes are defined on instances of `IMAP4`:

[Subject index](INDEX.md) · [Previous](imap4-myrights-to-imap4-setannotation.md) · [Continue](imap4-protocol-version-to-imap4-utf8-enabled.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md) · [Owning module, declaration or section: IMAP4 Objects](imap4-append-to-imap4-getquota.md)
