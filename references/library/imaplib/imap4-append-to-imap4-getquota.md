# imaplib: IMAP command arguments, authentication and mailbox operations

### IMAP4 Objects

Every IMAP4rev1 command maps to a method bearing the same name, in either uppercase or lowercase.

Command arguments are all turned into strings, with the exception of `AUTHENTICATE` and the final argument to `APPEND`, which goes through as an IMAP4 literal. Where needed (when the string holds IMAP4 protocol-sensitive characters and is not wrapped in either parentheses or double quotes) the string gets quoted. That said, the *password* argument to the `LOGIN` command is quoted in every case. To keep an argument string from being quoted (for example, the *flags* argument to `STORE`), wrap the string in parentheses (for example, `r'(\Deleted)'`).

The majority of commands give back a tuple: `(type, [data, ...])`, where *type* is typically `'OK'` or `'NO'`, and *data* is either the text of the command response or the results the command mandates. Each *data* is a `bytes` value or a tuple. When it is a tuple, the first element is the response header and the second carries the data (that is, the ‘literal’ value).

The *message_set* options used by the commands below form a string designating one or more messages to operate on. This may be a lone message number (`'1'`), a span of message numbers (`'2:4'`), or several non-contiguous spans joined by commas (`'1:3,6:9'`). A span may include an asterisk to denote an unbounded upper limit (`'3:*'`).

An `IMAP4` instance exposes these methods:

 IMAP4.append(*mailbox*, *flags*, *date_time*, *message*)

Append *message* to named mailbox.

 IMAP4.authenticate(*mechanism*, *authobject*)

Authenticate command: requires response processing.

*mechanism* names the authentication mechanism to apply — it ought to show up in the instance variable `capabilities` as `AUTH=mechanism`.

*authobject* has to be a callable object:

```python
data = authobject(response)

```

It is invoked to handle server continuation responses; the *response* argument supplied to it will be `bytes`. It ought to return `bytes` *data*, which gets base64 encoded and dispatched to the server. It ought to return `None` when the client abort response `*` should be transmitted instead.

Changed in version 3.5: rather than being confined to ASCII, string usernames and passwords now get encoded to `utf-8`.

 IMAP4.check()

Checkpoint mailbox on server.

 IMAP4.close()

Close the mailbox currently selected. Deleted messages get purged from a writable mailbox. This is the command advised before `LOGOUT`.

 IMAP4.copy(*message_set*, *new_mailbox*)

Copy *message_set* messages onto end of *new_mailbox*.

 IMAP4.create(*mailbox*)

Create new mailbox named *mailbox*.

 IMAP4.delete(*mailbox*)

Delete old mailbox named *mailbox*.

 IMAP4.deleteacl(*mailbox*, *who*)

Delete the ACLs (remove any rights) set for who on mailbox.

 IMAP4.enable(*capability*)

Enable *capability* (see [**RFC 5161**](https://datatracker.ietf.org/doc/html/rfc5161.html)). The bulk of capabilities require no enabling. At present only the `UTF8=ACCEPT` capability is handled (see [**RFC 6855**](https://datatracker.ietf.org/doc/html/rfc6855.html)).

Added in version 3.5: The `enable()` method itself, and [**RFC 6855**](https://datatracker.ietf.org/doc/html/rfc6855.html) support.

 IMAP4.expunge()

Permanently strip deleted items out of the selected mailbox. Produces an `EXPUNGE` response for each message deleted. The returned data holds a list of `EXPUNGE` message numbers in the order they arrived.

 IMAP4.fetch(*message_set*, *message_parts*)

Fetch (parts of) messages. *message_parts* should be a string listing message part names inside parentheses, for example `"(UID BODY[TEXT])"`. The data returned are tuples pairing message part envelope with data.

 IMAP4.getacl(*mailbox*)

Get the `ACL`s for *mailbox*. Though non-standard, this method works with the `Cyrus` server.

 IMAP4.getannotation(*mailbox*, *entry*, *attribute*)

Retrieve the specified `ANNOTATION`s for *mailbox*. Though non-standard, this method works with the `Cyrus` server.

 IMAP4.getquota(*root*)

Get the `quota` *root*’s resource usage and limits. This method forms part of the IMAP4 QUOTA extension defined in rfc2087.

[Subject index](INDEX.md) · [Previous](imaplib-internaldate2tuple-to-imaplib-time2internaldate.md) · [Continue](imap4-getquotaroot-to-imap4-lsub.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md)
