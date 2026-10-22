# imaplib: `imaplib.Internaldate2tuple()`, `imaplib.Int2AP()`, `imaplib.ParseFlags()`, `imaplib.Time2Internaldate()`

imaplib.Internaldate2tuple(*datestr*)

Parse an IMAP4 `INTERNALDATE` string and yield the matching local time. It returns a [`time.struct_time`](https://docs.python.org/3.14/library/time.html#time.struct_time) tuple, or `None` when the string is malformed.

 imaplib.Int2AP(*num*)

Turns an integer into a bytes representation drawn from the character set [`A` .. `P`].

 imaplib.ParseFlags(*flagstr*)

Turns an IMAP4 `FLAGS` response into a tuple of separate flags.

 imaplib.Time2Internaldate(*date_time*)

Convert *date_time* into an IMAP4 `INTERNALDATE` representation. The result is a string shaped as `"DD-Mmm-YYYY HH:MM:SS +HHMM"` (double-quotes included). The *date_time* argument may be a number (int or float) giving seconds since epoch (such as what [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) returns), a 9-tuple holding local time, an instance of [`time.struct_time`](https://docs.python.org/3.14/library/time.html#time.struct_time) (such as what [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime) returns), an aware instance of [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), or a double-quoted string. For that final case, it is taken to already follow the correct format.

Keep in mind that IMAP4 message numbers shift as the mailbox shifts; specifically, once an `EXPUNGE` command carries out deletions, the surviving messages get renumbered. For that reason it is strongly recommended to rely on UIDs instead, via the UID command.

A more thorough usage example sits in a test section at the close of the module.

See also

Documentation of the protocol, along with sources for servers that implement it, gathered by the University of Washington’s IMAP Information Center, are all available at (**Source Code**) [https://github.com/uw-imap/imap](https://github.com/uw-imap/imap) (**Not Maintained**).

[Subject index](INDEX.md) · [Previous](imaplib-imap4-stream-class.md) · [Continue](imap4-append-to-imap4-getquota.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md)
