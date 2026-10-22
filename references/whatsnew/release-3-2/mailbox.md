# What's New In Python 3.2 / mailbox — email, io, mailbox

### mailbox

Through a focused push by R. David Murray, the [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox) module was repaired for Python 3.2. The difficulty was that mailbox started life with a text-oriented interface, yet email messages are most faithfully held as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) since separate portions of a single message can carry differing encodings.

That fix leaned on the binary parsing support inside the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package to read arbitrary email messages. Several API changes were also necessary to make it work.

As you might predict, the [`add()`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Mailbox.add) method belonging to [`mailbox.Mailbox`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Mailbox) objects now takes binary input.

Both [`StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) and text file input have been deprecated. On top of that, string input fails right away when non-ASCII characters appear. Formerly the failure surfaced only once the email reached a later processing step.

Binary output is covered as well. The [`get_file()`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Mailbox.get_file) method hands back a file opened in binary mode (whereas before it wrongly placed the file into text-mode). A new [`get_bytes()`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Mailbox.get_bytes) method has also been added that yields a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) form of the message tied to a supplied *key*.

You may still obtain non-binary output by way of the old API’s [`get_string()`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Mailbox.get_string) method, though that route gains you little. The preferable approach is to pull messages out of a [`Message`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Message) object or to read them in from binary input.

(Contributed by R. David Murray, helped along by Steffen Daode Nurpmeso, building on a first patch from Victor Stinner in [bpo-9124](https://bugs.python.org/issue?@action=redirect&bpo=9124).)

[Subject index](INDEX.md) · [Previous source section](urllib-parse.md) · [Next source section](turtledemo.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
