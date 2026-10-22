# sqlite3: `sqlite3.Blob`

### Blob objects

 *class *sqlite3.Blob

Added in version 3.11.

A `Blob` instance is a [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) capable of reading and writing data within an SQLite BLOB. Invoke [`len(blob)`](https://docs.python.org/3.14/library/functions.html#len) to learn the blob's size in bytes. Reach the blob data directly through indices and [slices](https://docs.python.org/3.14/glossary.html#term-slice).

Treat the `Blob` as a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) so its blob handle gets closed once you are finished.

```python
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE test(blob_col blob)")
con.execute("INSERT INTO test(blob_col) VALUES(zeroblob(13))")

# Write to our blob, using two write operations:
with con.blobopen("test", "blob_col", 1) as blob:
    blob.write(b"hello, ")
    blob.write(b"world.")
    # Modify the first and last bytes of our blob
    blob[0] = ord("H")
    blob[-1] = ord("!")

# Read the contents of our blob
with con.blobopen("test", "blob_col", 1) as blob:
    greeting = blob.read()

print(greeting)  # outputs "b'Hello, world!'"
con.close()

```

[Subject index](INDEX.md) · [Previous](sqlite3-row-keys.md) · [Continue](sqlite3-blob-close-to-sqlite3-blob-seek.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
