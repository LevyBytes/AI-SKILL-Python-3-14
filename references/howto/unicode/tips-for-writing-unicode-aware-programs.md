# Tips for Writing Unicode-aware Programs

### Tips for Writing Unicode-aware Programs

Here are a few pointers for building software that handles Unicode.

The single most important pointer:

>

Internally a program should deal solely in Unicode strings, decoding incoming data at the earliest opportunity and encoding outgoing data only at the very end.

Should you try writing processing functions that take Unicode strings as well as byte strings, your code becomes prone to bugs anywhere the two kinds of strings get mixed. Nothing encodes or decodes for you automatically: write `str + bytes`, for example, and a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

With data arriving from a web browser or another untrusted origin, one frequent practice is to scan a string for forbidden characters before it goes into a generated command line or gets saved to a database. When you do that, take care to inspect the decoded string and not the encoded bytes; certain encodings carry quirky traits, like failing to be bijective or not being wholly ASCII-compatible. That matters all the more when the input data carries its own encoding, since an attacker can then pick a sneaky route to bury malicious text inside the encoded bytestream.

[Subject index](INDEX.md) · [Previous source context](unicode-filenames.md) · [Following source context](converting-between-file-encodings.md)
