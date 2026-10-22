# imaplib: IMAP mailbox selection, rights, search and annotations

IMAP4.myrights(*mailbox*)

Display my ACLs for a given mailbox (that is, the rights I hold on it).

 IMAP4.namespace()

Returns IMAP namespaces as defined in [**RFC 2342**](https://datatracker.ietf.org/doc/html/rfc2342.html).

 IMAP4.noop()

Send `NOOP` to server.

 IMAP4.open(*host*, *port*, *timeout=None*)

Opens a socket to *port* at *host*. The optional *timeout* parameter gives a timeout in seconds for the connection attempt. When timeout is absent or set to `None`, the global default socket timeout governs. Note as well that setting the *timeout* parameter to zero makes it raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), rejecting the creation of a non-blocking socket. The `IMAP4` constructor calls this method implicitly. The connection objects this method sets up serve the `IMAP4.read()`, `IMAP4.readline()`, `IMAP4.send()`, and `IMAP4.shutdown()` methods. Overriding this method is permitted.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `imaplib.open` with arguments `self`, `host`, `port`.

Changed in version 3.9: The *timeout* parameter was added.

 IMAP4.partial(*message_num*, *message_part*, *start*, *length*)

Fetch a truncated portion of a message. The data returned is a tuple holding the message part envelope and its data.

 IMAP4.proxyauth(*user*)

Assume authentication as *user*. This lets an authorised administrator proxy into the mailbox of any user.

 IMAP4.read(*size*)

Reads *size* bytes from the remote server. You may override this method.

 IMAP4.readline()

Reads one line from the remote server. You may override this method.

 IMAP4.recent()

Prompt the server for an update. The data returned is `None` when there are no new messages, otherwise the value of the `RECENT` response.

 IMAP4.rename(*oldmailbox*, *newmailbox*)

Rename mailbox named *oldmailbox* to *newmailbox*.

 IMAP4.response(*code*)

If the response *code* was received, return its data; otherwise return `None`. In place of the usual type, the supplied code is returned.

 IMAP4.search(*charset*, *criterion*[, *...*])

Search the mailbox for messages that match. *charset* may be `None`, and in that situation no `CHARSET` is named in the request sent to the server. The IMAP protocol demands that at least one criterion be given; an exception arises when the server reports an error. *charset* must be `None` whenever the `UTF8=ACCEPT` capability was turned on through the `enable()` command.

Example:

```python
# M is a connected IMAP4 instance...
typ, msgnums = M.search(None, 'FROM', '"LDJ"')

# or:
typ, msgnums = M.search(None, '(FROM "LDJ")')

```

 IMAP4.select(*mailbox='INBOX'*, *readonly=False*)

Select a mailbox. The data returned is the message count in *mailbox* (`EXISTS` response). *mailbox* defaults to `'INBOX'`. When the *readonly* flag is set, the mailbox cannot be modified.

 IMAP4.send(*data*)

Sends `data` to the remote server. You may override this method.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `imaplib.send` with arguments `self`, `data`.

 IMAP4.setacl(*mailbox*, *who*, *what*)

Set an `ACL` for *mailbox*. Though non-standard, this method works with the `Cyrus` server.

 IMAP4.setannotation(*mailbox*, *entry*, *attribute*[, *...*])

Set `ANNOTATION`s for *mailbox*. Though non-standard, this method works with the `Cyrus` server.

[Subject index](INDEX.md) · [Previous](imap4-getquotaroot-to-imap4-lsub.md) · [Continue](imap4-setquota-to-imap4-xatom.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md) · [Owning module, declaration or section: IMAP4 Objects](imap4-append-to-imap4-getquota.md)
