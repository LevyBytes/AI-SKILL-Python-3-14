# mailbox.Mailbox: `__contains__()`, `__len__()`, `clear()`, `pop()`, `popitem()`, `update()`, `flush()`, `lock()`, `unlock()`, `close()`

__contains__(*key*)

Return `True` if *key* corresponds to a message, `False` otherwise.

 __len__()

Return a count of messages in the mailbox.

 clear()

Delete all messages from the mailbox.

 pop(*key*, *default=None*)

For the message that *key* maps to, return a representation and delete that message. Where no such message exists, return *default*. Representation uses an instance of the fitting format-specific `Message` subclass, except where a custom message factory was supplied at the time the `Mailbox` instance was initialized.

 popitem()

Return an arbitrary (*key*, *message*) pair, in which *key* names a key while *message* names a message representation, and delete the matching message. Should the mailbox be empty, raise a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception. Representation uses an instance of the fitting format-specific `Message` subclass, except where a custom message factory was supplied at the time the `Mailbox` instance was initialized.

 update(*arg*)

For the *arg* parameter, supply either a *key*-to-*message* mapping or else an iterable made of (*key*, *message*) pairs. The mailbox is updated such that, for each supplied *key* together with *message*, whatever message maps to *key* takes on the value *message*, just as `__setitem__()` would do it. As with `__setitem__()`, every *key* has to already map to a message in the mailbox, or else a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception gets raised, so generally speaking it's incorrect for *arg* to be a `Mailbox` instance.

Note

Unlike with dictionaries, keyword arguments are not supported.

 flush()

Write any pending changes out to the filesystem. With some `Mailbox` subclasses, changes are always written right away and `flush()` does nothing, but you should nonetheless get into the habit of calling this method.

 lock()

Take an exclusive advisory lock on the mailbox so other processes know not to alter it. An `ExternalClashError` is raised should the lock be unavailable. Which locking mechanisms get used hinges on the mailbox format. You should *always* lock the mailbox ahead of making any modifications to its contents.

 unlock()

Release the lock on the mailbox, if any.

 close()

Flush the mailbox, unlock it where necessary, and close any open files. With some `Mailbox` subclasses, this method does nothing.

[Subject index](INDEX.md) · [Previous](mailbox-mailbox-add-to-mailbox-mailbox-get-file.md) · [Continue](mailbox-maildir-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.Mailbox](mailbox-mailbox-class.md) · [Owning module, declaration or section: `Mailbox` objects](mailbox-mailbox-class.md)
