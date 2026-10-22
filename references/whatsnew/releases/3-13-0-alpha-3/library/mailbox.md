# Python 3.13.0 alpha 3 / library / mailbox

[bpo-21360](https://bugs.python.org/issue?@action=redirect&bpo=21360): Files whose names begin with a dot are now skipped by [`mailbox.Maildir`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Maildir).

[gh-66515](https://github.com/python/cpython/issues/66515): Folders lacking a `.mh_sequences` file (for example Claws Mail IMAP-cache folders) are now handled by [`mailbox.MH`](https://docs.python.org/3.14/library/mailbox.html#mailbox.MH). Serhiy Storchaka wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
