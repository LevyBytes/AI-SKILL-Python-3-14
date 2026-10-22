# mailbox: `mailbox.MaildirMessage`

### `MaildirMessage` objects

 *class *mailbox.MaildirMessage(*message=None*)

A message carrying Maildir-specific behaviors. The *message* parameter carries the same meaning as with the `Message` constructor.

As a rule, a mail user agent application shifts every message in the `new` subdirectory into the `cur` subdirectory the first time the user opens then closes the mailbox, noting that the messages are old regardless of whether they've actually been read. Each message in `cur` gets an "info" section appended to its file name to hold information about its state. (Certain mail readers may likewise append an "info" section onto messages sitting in `new`.) The "info" section may come in one of two shapes: it may carry "2," followed by standardized flags listed out (e.g., "2,FR"), or alternatively it may carry "1," followed by so-called experimental information. Standard flags for Maildir messages run as follows:

| Flag | Meaning | Explanation |
| --- | --- | --- |
| D | Draft | Under composition |
| F | Flagged | Marked as important |
| P | Passed | Forwarded, resent, or bounced |
| R | Replied | Replied to |
| S | Seen | Read |
| T | Trashed | Marked for subsequent deletion |

`MaildirMessage` instances supply the following methods:

[Subject index](INDEX.md) · [Previous](mailbox-message-class.md) · [Continue](maildir-message-subdirectory-and-metadata.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md)
