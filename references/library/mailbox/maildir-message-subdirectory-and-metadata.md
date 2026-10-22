# mailbox.MaildirMessage: `get_subdir()`, `set_subdir()`, `get_flags()`, `set_flags()`, `add_flag()`, `remove_flag()`, `get_date()`, `set_date()`, `get_info()`, `set_info()`

get_subdir()

Return either "new" (when the message ought to be kept in the `new` subdirectory) or "cur" (when the message ought to be kept in the `cur` subdirectory).

Note

A message is usually moved out of `new` into `cur` once its mailbox has been accessed, regardless of whether the message has been read. A message `msg` counts as read when `"S" in msg.get_flags()` is `True`.

 set_subdir(*subdir*)

Set the subdirectory in which the message ought to be kept. The *subdir* parameter has to be either "new" or "cur".

 get_flags()

Return a string spelling out the flags that are presently set. When the message conforms to the standard Maildir format, the result concatenates, alphabetically, zero or one appearance of each among `'D'`, `'F'`, `'P'`, `'R'`, `'S'`, and `'T'`. The empty string comes back when no flags are set or when "info" carries experimental semantics.

 set_flags(*flags*)

Set the flags specified by *flags* and unset all others.

 add_flag(*flag*)

Set the flag(s) given by *flag* while leaving other flags untouched. To tack on more than one flag at once, *flag* may be a string of several characters. The current "info" gets overwritten regardless of whether it carries experimental information rather than flags.

 remove_flag(*flag*)

Unset the flag(s) given by *flag* while leaving other flags untouched. To clear more than one flag at once, *flag* may be a string of several characters. When "info" carries experimental information rather than flags, the current "info" is left unmodified.

 get_date()

Return the message's delivery date as a floating-point number standing for seconds since the epoch.

 set_date(*date*)

Set the message's delivery date to *date*, a floating-point number standing for seconds since the epoch.

 get_info()

Return a string holding the "info" for a message. This comes in handy for reaching and altering "info" that is experimental (i.e., not a list of flags).

 set_info(*info*)

Set "info" to *info*, which ought to be a string.

When a `MaildirMessage` instance is built from an `mboxMessage` or `MMDFMessage` instance, the *Status* and *X-Status* headers are left off and these conversions occur:

| Resulting state | `mboxMessage` or `MMDFMessage` state |
| --- | --- |
| “cur” subdirectory | O flag |
| F flag | F flag |
| R flag | A flag |
| S flag | R flag |
| T flag | D flag |

When a `MaildirMessage` instance is built from an `MHMessage` instance, these conversions occur:

| Resulting state | `MHMessage` state |
| --- | --- |
| “cur” subdirectory | “unseen” sequence |
| “cur” subdirectory and S flag | no “unseen” sequence |
| F flag | “flagged” sequence |
| R flag | “replied” sequence |

When a `MaildirMessage` instance is built from a `BabylMessage` instance, these conversions occur:

| Resulting state | `BabylMessage` state |
| --- | --- |
| “cur” subdirectory | “unseen” label |
| “cur” subdirectory and S flag | no “unseen” label |
| P flag | “forwarded” or “resent” label |
| R flag | “answered” label |
| T flag | “deleted” label |

[Subject index](INDEX.md) · [Previous](mailbox-maildirmessage-class.md) · [Continue](mailbox-mboxmessage-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.MaildirMessage](mailbox-maildirmessage-class.md) · [Owning module, declaration or section: `MaildirMessage` objects](mailbox-maildirmessage-class.md)
