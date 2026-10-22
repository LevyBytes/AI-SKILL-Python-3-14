# mailbox.mbox: `get_bytes()`, `get_file()`, `get_string()`, `lock()`, `unlock()`

get_bytes(*key*, *from_=False*)

Note: Unlike other classes, this method takes an extra parameter (*from_*). An mbox file entry's opening line is the Unix "From " line. When *from_* is False, that opening line of the file is dropped.

 get_file(*key*, *from_=False*)

Using the file once `flush()` or `close()` has been called on the `mbox` instance may produce unpredictable results or raise an exception.

Note: Unlike other classes, this method takes an extra parameter (*from_*). An mbox file entry's opening line is the Unix "From " line. When *from_* is False, that opening line of the file is dropped.

 get_string(*key*, *from_=False*)

Note: Unlike other classes, this method takes an extra parameter (*from_*). An mbox file entry's opening line is the Unix "From " line. When *from_* is False, that opening line of the file is dropped.

 lock()

 unlock()

Three locking schemes come into play—dot locking plus, where they're available, the `flock()` and `lockf()` system calls.

See also

[mbox man page from tin](http://www.tin.org/bin/man.cgi?section=5&topic=mbox)

A specification of the format, with details on locking.

[Configuring Netscape Mail on Unix: Why The Content-Length Format is Bad](https://www.jwz.org/doc/content-length.html)

An argument for using the original mbox format rather than a variation.

[“mbox” is a family of several mutually incompatible mailbox formats](https://www.loc.gov/preservation/digital/formats/fdd/fdd000383.shtml)

A history of mbox variations.

[Subject index](INDEX.md) · [Previous](mailbox-mbox-class.md) · [Continue](mailbox-mh-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.mbox](mailbox-mbox-class.md) · [Owning module, declaration or section: `mbox` objects](mailbox-mbox-class.md)
