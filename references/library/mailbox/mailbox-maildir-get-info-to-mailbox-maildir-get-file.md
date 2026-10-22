# mailbox.Maildir: `get_info()`, `set_info()`, `add()`, `__setitem__()`, `update()`, `flush()`, `lock()`, `unlock()`, `close()`, `get_file()`

get_info(*key*)

Return a string holding the info for the message corresponding to *key*. This matches `get_message(key).get_info()` but runs much faster, since it doesn't open the message file. Reach for this method while iterating over the keys to figure out which messages are worth fetching.

Where a `MaildirMessage` object is on hand, reach for its `get_info()` method instead, since edits applied via the message's `set_info()` method won't appear here until the mailbox's `__setitem__()` method has run.

Added in version 3.13.

 set_info(*key*, *info*)

Set the info of the message corresponding to *key* to *info*. Invoking `some_mailbox.set_info(key, flags)` resembles

```python
one_message = some_mailbox.get_message(key)
one_message.set_info(info)
some_mailbox[key] = one_message

```

but faster, since it doesn't open the message file.

When you do hold a `MaildirMessage` object, use its `set_info()` method instead, because changes made through this mailbox method won't be visible to the message object's method, `get_info()`.

Added in version 3.13.

A few `Mailbox` methods that `Maildir` implements warrant particular notes:

 add(*message*)

 __setitem__(*key*, *message*)

 update(*arg*)

Warning

These methods produce unique file names drawn from the current process ID. With multiple threads in play, undetected name clashes may arise and corrupt the mailbox unless threads are coordinated so as not to use these methods on the same mailbox at the same moment.

 flush()

Every change to Maildir mailboxes takes effect at once, so this method does nothing.

 lock()

 unlock()

Maildir mailboxes neither support nor require locking, so these methods do nothing.

 close()

`Maildir` instances hold no open files and the underlying mailboxes don't support locking, so this method does nothing.

 get_file(*key*)

Depending on the host platform, modifying or removing the underlying message may not be feasible while the returned file stays open.

See also

[maildir man page from Courier](https://www.courier-mta.org/maildir.html)

A specification of the format. Describes a common extension for supporting folders.

[Using maildir format](https://cr.yp.to/proto/maildir.html)

The inventor's own notes on Maildir. Covers a revised name-creation scheme along with specifics of “info” semantics.

[Subject index](INDEX.md) · [Previous](mailbox-maildir-list-folders-to-mailbox-maildir-remove-flag.md) · [Continue](mailbox-mbox-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.Maildir](mailbox-maildir-class.md) · [Owning module, declaration or section: `Maildir` objects](mailbox-maildir-class.md)
