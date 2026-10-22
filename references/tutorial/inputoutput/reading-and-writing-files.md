# 7.2. Reading and Writing Files

### 7.2. Reading and Writing Files

A call to [`open()`](https://docs.python.org/3.14/library/functions.html#open) gives back a [file object](https://docs.python.org/3.14/glossary.html#term-file-object); in the usual case you invoke it with two positional arguments plus one keyword argument: `open(filename, mode, encoding=None)`

```python
>>> f = open('workfile', 'w', encoding="utf-8")

```

For the first argument you pass a string holding the filename. The second argument is a further string whose handful of characters spell out how the file is to be used. *mode* may be `'r'` if the file is to be read only, `'w'` for writing alone (any existing file bearing the same name gets wiped), and `'a'` opens it for appending, so whatever you write lands at the end automatically. `'r+'` opens the file for reading and writing both. Supplying the *mode* argument is optional; leave it off and `'r'` is taken as the default.

By default a file opens in *text mode*, meaning you read and write strings to and from it that are encoded under a particular *encoding*. Leave *encoding* unspecified and the default hinges on the platform (refer to [`open()`](https://docs.python.org/3.14/library/functions.html#open)). Since UTF-8 has become the de-facto standard nowadays, `encoding="utf-8"` is the advised choice unless you're aware you require some other encoding. Tacking a `'b'` onto the mode opens the file in *binary mode*, where data is read and written as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects. Opening a file in binary mode rules out specifying *encoding*.

Under text mode, reading by default folds platform-specific line endings (`\n` on Unix, `\r\n` on Windows) down to a plain `\n`. Writing in text mode by default does the reverse, turning each `\n` back into the platform-specific line ending. That hidden reworking of file data suits text files but wrecks binary data such as what sits in `JPEG` or `EXE` files. Take great care to switch to binary mode when reading and writing files of that kind.

Reaching for the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) keyword whenever you handle file objects is sound practice. Its benefit is that the file is closed correctly once its suite wraps up, even should an exception fire somewhere along the way. Leaning on `with` also runs far shorter than spelling out the equivalent [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)-[`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) blocks:

```python
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True

```

When you aren't relying on the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) keyword, you ought to invoke `f.close()` so the file shuts and any system resources it was holding are released at once.

Warning

Invoking `f.write()` while neither using the `with` keyword nor invoking `f.close()` **might** leave the arguments you gave `f.write()` only partly flushed to disk, even when the program finishes without error.

Once a file object has been closed, whether through a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement or via a `f.close()` call, any further attempt to use that file object fails automatically.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.

```

[Subject index](INDEX.md) · [Previous source section](old-string-formatting.md) · [Following source section](methods-of-file-objects.md)
