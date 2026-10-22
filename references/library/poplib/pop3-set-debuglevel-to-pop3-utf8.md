# poplib: POP3 authentication, mailbox and message commands

### POP3 Objects

Every POP3 command maps to a like-named method, written in lowercase; for the most part each returns the reply text the server sent back.

The methods below belong to a `POP3` instance:

`POP3.set_debuglevel(*level*)`

Choose how much debugging the instance emits. This governs how verbose the debug output is. With the default, `0`, nothing is printed. Pass `1` for a modest stream, usually one line for every request. Pass `2` or above for the fullest output, which records every line that crosses the control connection in either direction.

`POP3.getwelcome()`

Hands back the greeting text the POP3 server issued.

`POP3.capa()`

Ask the server which capabilities it offers, per [**RFC 2449**](https://datatracker.ietf.org/doc/html/rfc2449.html). The reply comes as a dictionary shaped like `{'name': ['param'...]}`.

Added in version 3.4.

`POP3.user(*username*)`

Issue the user command; the reply ought to say that a password is now expected.

`POP3.pass_(*password*)`

Transmit the password; the reply carries the message tally and mailbox size. Be aware: the server keeps the mailbox locked until `quit()` runs.

`POP3.apop(*user*, *secret*)`

Sign in to the POP3 server with the sturdier APOP authentication.

`POP3.rpop(*user*)`

Sign in to the POP3 server using RPOP authentication (akin to the UNIX r-commands).

`POP3.stat()`

Fetch the mailbox status. What comes back is a 2-integer tuple: `(message count, mailbox size)`.

`POP3.list([*which*])`

Ask for the message list; the reply takes the shape `(response, ['mesg_num octets', ...], octets)`. Supplying *which* names the single message to list.

`POP3.retr(*which*)`

Pull down the entire message numbered *which* and mark it seen. The reply has the form `(response, ['line', ...], octets)`.

`POP3.dele(*which*)`

Mark message number *which* to be deleted. On the majority of servers nothing is actually erased until QUIT (Eudora QPOP being the standout — it knowingly breaks the RFCs by enacting queued deletes on any disconnect).

`POP3.rset()`

Clear every pending deletion mark for the mailbox.

`POP3.noop()`

Take no action. Handy as a keep-alive.

`POP3.quit()`

Sign off: write changes, release the mailbox lock, and close the connection.

`POP3.top(*which*, *howmuch*)`

Pull the header of message number *which* together with *howmuch* lines of body that follow it. The reply has the form `(response, ['line', ...], octets)`.

The POP3 TOP command behind this method, in contrast to RETR, leaves the message’s seen flag untouched; regrettably the RFCs pin down TOP poorly and many off-brand servers get it wrong. Try the method by hand against whatever POP3 servers you intend to use before you rely on it.

`POP3.uidl(*which=None*)`

Give back the list of message digests (unique ids). Naming *which* yields just that message’s unique id, shaped as `'response mesgnum uid`; otherwise you get the list `(response, ['mesgnum uid', ...], octets)`.

`POP3.utf8()`

Attempt to flip into UTF-8 mode. On success it returns the server reply; on failure it raises `error_proto`. Defined by [**RFC 6856**](https://datatracker.ietf.org/doc/html/rfc6856.html).

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](poplib-error-proto.md) · [Continue](pop3-stls.md) · [Owning module, declaration or section: poplib](poplib-pop3-class.md)
