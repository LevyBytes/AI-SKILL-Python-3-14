# Reading and Writing Unicode Data continuation

One fix is to reach for the low-level decoding interface so that partial coding sequences get handled. That implementation, though, is already provided for you: the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function hands back a file-like object that treats the file’s bytes as being in a given encoding and takes Unicode arguments in methods like [`read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read) and [`write()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.write). It operates via the *encoding* and *errors* parameters of `open()`, which carry the same meaning they have in [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode) and [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode).

Pulling Unicode out of a file is thus straightforward:

```python
with open('unicode.txt', encoding='utf-8') as f:
    for line in f:
        print(repr(line))

```

You can likewise open a file in update mode, which permits reading and writing together:

```python
with open('test', encoding='utf-8', mode='w+') as f:
    f.write('\u4500 blah blah blah\n')
    f.seek(0)
    print(repr(f.readline()[:1]))

```

Serving as a byte-order mark (BOM), the Unicode character `U+FEFF` is frequently placed as a file’s opening character to help software auto-detect that file’s byte ordering. Certain encodings, UTF-16 among them, count on a BOM sitting at a file’s start; with such an encoding the BOM is written automatically as the leading character and then quietly discarded on read. These encodings also have variants — for the little-endian case ‘utf-16-le’, and ‘utf-16-be’ in the big-endian case — that nail down a single byte ordering and leave the BOM in place.

There are settings where placing a “BOM” at the front of UTF-8 files is the norm too; that label misleads, because UTF-8 carries no byte-order dependence. All the mark does is signal that UTF-8 encodes the file. When reading files like these, reach for the ‘utf-8-sig’ codec, which strips the mark automatically should one be there.

[Subject index](INDEX.md) · [Previous source owning section](reading-and-writing-unicode-data.md) · [Following source context](unicode-filenames.md)
