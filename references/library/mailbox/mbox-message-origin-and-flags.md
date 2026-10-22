# mailbox.mboxMessage: mboxMessage flag access and mutation

get_from()

Return a string standing for the "From " line that marks a message's start within an mbox mailbox. The leading "From " and the trailing newline are left out.

 set_from(*from_*, *time_=None*)

Set the "From " line to *from_*, which ought to be given without a leading "From " or trailing newline. As a convenience, *time_* may be given and will be formatted suitably then appended to *from_*. When *time_* is given, it ought to be a [`time.struct_time`](https://docs.python.org/3.14/library/time.html#time.struct_time) instance, a tuple fit for passing to [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime), or `True` (to use [`time.gmtime()`](https://docs.python.org/3.14/library/time.html#time.gmtime)).

 get_flags()

Return a string spelling out the flags that are presently set. When the message conforms to the conventional format, the result concatenates, in this order, zero or one appearance of each among `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

 set_flags(*flags*)

Set the flags specified by *flags* and unset all others. The *flags* parameter ought to concatenate, in whatever order, zero or more appearances of each among `'R'`, `'O'`, `'D'`, `'F'`, and `'A'`.

 add_flag(*flag*)

Set the flag(s) given by *flag* while leaving other flags untouched. To tack on more than one flag at once, *flag* may be a string of several characters.

 remove_flag(*flag*)

Unset the flag(s) given by *flag* while leaving other flags untouched. To clear more than one flag at once, *flag* may be a string of several characters.

When an `mboxMessage` instance is built from a `MaildirMessage` instance, a "From " line is produced from the `MaildirMessage` instance's delivery date, and these conversions occur:

| Resulting state | `MaildirMessage` state |
| --- | --- |
| R flag | S flag |
| O flag | “cur” subdirectory |
| D flag | T flag |
| F flag | F flag |
| A flag | R flag |

When an `mboxMessage` instance is built from an `MHMessage` instance, these conversions occur:

| Resulting state | `MHMessage` state |
| --- | --- |
| R flag and O flag | no “unseen” sequence |
| O flag | “unseen” sequence |
| F flag | “flagged” sequence |
| A flag | “replied” sequence |

When an `mboxMessage` instance is built from a `BabylMessage` instance, these conversions occur:

| Resulting state | `BabylMessage` state |
| --- | --- |
| R flag and O flag | no “unseen” label |
| O flag | “unseen” label |
| D flag | “deleted” label |
| A flag | “answered” label |

When a `mboxMessage` instance is built from an `MMDFMessage` instance, the "From " line is copied and every flag corresponds directly:

| Resulting state | `MMDFMessage` state |
| --- | --- |
| R flag | R flag |
| O flag | O flag |
| D flag | D flag |
| F flag | F flag |
| A flag | A flag |

[Subject index](INDEX.md) · [Previous](mailbox-mboxmessage-class.md) · [Continue](mailbox-mhmessage-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.mboxMessage](mailbox-mboxmessage-class.md) · [Owning module, declaration or section: `mboxMessage` objects](mailbox-mboxmessage-class.md)
