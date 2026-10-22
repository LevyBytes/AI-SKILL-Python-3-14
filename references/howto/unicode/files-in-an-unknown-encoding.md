# Files in an Unknown Encoding

#### Files in an Unknown Encoding

Suppose you must edit a file yet have no idea what its encoding is — what then? Provided you're confident the encoding is ASCII-compatible and you intend only to look at or change the ASCII portions, you can open the file using the `surrogateescape` error handler:

```python
with open(fname, 'r', encoding="ascii", errors="surrogateescape") as f:
    data = f.read()

# make changes to the string 'data'

with open(fname + '.new', 'w',
          encoding="ascii", errors="surrogateescape") as f:
    f.write(data)

```

Any non-ASCII bytes get decoded by the `surrogateescape` error handler into code points within a dedicated range stretching from U+DC80 to U+DCFF. Those very code points convert back into the identical bytes once the `surrogateescape` error handler encodes the data and writes it out again.

[Subject index](INDEX.md) · [Previous source context](converting-between-file-encodings.md) · [Following source context](references.md)
