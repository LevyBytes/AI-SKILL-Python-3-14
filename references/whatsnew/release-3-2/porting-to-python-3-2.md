# What's New In Python 3.2 / Porting to Python 3.2 — array, configparser, random, string

### Porting to Python 3.2

Gathered here are the already-mentioned changes plus further bugfixes that might oblige you to adjust your code:

- The [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) module received several tidy-ups. Chief among them is swapping the aging `ConfigParser` class for the long-favored `SafeConfigParser`. Beyond that, a few lesser incompatibilities crept in:

  - Both [`get()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.get) and [`set()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.set) operations now check the interpolation syntax. Under the default interpolation scheme, exactly two percent-sign tokens pass muster: `%(name)s` and `%%`, where the second stands for an escaped percent sign.

  - The [`set()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.set) and [`add_section()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.add_section) methods now confirm that the values handed in are genuine strings. In the past, unsupported types could slip in by accident.

  - Repeated sections or options coming from one source now trigger either [`DuplicateSectionError`](https://docs.python.org/3.14/library/configparser.html#configparser.DuplicateSectionError) or [`DuplicateOptionError`](https://docs.python.org/3.14/library/configparser.html#configparser.DuplicateOptionError). Previously, a duplicate just quietly clobbered whatever came before it.

  - With inline comments off by default these days, the **;** character is safe to put inside values.

  - Indentation is now permitted on comments. Because of that, getting a **;** or **#** to sit at the head of a line within multiline values requires interpolating it. Doing so stops comment-prefix characters embedded in values from being read as comments.

  - These days `""` counts as a legitimate value rather than being turned into an empty string on its own. When you do want an empty string, write `"option ="` on the line.

- A thorough overhaul of the `nntplib` module leaves its APIs frequently at odds with the 3.1 APIs.

- You can no longer hand [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects in as filenames; convert them to [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) first.

- For the sake of clarity, `array.tostring()` and `array.fromstring()` now go by [`array.tobytes()`](https://docs.python.org/3.14/library/array.html#array.array.tobytes) and [`array.frombytes()`](https://docs.python.org/3.14/library/array.html#array.array.frombytes). Their former names are deprecated. (See [bpo-8990](https://bugs.python.org/issue?@action=redirect&bpo=8990).)

- `PyArg_Parse*()` functions:

  - “t#” format has been removed: use “s#” or “s*” instead

  - “w” and “w#” formats has been removed: use “w*” instead

- The `PyCObject` type, which 3.1 had deprecated, is now gone. For enclosing opaque C pointers in Python objects, reach for the [`PyCapsule`](https://docs.python.org/3.14/c-api/capsule.html#c.PyCapsule) API in its place; that newer type sports a clear interface for conveying typing-safety details together with a simpler destructor-calling signature.

- Owing to a defective design, the `sys.setfilesystemencoding()` function has been taken out.

- Both the [`random.seed()`](https://docs.python.org/3.14/library/random.html#random.seed) function and method now run string seeds through an sha512 hash function for salting. Should you want the earlier *seed* behavior so as to recreate Python 3.1 sequences, give the *version* argument the value *1*, as in `random.seed(s, version=1)`.

- The `string.maketrans()` function, already deprecated earlier, is gone, supplanted by the static methods [`bytes.maketrans()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.maketrans) and [`bytearray.maketrans()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.maketrans). The move clears up the muddle over which types the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module actually handled. Today [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) carry their own **maketrans** and **translate** methods, each working through an intermediate translation table of the fitting type.

(Contributed by Georg Brandl; [bpo-5675](https://bugs.python.org/issue?@action=redirect&bpo=5675).)

- The `contextlib.nested()` function, deprecated before this, is gone now in favor of an ordinary [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement capable of taking several context managers at once. That route runs quicker thanks to being built in, and it finalizes a group of context managers more gracefully when one of them throws an exception:

```python
with open('mylog.txt') as infile, open('a.out', 'w') as outfile:
    for line in infile:
        if '<critical>' in line:
            outfile.write(line)

```

(Contributed by Georg Brandl and Mattias Brändström; [appspot issue 53094](https://codereview.appspot.com/53094).)

- For the `s` string pack code, [`struct.pack()`](https://docs.python.org/3.14/library/struct.html#struct.pack) now insists on bytes alone. It used to take text arguments and silently encode them to bytes via UTF-8. That caused trouble, since it presumed a particular encoding was right and since a variable-length encoding may break when it has to fill a fixed-length slot inside a structure.

Something like `struct.pack('<6sHHBBB', 'GIF87a', x, y)` needs reworking so it passes bytes rather than text: `struct.pack('<6sHHBBB', b'GIF87a', x, y)`.

(Discovered by David Beazley and fixed by Victor Stinner; [bpo-10783](https://bugs.python.org/issue?@action=redirect&bpo=10783).)

- On a failed parse, the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) class now throws an [`xml.etree.ElementTree.ParseError`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ParseError). What it threw before was an [`xml.parsers.expat.ExpatError`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.ExpatError).

- Because [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) yields a new, lengthier representation for floats, doctests pinned to the former output format may stop passing.

- Within [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen), *close_fds* now defaults to `True` on Unix; on Windows it defaults to `True` when the three standard streams are all `None` and to `False` otherwise. Its old default was always `False`, a setting that bred hard-to-track bugs and race conditions as open file descriptors leaked through into the child process.

- Both [`urllib.request`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.request) and [`http.client`](https://docs.python.org/3.14/library/http.client.html#module-http.client) have dropped their handling of the old HTTP 0.9. The server end keeps it, though (over in [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server)).

(Contributed by Antoine Pitrou, [bpo-10711](https://bugs.python.org/issue?@action=redirect&bpo=10711).)

- When an SSL socket in timeout mode actually times out, it now throws [`socket.timeout`](https://docs.python.org/3.14/library/socket.html#socket.timeout) in place of a generic [`SSLError`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLError).

(Contributed by Antoine Pitrou, [bpo-10272](https://bugs.python.org/issue?@action=redirect&bpo=10272).)

- The deceptive functions `PyEval_AcquireLock()` and `PyEval_ReleaseLock()` are now formally deprecated. Lean on the thread-state aware APIs instead, [`PyEval_SaveThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_SaveThread) and [`PyEval_RestoreThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_RestoreThread) among them.

- On account of security hazards, `asyncore.handle_accept()` is now deprecated, with a fresh function `asyncore.handle_accepted()` introduced to take over from it.

(Contributed by Giampaolo Rodola in [bpo-6706](https://bugs.python.org/issue?@action=redirect&bpo=6706).)

- With the reworked [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) implementation in place, you can no longer invoke `PyEval_InitThreads()` ahead of [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize).

[Subject index](INDEX.md) · [Previous source section](build-and-c-api-changes.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
