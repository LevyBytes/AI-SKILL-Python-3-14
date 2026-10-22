# mailbox.Maildir: `list_folders()`, `get_folder()`, `add_folder()`, `remove_folder()`, `clean()`, `get_flags()`, `set_flags()`, `add_flag()`, `remove_flag()`

colon

The Maildir specification calls for a colon (`':'`) within certain message file names. Some operating systems, however, forbid this character in file names. To run a Maildir-like format on one of those operating systems, you'll need to pick a different character to stand in for it. The exclamation point (`'!'`) is a popular choice. For example:

```python
import mailbox
mailbox.Maildir.colon = '!'

```

The `colon` attribute can also be set per instance.

Changed in version 3.13: `Maildir` now ignores files with a leading dot.

`Maildir` instances carry all the methods of `Mailbox` plus the following:

 list_folders()

Return a list of the names of all folders.

 get_folder(*folder*)

Return a `Maildir` instance standing for the folder whose name is *folder*. A `NoSuchMailboxError` exception is raised should the folder not exist.

 add_folder(*folder*)

Create a folder whose name is *folder* and return a `Maildir` instance standing for it.

 remove_folder(*folder*)

Delete the folder whose name is *folder*. Should the folder hold any messages, a `NotEmptyError` exception will be raised and the folder won't be deleted.

 clean()

Delete temporary files from the mailbox that have gone untouched over the last 36 hours. The Maildir specification states that mail-reading programs ought to do this from time to time.

 get_flags(*key*)

Return as a string the flags set on the message corresponding to *key*. This matches `get_message(key).get_flags()` but runs much faster, since it doesn't open the message file. Reach for this method while iterating over the keys to figure out which messages are worth fetching.

Where a `MaildirMessage` object is on hand, reach for its `get_flags()` method instead, since edits applied via the message's `set_flags()`, `add_flag()` and `remove_flag()` methods won't appear here until the mailbox's `__setitem__()` method has run.

Added in version 3.13.

 set_flags(*key*, *flags*)

For the message that *key* maps to, set the flags specified by *flags* and unset all others. Invoking `some_mailbox.set_flags(key, flags)` resembles

```python
one_message = some_mailbox.get_message(key)
one_message.set_flags(flags)
some_mailbox[key] = one_message

```

but faster, since it doesn't open the message file.

When you do hold a `MaildirMessage` object, use its `set_flags()` method instead, because changes made through this mailbox method won't be visible to the message object's method, `get_flags()`.

Added in version 3.13.

 add_flag(*key*, *flag*)

On the message corresponding to *key*, set the flags specified by *flag* while leaving other flags untouched. To tack on more than one flag at once, *flag* may be a string of several characters.

The considerations weighing this method against the message object's `add_flag()` method mirror those for `set_flags()`; consult the discussion there.

Added in version 3.13.

 remove_flag(*key*, *flag*)

On the message corresponding to *key*, unset the flags specified by *flag* while leaving other flags untouched. To clear more than one flag at once, *flag* may be a string of several characters.

The considerations weighing this method against the message object's `remove_flag()` method mirror those for `set_flags()`; consult the discussion there.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](mailbox-maildir-class.md) · [Continue](mailbox-maildir-get-info-to-mailbox-maildir-get-file.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.Maildir](mailbox-maildir-class.md) · [Owning module, declaration or section: `Maildir` objects](mailbox-maildir-class.md)
