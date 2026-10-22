# mailbox.Mailbox: `add()`, `remove()`, `__delitem__()`, `discard()`, `__setitem__()`, `iterkeys()`, `keys()`, `itervalues()`, `__iter__()`, `values()`, `iteritems()`, `items()`, `get()`, `__getitem__()`, `get_message()`, `get_bytes()`, `get_string()`, `get_file()`

add(*message*)

Add *message* to the mailbox, then return the key that got assigned to it.

For the *message* parameter you may supply a `Message` instance, an [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) instance, a string, a byte string, or else a file-like object (one that ought to be open in binary mode). Should *message* be an instance of the fitting format-specific `Message` subclass (e.g., should it be an `mboxMessage` instance while this is an `mbox` instance), its format-specific information is used. If not, sensible defaults for format-specific information apply.

Changed in version 3.2: Support for binary input was added.

 remove(*key*)

 __delitem__(*key*)

 discard(*key*)

Delete the message corresponding to *key* from the mailbox.

Where no such message exists, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception is raised should the method have been called as `remove()` or `__delitem__()`, yet no exception is raised should it have been called as `discard()`. The behavior of `discard()` may be preferable when the underlying mailbox format permits concurrent modification by other processes.

 __setitem__(*key*, *message*)

Replace the message corresponding to *key* with *message*. Raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception should no message already correspond to *key*.

Just as with `add()`, for the *message* parameter you may supply a `Message` instance, an [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) instance, a string, a byte string, or else a file-like object (one that ought to be open in binary mode). Should *message* be an instance of the fitting format-specific `Message` subclass (e.g., should it be an `mboxMessage` instance while this is an `mbox` instance), its format-specific information is used. If not, the format-specific information of the message presently corresponding to *key* stays unchanged.

 iterkeys()

Return an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) over all keys

 keys()

The same as `iterkeys()`, except that a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) is returned rather than an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator)

 itervalues()

 __iter__()

Return an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) over representations of all messages. Each message is represented as an instance of the fitting format-specific `Message` subclass, unless a custom message factory was given when the `Mailbox` instance was initialized.

Note

The behavior of `__iter__()` differs from that of dictionaries, which walk over keys.

 values()

The same as `itervalues()`, except that a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) is returned rather than an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator)

 iteritems()

Return an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) over (*key*, *message*) pairs, in which *key* names a key while *message* names a message representation. Each message is represented as an instance of the fitting format-specific `Message` subclass, unless a custom message factory was given when the `Mailbox` instance was initialized.

 items()

The same as `iteritems()`, save that what comes back is a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) of pairs in place of an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) of pairs.

 get(*key*, *default=None*)

 __getitem__(*key*)

For the message that *key* maps to, return a representation. Where no such message exists, *default* is returned should the method have been called as `get()`, and a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception is raised should it have been called as `__getitem__()`. Representation uses an instance of the fitting format-specific `Message` subclass, except where a custom message factory was supplied at the time the `Mailbox` instance was initialized.

 get_message(*key*)

For the message that *key* maps to, return a representation as an instance of the fitting format-specific `Message` subclass, or raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception should no such message exist.

 get_bytes(*key*)

For the message that *key* maps to, return a byte representation, or raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception should no such message exist.

Added in version 3.2.

 get_string(*key*)

For the message that *key* maps to, return a string representation, or raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception should no such message exist. The message is run through [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) to turn it into a 7bit clean representation.

 get_file(*key*)

For the message that *key* maps to, return a [file-like](https://docs.python.org/3.14/glossary.html#term-file-like-object) representation, or raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception should no such message exist. The file-like object acts as though open in binary mode. This file ought to be closed once you no longer need it.

Changed in version 3.2: The file object genuinely is a [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file); before, it had wrongly been returned in text mode. On top of that, the [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) now honors the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol: a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement can close it for you automatically.

Note

Unlike other representations of messages, [file-like](https://docs.python.org/3.14/glossary.html#term-file-like-object) representations aren't necessarily independent of the `Mailbox` instance that produced them or of the underlying mailbox. Each subclass supplies more specific documentation.

[Subject index](INDEX.md) · [Previous](mailbox-mailbox-class.md) · [Continue](mailbox-mailbox-contains-to-mailbox-mailbox-close.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.Mailbox](mailbox-mailbox-class.md) · [Owning module, declaration or section: `Mailbox` objects](mailbox-mailbox-class.md)
