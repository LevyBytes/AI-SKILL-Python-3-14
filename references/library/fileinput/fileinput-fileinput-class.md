# fileinput: `fileinput.FileInput`

*class *fileinput.FileInput(*files=None*, *inplace=False*, *backup=''*, ***, *mode='r'*, *openhook=None*, *encoding=None*, *errors=None*)

The actual implementation is the `FileInput` class; its `filename()`, `fileno()`, `lineno()`, `filelineno()`, `isfirstline()`, `isstdin()`, `nextfile()`, and `close()` methods line up with the like-named module functions. On top of that it is [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) and carries a [`readline()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.readline) method that yields the following input line. You have to step through the sequence in strict order; mixing random access with `readline()` is not allowed.

The `mode` argument lets you dictate the file mode forwarded to [`open()`](https://docs.python.org/3.14/library/functions.html#open). Its value has to be either `'r'` or `'rb'`.

If you supply an `openhook`, it has to be a function accepting two arguments — `filename` and `mode` — and returning a file-like object opened to match. The `inplace` and `openhook` options cannot be combined.

You are free to give `encoding` and `errors`, which then travel on to [`open()`](https://docs.python.org/3.14/library/functions.html#open) or to `openhook`.

Likewise, a `FileInput` object serves as a context manager within a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. In the snippet here, `input` is closed the moment the `with` block ends, whether or not an exception is thrown:

```python
with FileInput(files=('spam.txt', 'eggs.txt')) as input:
    process(input)

```

Changed in version 3.2: Can be used as a context manager.

Changed in version 3.8: The `mode` and `openhook` keyword parameters turned keyword-only.

Changed in version 3.10: Gained the keyword-only `encoding` and `errors` parameters.

Changed in version 3.11: Both the `'rU'` and `'U'` modes, plus the `__getitem__()` method, were taken out.

**Optional in-place filtering:** when the keyword argument `inplace=True` reaches `fileinput.input()` or the `FileInput` constructor, the file is shifted aside into a backup and standard output is steered toward the original input file (and if something already bears the backup file's name, it is overwritten without a word). That is what lets you build a filter that rewrites its own input file on the spot. Supplying the `backup` parameter (usually written `backup='.<some extension>'`) sets the backup file's extension and keeps that backup around; absent it, the extension defaults to `'.bak'` and the backup is removed once the output file closes. Reading from standard input switches in-place filtering off.

This module supplies the two opening hooks below:

[Subject index](INDEX.md) · [Previous](fileinput-close.md) · [Continue](fileinput-hook-compressed-to-fileinput-hook-encoded.md) · [Owning module, declaration or section: fileinput](fileinput-input-to-fileinput-nextfile.md)
