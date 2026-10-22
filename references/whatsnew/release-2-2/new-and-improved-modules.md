# What’s New in Python 2.2 / New and Improved Modules — hmac, os, pydoc, re, socket, struct, time, xmlrpc.client, xmlrpc.server

### New and Improved Modules

- Fredrik Lundh donated the [`xmlrpclib`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) module to the standard library, supplying the means to write XML-RPC clients. XML-RPC is a lightweight remote procedure call protocol layered over HTTP and XML. As an illustration, the snippet below pulls a roster of RSS channels from the O’Reilly Network and then prints the latest headlines for a single channel:

```python
import xmlrpclib
s = xmlrpclib.Server(
      'http://www.oreillynet.com/meerkat/xml-rpc/server.php')
channels = s.meerkat.getChannels()
# channels is a list of dictionaries, like this:
# [{'id': 4, 'title': 'Freshmeat Daily News'}
#  {'id': 190, 'title': '32Bits Online'},
#  {'id': 4549, 'title': '3DGamers'}, ... ]

# Get the items for one channel
items = s.meerkat.getItems( {'channel': 4} )

# 'items' is another list of dictionaries, like this:
# [{'link': 'http://freshmeat.net/releases/52719/',
#   'description': 'A utility which converts HTML to XSL FO.',
#   'title': 'html2fo 0.3 (Default)'}, ... ]

```

Building plain XML-RPC servers is straightforward with the [`SimpleXMLRPCServer`](https://docs.python.org/3.14/library/xmlrpc.server.html#module-xmlrpc.server) module. Head to [http://xmlrpc.scripting.com/](http://xmlrpc.scripting.com/) for further detail on XML-RPC.

- The fresh [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) module carries out the HMAC algorithm laid out in [**RFC 2104**](https://datatracker.ietf.org/doc/html/rfc2104.html). (Contributed by Gerhard Häring.)

- A number of functions that used to hand back long tuples now return pseudo-sequences which still act like tuples yet additionally expose mnemonic attributes such as `memberst_mtime` or [`tm_year`](https://docs.python.org/3.14/library/time.html#time.struct_time.tm_year). Among the upgraded functions are [`stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`fstat()`](https://docs.python.org/3.14/library/os.html#os.fstat), [`statvfs()`](https://docs.python.org/3.14/library/os.html#os.statvfs), and [`fstatvfs()`](https://docs.python.org/3.14/library/os.html#os.fstatvfs) within the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module, plus [`localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime), [`gmtime()`](https://docs.python.org/3.14/library/time.html#time.gmtime), and [`strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) inside the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module.

To take an example, fetching a file’s size through the old tuples meant writing something along the lines of `file_size = os.stat(filename)[stat.ST_SIZE]`, whereas this now reads more plainly as `file_size = os.stat(filename).st_size`.

Nick Mathewson supplied the original patch behind this feature.

- The Python profiler underwent a thorough overhaul, and a range of mistakes in what it printed have been put right. (Contributed by Fred L. Drake, Jr. and Tim Peters.)

- IPv6 support can be compiled into the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module: pass `--enable-ipv6` when running Python’s configure script. (Contributed by Jun-ichiro “itojun” Hagino.)

- The [`struct`](https://docs.python.org/3.14/library/struct.html#module-struct) module gained two fresh format characters for 64-bit integers on platforms offering the C long long type. `q` denotes a signed 64-bit integer, while `Q` denotes an unsigned one. The result comes back as Python’s long integer type. (Contributed by Tim Peters.)

- Within the interpreter’s interactive mode, a fresh built-in function [`help()`](https://docs.python.org/3.14/library/functions.html#help) now draws on the [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) module that arrived in Python 2.1 to offer interactive help. `help(object)` shows whatever help text exists for *object*. Calling `help()` with no argument drops you into an online help utility, where typing the names of functions, classes, or modules surfaces the relevant documentation. (Contributed by Guido van Rossum, drawing on the `pydoc` module from Ka-Ping Yee.)

- The SRE engine beneath the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module has received assorted bug fixes and speed gains. The [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) and [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split) functions, for instance, were rewritten in C. A further donated patch makes some Unicode character ranges run twice as fast, and a new [`finditer()`](https://docs.python.org/3.14/library/re.html#re.finditer) method yields an iterator across every non-overlapping match within a supplied string. (Fredrik Lundh maintains SRE. Martin von Löwis contributed the BIGCHARSET patch.)

-

[`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib) has gained backing for [**RFC 2487**](https://datatracker.ietf.org/doc/html/rfc2487.html), “Secure SMTP over TLS”, which means you can now scramble the SMTP exchange running between a Python program and the mail transport agent receiving a message. On top of that, `smtplib` handles SMTP authentication. (Contributed by Gerhard Häring.)

- Kept up by Piers Lauder, the [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) module now understands a handful of fresh extensions: the NAMESPACE extension laid out in [**RFC 2342**](https://datatracker.ietf.org/doc/html/rfc2342.html), plus SORT, GETACL and SETACL. (Contributed by Anthony Baxter and Michel Pelletier.)

- How the `rfc822` module reads email addresses now lines up with [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html), itself a revision of [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html). (Rest assured the module's name is *not* being renamed to `rfc2822`.) Alongside this, a new package, [`email`](https://docs.python.org/3.14/library/email.html#module-email), has joined the library for reading and building e-mail messages. (Contributed by Barry Warsaw, an offshoot of the work he did on Mailman.)

- A new `Differ` class now lives in the [`difflib`](https://docs.python.org/3.14/library/difflib.html#module-difflib) module, built to turn out human-readable change listings (a “delta”) between two sequences of text lines. The module also gains two generator functions, `ndiff()` and `restore()`: the first yields a delta given two sequences, the second recovers one of the source sequences from a delta. (The grunt work came from David Goodger, building on ndiff.py code by Tim Peters, who afterward handled the generatorization.)

- The [`string`](https://docs.python.org/3.14/library/string.html#module-string) module picked up the new constants `ascii_letters`, `ascii_lowercase`, and `ascii_uppercase`. A number of standard-library modules had been leaning on `string.letters` as a stand-in for the A-Za-z ranges, yet that assumption breaks down once locales come into play, since `string.letters` shifts with whichever legal-character set the active locale defines. Every one of those broken modules has since been corrected to rely on `ascii_letters`. (Reported by an unknown person; fixed by Fred L. Drake, Jr.)

- By adding a [`MimeTypes`](https://docs.python.org/3.14/library/mimetypes.html#mimetypes.MimeTypes) class that accepts a list of filenames to parse, the [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes) module makes working with alternative MIME-type databases simpler. (Contributed by Fred L. Drake, Jr.)

- The [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module gained a [`Timer`](https://docs.python.org/3.14/library/threading.html#threading.Timer) class, letting you arrange for some activity to fire at a later moment. (Contributed by Itamar Shtull-Trauring.)

[Subject index](INDEX.md) · [Previous source section](pep-227-nested-scopes.md) · [Release/subject declaration](introduction.md) · [Next source section](interpreter-changes-and-fixes.md)
