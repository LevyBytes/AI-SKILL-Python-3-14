# What's New In Python 3.0 / Library Changes - array, dbm, hashlib, html, http, io, operator, pickle, profile, sys, threading, tkinter, turtle, urllib, xmlrpc

### Library Changes

Owing to limited time, this writeup makes no attempt to catalog every one of the sweeping revisions made to the standard library. The authoritative source for the headline library changes is [**PEP 3108**](https://peps.python.org/pep-3108/). What follows is a brief overview:

- A large number of legacy modules were dropped. A handful of them — `gopherlib` (which nobody used anymore) and `md5` (superseded by [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib)) — had already been marked deprecated under [**PEP 4**](https://peps.python.org/pep-0004/). Still others disappeared once support for platforms like Irix, BeOS, and Mac OS 9 was withdrawn (consult [**PEP 11**](https://peps.python.org/pep-0011/)). A further set was earmarked for deletion in Python 3.0 either because hardly anyone relied on it or because a stronger alternative had appeared. The complete roster lives in [**PEP 3108**](https://peps.python.org/pep-3108/).

- Shipping the `bsddb3` package inside the core standard library had, over the years, become an ongoing headache for the maintainers — flaky tests and Berkeley DB’s own release cadence both contributed — so it was taken out. The package itself remains healthy and is still being maintained outside the tree at [https://www.jcea.es/programacion/pybsddb.htm](https://www.jcea.es/programacion/pybsddb.htm).

- A number of modules picked up new names, whether because the former name clashed with [**PEP 8**](https://peps.python.org/pep-0008/) or on other grounds. The full mapping appears below:

| Old Name | New Name |
| --- | --- |
| _winreg | winreg |
| ConfigParser | configparser |
| copy_reg | copyreg |
| Queue | queue |
| SocketServer | socketserver |
| markupbase | _markupbase |
| repr | reprlib |
| test.test_support | test.support |

- It was customary throughout Python 2.x to ship a module as a plain-Python implementation paired with an optional speed-boosted variant written as a C extension — take [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) alongside `cPickle` as an illustration. Under that arrangement, every consumer of such a module had to handle importing the fast variant and reverting to the plain one itself. From Python 3.0 onward, the accelerated builds are regarded as internal details of their plain-Python counterparts. Code ought to simply import the ordinary name, which internally tries the fast variant first and quietly drops back to the plain one. The `pickle` / `cPickle` duo was converted this way. As for the [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile) module, that is queued up for 3.1. Meanwhile the `StringIO` module became a class housed inside the [`io`](https://docs.python.org/3.14/library/io.html#module-io) module.

- Several modules that belong together were gathered under packages, and in most cases the submodule names got shortened. Those freshly assembled packages are:

  - [`dbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm) (`anydbm`, `dbhash`, `dbm`, `dumbdbm`, `gdbm`, `whichdb`).

  - [`html`](https://docs.python.org/3.14/library/html.html#module-html) (`HTMLParser`, `htmlentitydefs`).

  - [`http`](https://docs.python.org/3.14/library/http.html#module-http) (`httplib`, `BaseHTTPServer`, `CGIHTTPServer`, `SimpleHTTPServer`, `Cookie`, `cookielib`).

  - [`tkinter`](https://docs.python.org/3.14/library/tkinter.html#module-tkinter) (every `Tkinter`-related module apart from [`turtle`](https://docs.python.org/3.14/library/turtle.html#module-turtle)). Those who reach for `turtle` generally have no interest in `tkinter`. It is also worth pointing out that starting with Python 2.6 the `turtle` feature set was substantially expanded.

  - [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib) (`urllib`, `urllib2`, `urlparse`, `robotparse`).

  - [`xmlrpc`](https://docs.python.org/3.14/library/xmlrpc.html#module-xmlrpc) (`xmlrpclib`, `DocXMLRPCServer`, `SimpleXMLRPCServer`).

A few additional adjustments to standard-library modules that fall outside [**PEP 3108**](https://peps.python.org/pep-3108/):

- Killed `sets`. Use the built-in [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set) class.

- Tidying of the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module: gone are `sys.exitfunc()`, `sys.exc_clear()`, `sys.exc_type`, `sys.exc_value`, `sys.exc_traceback`. (Keep in mind that [`sys.last_type`](https://docs.python.org/3.14/library/sys.html#sys.last_type) and the like are still present.)

- Tidying of the [`array.array`](https://docs.python.org/3.14/library/array.html#array.array) type: its `read()` and `write()` methods no longer exist; reach for [`fromfile()`](https://docs.python.org/3.14/library/array.html#array.array.fromfile) and [`tofile()`](https://docs.python.org/3.14/library/array.html#array.array.tofile) in their place. The `'c'` array typecode has likewise vanished — pick `'b'` for bytes or `'u'` for Unicode characters instead.

- Tidying of the [`operator`](https://docs.python.org/3.14/library/operator.html#module-operator) module: both `sequenceIncludes()` and `isCallable()` were taken out.

- Tidying of the `thread` module: `acquire_lock()` and `release_lock()` have been dropped — switch to [`acquire()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire) and [`release()`](https://docs.python.org/3.14/library/threading.html#threading.Lock.release).

-

Cleanup of the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module: removed the `jumpahead()` API.

- The `new` module is gone.

- The `os.tmpnam()`, `os.tempnam()`, and `os.tmpfile()` functions are gone, displaced by the [`tempfile`](https://docs.python.org/3.14/library/tempfile.html#module-tempfile) module.

- The [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module was reworked to operate on bytes. Its principal entry point has shifted to [`tokenize.tokenize()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.tokenize) in place of generate_tokens.

- `string.letters` and its companions (`string.lowercase` and `string.uppercase`) have been removed. Use [`string.ascii_letters`](https://docs.python.org/3.14/library/string.html#string.ascii_letters) and so on as replacements. (They were dropped because `string.letters` and the rest behaved in a locale-dependent way, which makes for a poor design choice in things bearing such appealingly named global “constants”.)

- The `__builtin__` module was rechristened [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins) (dropping the surrounding underscores and appending an ‘s’). The `__builtins__` name that turns up in most global namespaces stays as it was. When you want to alter a builtin, work through `builtins` and never `__builtins__`!

[Subject index](INDEX.md) · [Previous source section](changes-already-present-in-python-2-6.md) · [Release/subject declaration](common-stumbling-blocks.md) · [Next source section](pep-3101-a-new-approach-to-string-formatting.md)
