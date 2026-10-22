# Python 2.7 changes: Subprocess signal retries and adjacent module changes

(Contributed by Gregory P. Smith.)

The [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module will now retry its internal system calls whenever it receives an [`EINTR`](https://docs.python.org/3.14/library/errno.html#errno.EINTR) signal. (Many people reported it; Gregory P. Smith supplied the final patch in [bpo-1068268](https://bugs.python.org/issue?@action=redirect&bpo=1068268).)

- New function: [`is_declared_global()`](https://docs.python.org/3.14/library/symtable.html#symtable.Symbol.is_declared_global), part of the [`symtable`](https://docs.python.org/3.14/library/symtable.html#module-symtable) module, gives true for variables that have been explicitly declared global and false for those that are global only implicitly. (Contributed by Jeremy Hylton.)

- The [`syslog`](https://docs.python.org/3.14/library/syslog.html#module-syslog) module will now adopt the value held in `sys.argv[0]` as its identifier rather than the former default of `'python'`. (Changed by Sean Reifschneider; [bpo-8451](https://bugs.python.org/issue?@action=redirect&bpo=8451).)

- The [`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info) value has become a named tuple whose attributes are `major`, `minor`, `micro`, `releaselevel`, and `serial`. (Contributed by Ross Light; [bpo-4285](https://bugs.python.org/issue?@action=redirect&bpo=4285).)

Likewise, [`sys.getwindowsversion()`](https://docs.python.org/3.14/library/sys.html#sys.getwindowsversion) returns a named tuple, its attributes being `major`, `minor`, `build`, `platform`, `service_pack`, `service_pack_major`, `service_pack_minor`, `suite_mask`, and `product_type`. (Contributed by Brian Curtin; [bpo-7766](https://bugs.python.org/issue?@action=redirect&bpo=7766).)

- Default error handling in the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module was reworked so that fatal errors are no longer hidden. Earlier the default error level sat at 0, meaning an error did nothing more than write a line to the debug log; since that debug log stays off by default, such errors slipped by unseen. The default error level is now 1, raising an exception whenever there is an error. (Changed by Lars Gustäbel; [bpo-7357](https://bugs.python.org/issue?@action=redirect&bpo=7357).)

[`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) now lets you filter the [`TarInfo`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarInfo) objects on their way into a tar file. A call to [`add()`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile.add) may include an optional *filter* argument that is a callable. That *filter* callable receives the `TarInfo` for each file being added and is free to alter and return it. Returning `None` from the callable drops that file from the finished archive. This goes well beyond the existing *exclude* argument, which is consequently now deprecated. (Added by Lars Gustäbel; [bpo-6856](https://bugs.python.org/issue?@action=redirect&bpo=6856).) On top of that, the [`TarFile`](https://docs.python.org/3.14/library/tarfile.html#tarfile.TarFile) class now honors the context management protocol. (Added by Lars Gustäbel; [bpo-7232](https://bugs.python.org/issue?@action=redirect&bpo=7232).)

- On exit, the [`wait()`](https://docs.python.org/3.14/library/threading.html#threading.Event.wait) method of the [`threading.Event`](https://docs.python.org/3.14/library/threading.html#threading.Event) class now returns the internal flag. As a result the method will normally return true, given that `wait()` is meant to block until that internal flag turns true. The only way the return value comes back false is when a timeout was given and the operation timed out. (Contributed by Tim Lesher; [bpo-1674032](https://bugs.python.org/issue?@action=redirect&bpo=1674032).)

- To decide which characters count as numeric, whitespace, or line breaks, the interpreter now consults internally the Unicode database that the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module supplies. That database also pulls in entries drawn from the `Unihan.txt` data file (patch by Anders Chrigström and Amaury Forgeot d — Arc; [bpo-1571184](https://bugs.python.org/issue?@action=redirect&bpo=1571184)) and was refreshed to version 5.2.0 (updated by Florent Xicluna; [bpo-8024](https://bugs.python.org/issue?@action=redirect&bpo=8024)).

- The [`urlsplit()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlsplit) function in the [`urlparse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) module now deals with unfamiliar URL schemes the way [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) prescribes: when a URL takes the shape `"<something>://..."`, whatever precedes the `://` is read as the scheme, even where it is an invented scheme the module has never heard of. Code that relied on a workaround for the previous behaviour may break because of this change. As an illustration, Python 2.6.4 or 2.5 returns the following:

```pycon
>>> import urlparse
>>> urlparse.urlsplit('invented://host/filename?query')
('invented', '', '//host/filename?query', '', '')

```

Whereas Python 2.7 (and Python 2.6.5) returns:

```pycon
>>> import urlparse
>>> urlparse.urlsplit('invented://host/filename?query')
('invented', 'host', '/filename?query', '', '')

```

(The actual Python 2.7 output differs a little, because it gives back a named tuple in place of a standard tuple.)

The [`urlparse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) module additionally accepts IPv6 literal addresses laid out in [**RFC 2732**](https://datatracker.ietf.org/doc/html/rfc2732.html) (contributed by Senthil Kumaran; [bpo-2987](https://bugs.python.org/issue?@action=redirect&bpo=2987)).

```pycon
>>> urlparse.urlparse('http://[1080::8:800:200C:417A]/foo')
ParseResult(scheme='http', netloc='[1080::8:800:200C:417A]',
            path='/foo', params='', query='', fragment='')

```

- New class: the [`WeakSet`](https://docs.python.org/3.14/library/weakref.html#weakref.WeakSet) class within the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module is a set that retains only weak references to whatever it contains; an element is dropped as soon as nothing else refers to it. (First implemented for Python 3.x by Raymond Hettinger, then backported to 2.7 by Michael Foord.)

- The [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) library no longer escapes ampersands and angle brackets while emitting an XML processing instruction (something resembling `<?xml-stylesheet href="#style1"?>`) or a comment (resembling ``). (Patch by Neil Muller; [bpo-2746](https://bugs.python.org/issue?@action=redirect&bpo=2746).)

- Performance of the XML-RPC client and server, delivered through the [`xmlrpclib`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) and [`SimpleXMLRPCServer`](https://docs.python.org/3.14/library/xmlrpc.server.html#module-xmlrpc.server) modules, got better thanks to HTTP/1.1 keep-alive support and the option of gzip encoding to shrink the XML being passed around. That gzip compression is governed by the `encode_threshold` attribute of [`SimpleXMLRPCRequestHandler`](https://docs.python.org/3.14/library/xmlrpc.server.html#xmlrpc.server.SimpleXMLRPCRequestHandler), holding a size in bytes; any response bigger than that gets compressed. (Contributed by Kristján Valur Jánsson; [bpo-6267](https://bugs.python.org/issue?@action=redirect&bpo=6267).)

- The [`ZipFile`](https://docs.python.org/3.14/library/zipfile.html#zipfile.ZipFile) class in the [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) module now honors the context management protocol, letting you write `with zipfile.ZipFile(...) as f:`. (Contributed by Brian Curtin; [bpo-5511](https://bugs.python.org/issue?@action=redirect&bpo=5511).)

[`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) is also now able to archive empty directories and to extract them properly. (Fixed by Kuba Wieczorek; [bpo-4710](https://bugs.python.org/issue?@action=redirect&bpo=4710).) Pulling files back out of an archive runs faster, and alternating [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read) and [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) calls now behaves correctly. (Contributed by Nir Aides; [bpo-7610](https://bugs.python.org/issue?@action=redirect&bpo=7610).)

Beyond the path names taken in earlier versions, the [`is_zipfile()`](https://docs.python.org/3.14/library/zipfile.html#zipfile.is_zipfile) function now also accepts a file object. (Contributed by Gabriel Genellina; [bpo-4756](https://bugs.python.org/issue?@action=redirect&bpo=4756).)

[Subject index](INDEX.md) · [Previous source section](posix-identities-and-process-module-changes.md) · [Next source section](zip-compression-overrides.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](call-arguments-and-iteration-module-changes.md)
