# mailbox — MH additional method behavior

This operation invalidates already-issued keys, which therefore ought not to be used afterward.

A few `Mailbox` methods that `MH` implements warrant particular notes:

 remove(*key*)

 __delitem__(*key*)

 discard(*key*)

These methods delete the message at once. The MH practice of flagging a message for deletion by sticking a comma in front of its name is not employed.

 lock()

 unlock()

Three locking schemes come into play—dot locking plus, where they're available, the `flock()` and `lockf()` system calls. For MH mailboxes, locking the mailbox amounts to locking the `.mh_sequences` file and, solely while operations that touch them are underway, locking individual message files.

 get_file(*key*)

Depending on the host platform, removing the underlying message may not be feasible while the returned file stays open.

 flush()

Every change to MH mailboxes takes effect at once, so this method does nothing.

 close()

`MH` instances hold no open files, so this method amounts to the same thing as `unlock()`.

See also

[nmh - Message Handling System](https://www.nongnu.org/nmh/)

Home page of **nmh**, an updated version of the original **mh**.

[MH & nmh: Email for Users & Programmers](https://rand-mh.sourceforge.io/book/)

A GPL-licensed book covering **mh** and **nmh**, including a bit of detail about the mailbox format.

[Subject index](INDEX.md) · [Continue](mailbox-babyl-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: MH.pack key invalidation and MH method notes](mailbox-mh-list-folders-to-mailbox-mh-pack.md) · [Preceding source contract and version conditions](mailbox-mh-list-folders-to-mailbox-mh-pack.md)
