# shlex: `shlex.source`, `shlex.debug`, `shlex.lineno`, `shlex.token`, `shlex.eof`, `shlex.punctuation_chars`

`shlex.source`

Defaults to `None`. Assign a string here and that string becomes recognized as a lexical-level inclusion request, akin to the `source` keyword found in assorted shells. In practice, the token that immediately follows is opened as a filename, and input flows from that stream up to EOF, whereupon the stream's [`close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close) method fires and the input source reverts to the original input stream. You may nest source requests to any depth.

`shlex.debug`

Whenever this attribute holds a number that is `1` or greater, a `shlex` instance emits verbose progress output describing its behavior. Should you need it, the module source code spells out the specifics.

`shlex.lineno`

Source line number (one more than the count of newlines encountered so far).

`shlex.token`

The token buffer. Examining it can be handy when you are catching exceptions.

`shlex.eof`

The token that marks end of file. Outside POSIX mode it is the empty string (`''`); inside POSIX mode it is `None`.

`shlex.punctuation_chars`

A read-only property. The characters that count as punctuation. A run of punctuation characters comes back as one token. Be aware, though, that no semantic-validity check happens: '>>>', say, could be handed back as a token even when shells would not accept it as such.

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](shlex-get-token-to-shlex-instream.md) · [Continue](parsing-rules.md) · [Owning module, declaration or section: shlex](shlex-split-to-shlex-join.md) · [Owning module, declaration or section: shlex Objects](shlex-get-token-to-shlex-instream.md)
