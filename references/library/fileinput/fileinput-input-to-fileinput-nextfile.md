# fileinput: `fileinput.input()`, `fileinput.filename()`, `fileinput.fileno()`, `fileinput.lineno()`, `fileinput.filelineno()`, `fileinput.isfirstline()`, `fileinput.isstdin()`, `fileinput.nextfile()`

## fileinput - Iterate over lines from multiple input streams

### `fileinput` - Iterate over lines from multiple input streams

**Source code:** [Lib/fileinput.py](https://github.com/python/cpython/tree/3.14/Lib/fileinput.py)

---

A convenience class plus supporting functions live in this module, letting you dash off a loop across standard input or a set of files in short order. When all you need is to read or write a single file, turn instead to [`open()`](https://docs.python.org/3.14/library/functions.html#open).

The typical use is:

```python
import fileinput
for line in fileinput.input(encoding="utf-8"):
    process(line)

```

Doing so steps through the lines of every file named in `sys.argv[1:]`, and when that list is empty it falls back to `sys.stdin`. Any filename equal to `'-'` likewise becomes `sys.stdin`, with the optional `mode` and `openhook` arguments disregarded. Should you want a different set of filenames, hand it in as the first argument to `input()`. Supplying just one filename works too.

Out of the box every file opens in text mode, though you may change that by handing a `mode` parameter to the `input()` call or to `FileInput`. Whenever an I/O error crops up while a file is being opened or read, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised.

Changed in version 3.3: What once raised [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) now does so under the name [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), of which it is an alias.

Draw on `sys.stdin` more than a single time and every use past the first yields nothing — unless you are working interactively, or you have deliberately reset it (say, via `sys.stdin.seek(0)`).

An empty file gets opened and then shut again at once; you only ever notice such a file figuring in the filename list when the final file to be opened turns out to be the empty one.

Each returned line keeps whatever newline it had, so a file's final line might well come back without one.

How files get opened is yours to steer by feeding an opening hook through the `openhook` parameter of `fileinput.input()` or `FileInput()`. That hook has to be a function accepting a pair of arguments, `filename` and `mode`, and giving back a suitably opened file-like object. Whenever `encoding` and/or `errors` are supplied, they reach the hook as extra keyword arguments. For compressed files, the module ships a `hook_compressed()`.

The following function is the primary interface of this module:

 fileinput.input(*files=None*, *inplace=False*, *backup=''*, ***, *mode='r'*, *openhook=None*, *encoding=None*, *errors=None*)

Spin up a `FileInput` object. That object doubles as the shared global state behind this module's functions and is also given back for you to drive the iteration. Whatever parameters you pass here are forwarded straight to the `FileInput` class constructor.

A `FileInput` object works as a context manager inside the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Below, `input` is shut once the `with` statement finishes, exception or not:

```python
with fileinput.input(files=('spam.txt', 'eggs.txt'), encoding="utf-8") as f:
    for line in f:
        process(line)

```

Changed in version 3.2: Can be used as a context manager.

Changed in version 3.8: The `mode` and `openhook` keyword parameters became keyword-only.

Changed in version 3.10: The keyword-only `encoding` and `errors` parameters arrived.

Each of the functions below draws on the global state that `fileinput.input()` sets up; with no such state active, [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised.

 fileinput.filename()

Hand back the name of whichever file is being read at the moment. Until the first line has come in, the result is `None`.

 fileinput.fileno()

Hand back the integer “file descriptor” belonging to the active file. While nothing is open — ahead of the first line and in the gaps between files — the result is `-1`.

 fileinput.lineno()

Hand back the running line count up through the line just consumed. Until that first line arrives, the result is `0`. Once the closing line of the closing file has gone by, it reports that line's number.

 fileinput.filelineno()

Hand back the line number within the file presently open. Until the first line is read, the result is `0`. After the closing line of the closing file has gone by, it gives that line's position inside its own file.

 fileinput.isfirstline()

Give back `True` when the line just consumed opens its file, and `False` in every other case.

 fileinput.isstdin()

Give back `True` when the most recent line came out of `sys.stdin`, and `False` otherwise.

 fileinput.nextfile()

Shut the file in progress, so that on the following iteration the opening line of the next file (should one exist) is read; whatever lines you never read from the file are left out of the running total. The reported filename stays put until the next file's first line has actually been read. While no line has yet been read, calling this does nothing — it offers no way to bypass the first file. Likewise, once the closing line of the closing file is behind you, it does nothing.

[Subject index](INDEX.md) · [Continue](fileinput-close.md)
