# mailbox — `mailbox` — Manipulate mailboxes in various formats

### `mailbox` — Manipulate mailboxes in various formats

**Source code:** [Lib/mailbox.py](https://github.com/python/cpython/tree/3.14/Lib/mailbox.py)

---

Two classes, `Mailbox` and `Message`, are defined in this module for reaching and working with on-disk mailboxes plus the messages they hold. `Mailbox` provides a dictionary-like mapping from keys to messages. `Message` builds on the [`email.message`](https://docs.python.org/3.14/library/email.message.html#module-email.message) module's [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) class with format-specific state and behavior. The mailbox formats supported are Maildir, mbox, MH, Babyl, and MMDF.

See also

Module [`email`](https://docs.python.org/3.14/library/email.html#module-email)

Represent and manipulate messages.

[Subject index](INDEX.md) · [Continue](mailbox-mailbox-class.md)
