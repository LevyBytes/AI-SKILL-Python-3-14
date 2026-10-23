# mailbox.MMDF: `get_bytes()`, `get_file()`, `lock()`, `unlock()`

get_bytes(*key*, *from_=False*)

Note: Compared with other classes, this method carries an extra parameter (*from_*). An mbox file entry's first line is the Unix "From " line. When *from_* is False, the file's first line is dropped.

 get_file(*key*, *from_=False*)

Using the file after `flush()` or `close()` has been called on the `MMDF` instance may produce unpredictable results or raise an exception.

Note: Compared with other classes, this method carries an extra parameter (*from_*). An mbox file entry's first line is the Unix "From " line. When *from_* is False, the file's first line is dropped.

 lock()

 unlock()

Three locking schemes come into play: dot locking plus, where they're available, the `flock()` and `lockf()` system calls.

See also

[mmdf man page from tin](http://www.tin.org/bin/man.cgi?section=5&topic=mmdf)

A specification of MMDF format from the documentation of tin, a newsreader.

[MMDF](https://en.wikipedia.org/wiki/MMDF)

A Wikipedia article describing the Multichannel Memorandum Distribution Facility.

[Subject index](INDEX.md) · [Previous](mailbox-mmdf-class.md) · [Continue](mailbox-message-class.md) · [Owning module, declaration or section: mailbox](mailbox-manipulate-mailboxes-in-various-formats.md) · [Owning module, declaration or section: mailbox.MMDF](mailbox-mmdf-class.md) · [Owning module, declaration or section: `MMDF` objects](mailbox-mmdf-class.md)
