# Reading and Writing Unicode Data

### Reading and Writing Unicode Data

After you’ve written some code that operates on Unicode data, the next hurdle is input/output. How are Unicode strings brought into your program, and how is Unicode turned into a form fit for storage or transmission?

Depending on where your input comes from and where your output goes, you might not have to do anything at all; check whether the libraries your application uses support Unicode natively. XML parsers, for one, often return Unicode data. Plenty of relational databases likewise support Unicode-valued columns and can return Unicode values out of an SQL query.

Before Unicode data is written to disk or pushed across a socket, it is normally converted into a specific encoding. Handling all of it yourself is possible: crack open a file, pull an 8-bit bytes object out of it, then run those bytes through `bytes.decode(encoding)`. The manual route, however, is discouraged.

The multi-byte character of encodings poses one issue; a single Unicode character may be represented by several bytes. Should you want to read the file in arbitrarily sized chunks (say, 1024 or 4096 bytes), you have to write error-handling code that catches the case where only part of the bytes encoding one Unicode character get read at a chunk’s end. One workaround is to pull the whole file into memory and then decode it, but that bars you from handling files that are extremely large; reading a 2 GiB file would demand 2 GiB of RAM. (Actually more, since for at least a brief moment you would have both the encoded string and its Unicode form held in memory.)

[Subject index](INDEX.md) · [Following source continuation](reading-and-writing-unicode-data-continuation.md) · [Previous source context](references.md)
