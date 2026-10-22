# shlex: `shlex.shlex`

`*class *shlex.shlex(*instream=None*, *infile=None*, *posix=False*, *punctuation_chars=False*)`

Any `shlex` instance — or an instance of a subclass — is a lexical analyzer object. Should the initialization argument be supplied, it names the source from which characters are read. That source has to be either a string or a file-/stream-like object exposing [`read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read) and [`readline()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.readline) methods. When nothing is passed, the input comes from `sys.stdin`. A second, optional argument is a filename string that seeds the starting value of the `infile` attribute. Should the *instream* argument be left out or match `sys.stdin`, that second argument falls back to “stdin”. The mode of operation is governed by the *posix* argument: while *posix* stays untrue (the default), the `shlex` instance runs in compatibility mode; once POSIX mode is active, `shlex` aims to match the POSIX shell parsing rules as closely as it can. To bring the behaviour still nearer to how actual shells parse, use the *punctuation_chars* argument, which accepts several possibilities. Its default, `False`, keeps the behaviour from Python 3.5 and before. Switching it to `True` alters how the characters `();<>|&` are parsed: each run of them (treated as punctuation characters) comes back as one token. Hand it a non-empty character string instead and those characters serve as the punctuation set. Whatever characters in the `wordchars` attribute also occur in *punctuation_chars* get dropped from `wordchars`. Consult Improved Compatibility with Shells for further detail. You may only assign *punctuation_chars* when the `shlex` instance is created; it can't be changed afterward.

Changed in version 3.6: The *punctuation_chars* parameter was added.

See also

Module [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser)

Parser for configuration files similar to the Windows `.ini` files.

[Subject index](INDEX.md) · [Previous](shlex-quote.md) · [Continue](shlex-get-token-to-shlex-instream.md) · [Owning module, declaration or section: shlex](shlex-split-to-shlex-join.md)
