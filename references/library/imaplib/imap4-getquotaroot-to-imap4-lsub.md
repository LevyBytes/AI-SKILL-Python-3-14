# imaplib: `IMAP4.getquotaroot()`, `IMAP4.idle()`, `Idler.burst()`, `IMAP4.list()`, `IMAP4.login()`, `IMAP4.login_cram_md5()`, `IMAP4.logout()`, `IMAP4.lsub()`

IMAP4.getquotaroot(*mailbox*)

Get the list of `quota` `roots` for the named *mailbox*. This method forms part of the IMAP4 QUOTA extension defined in rfc2087.

 IMAP4.idle(*duration=None*)

Return an `Idler`: an iterable context manager that implements the IMAP4 `IDLE` command described by [**RFC 2177**](https://datatracker.ietf.org/doc/html/rfc2177.html).

Once the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement activates it, the returned object issues the `IDLE` command, surfaces IMAP untagged responses through the [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) protocol, and sends `DONE` when the context closes.

Every untagged response landing after the `IDLE` command is sent (even any arriving before the server acknowledges the command) will be reachable through iteration. Whatever responses are left over (those not iterated inside the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) context) can be obtained the usual way once `IDLE` finishes, by means of `IMAP4.response()`.

Responses take the form of `(type, [data, ...])` tuples, just as described in IMAP4 Objects.

The *duration* argument caps how long (in seconds) idling continues, after which any iteration still running stops. It may be an [`int`](https://docs.python.org/3.14/library/functions.html#int) or [`float`](https://docs.python.org/3.14/library/functions.html#float), or `None` for an unlimited time. To dodge inactivity timeouts on servers that enforce them, callers should keep this no higher than 29 minutes (1740 seconds). A socket connection is required; on `IMAP4_stream` connections *duration* has to be `None`.

```pycon
>>> with M.idle(duration=29 * 60) as idler:
...     for typ, data in idler:
...         print(typ, data)
...
EXISTS [b'1']
RECENT [b'1']

```

 Idler.burst(*interval=0.1*)

Yield a burst of responses spaced by no more than *interval* seconds (given as an [`int`](https://docs.python.org/3.14/library/functions.html#int) or [`float`](https://docs.python.org/3.14/library/functions.html#float)).

This [generator](https://docs.python.org/3.14/glossary.html#term-generator) offers an alternative to taking one response at a time, meant to support efficient batch processing. It grabs the next response together with any that are immediately ready afterward. (For instance, a fast succession of `EXPUNGE` responses following a bulk delete.)

A socket connection is required; this does not function on `IMAP4_stream` connections.

```pycon
>>> with M.idle() as idler:
...     # get a response and any others following by < 0.1 seconds
...     batch = list(idler.burst())
...     print(f'processing {len(batch)} responses...')
...     print(batch)
...
processing 3 responses...
[('EXPUNGE', [b'2']), ('EXPUNGE', [b'1']), ('RECENT', [b'0'])]

```

Tip

The `IDLE` context’s maximum duration, handed to `IMAP4.idle()`, is honored while awaiting the first response of a burst. Consequently, an `Idler` that has expired causes this generator to return at once without yielding anything. Callers ought to bear this in mind when using it inside a loop.

Note

The iterator that `IMAP4.idle()` returns may be used solely within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Outside of that context, unsolicited responses get gathered internally each time a command completes, and they can be obtained with `IMAP4.response()`.

Note

The `Idler` class name and structure are internal interfaces and may change. Calling code may count on its context management, iteration, and public method staying stable, but should not subclass, instantiate, compare, or otherwise reference the class directly.

Added in version 3.14.

 IMAP4.list([*directory*[, *pattern*]])

List mailbox names within *directory* that match *pattern*. *directory* defaults to the top-level mail folder, while *pattern* defaults to matching anything. The data returned holds a list of `LIST` responses.

 IMAP4.login(*user*, *password*)

Identify the client by means of a plaintext password. The *password* gets quoted.

 IMAP4.login_cram_md5(*user*, *password*)

Compel the use of `CRAM-MD5` authentication when identifying the client so as to safeguard the password. This functions only when the server `CAPABILITY` response carries the phrase `AUTH=CRAM-MD5`.

Changed in version 3.14: When MD5 support is missing, an `IMAP4.error` gets raised.

 IMAP4.logout()

Shutdown connection to server. Returns server `BYE` response.

Changed in version 3.8: arbitrary exceptions are no longer swallowed silently by the method.

 IMAP4.lsub(*directory='""'*, *pattern='*'*)

List the subscribed mailbox names found in directory that match pattern. *directory* falls back to the top level directory, while *pattern* falls back to matching any mailbox. The data returned consists of tuples pairing message part envelope with data.

[Subject index](INDEX.md) · [Previous](imap4-append-to-imap4-getquota.md) · [Continue](imap4-myrights-to-imap4-setannotation.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md) · [Owning module, declaration or section: IMAP4 Objects](imap4-append-to-imap4-getquota.md)
