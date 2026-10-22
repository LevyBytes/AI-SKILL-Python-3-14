# What's New In Python 3.9 / Removed — array, base64, bz2, json, math, plistlib, sys, threading, typing, wave, xml.etree.elementtree

### Removed

- The bogus version string at `unittest.mock.__version__` is gone.

- `nntplib.NNTP`: the `xpath()` and `xgtitle()` methods are gone. Both had been deprecated as far back as Python 3.3. As a rule, NNTP server administrators either do not support or do not enable these extensions. As a replacement for `xgtitle()`, turn to `nntplib.NNTP.descriptions()` or `nntplib.NNTP.description()`. (Contributed by Donghee Na in [bpo-39366](https://bugs.python.org/issue?@action=redirect&bpo=39366).)

- [`array.array`](https://docs.python.org/3.14/library/array.html#array.array): the `tostring()` and `fromstring()` methods are gone. They had served as aliases to `tobytes()` and `frombytes()`, deprecated all the way back to Python 3.2. (Contributed by Victor Stinner in [bpo-38916](https://bugs.python.org/issue?@action=redirect&bpo=38916).)

- The undocumented `sys.callstats()` function is gone. Deprecated since Python 3.7, it had always returned [`None`](https://docs.python.org/3.14/library/constants.html#None). It depended on a special build option `CALL_PROFILE` that was itself already dropped back in Python 3.7. (Contributed by Victor Stinner in [bpo-37414](https://bugs.python.org/issue?@action=redirect&bpo=37414).)

- The `sys.getcheckinterval()` and `sys.setcheckinterval()` functions are gone. Both had been deprecated since Python 3.2. Reach for [`sys.getswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.getswitchinterval) and [`sys.setswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.setswitchinterval) in their place. (Contributed by Victor Stinner in [bpo-37392](https://bugs.python.org/issue?@action=redirect&bpo=37392).)

- The C function `PyImport_Cleanup()` is gone. Its docstring had described it this way: ?Empty the module table. For internal use only.? That removal was contributed by Victor Stinner in [bpo-36710](https://bugs.python.org/issue?@action=redirect&bpo=36710).

- The `_dummy_thread` and `dummy_threading` modules are gone. They had been deprecated since Python 3.7, which mandates threading support. (Contributed by Victor Stinner in [bpo-37312](https://bugs.python.org/issue?@action=redirect&bpo=37312).)

- The `aifc.openfp()` alias to `aifc.open()`, the `sunau.openfp()` alias to `sunau.open()`, and the `wave.openfp()` alias to [`wave.open()`](https://docs.python.org/3.14/library/wave.html#wave.open) are gone. All three had been deprecated since Python 3.7. (Contributed by Victor Stinner in [bpo-37320](https://bugs.python.org/issue?@action=redirect&bpo=37320).)

- The `isAlive()` method belonging to [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) is gone. It had been deprecated since Python 3.8. Switch to [`is_alive()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.is_alive). (Contributed by Donghee Na in [bpo-37804](https://bugs.python.org/issue?@action=redirect&bpo=37804).)

- The `getchildren()` and `getiterator()` methods on the [`ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree) and [`Element`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) classes in the [`ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module are gone. Both had been deprecated back in Python 3.2. Write `iter(x)` or `list(x)` rather than `x.getchildren()`, and `x.iter()` or `list(x.iter())` rather than `x.getiterator()`. (Contributed by Serhiy Storchaka in [bpo-36543](https://bugs.python.org/issue?@action=redirect&bpo=36543).)

- The legacy [`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib) API is gone; it had been deprecated since Python 3.4. Rely on the [`load()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.load), [`loads()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.loads), [`dump()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.dump), and [`dumps()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.dumps) functions. On top of that, the *use_builtin_types* parameter was dropped; plain [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects are used at all times now. (Contributed by Jon Janzen in [bpo-36409](https://bugs.python.org/issue?@action=redirect&bpo=36409).)

- The C function `PyGen_NeedsFinalizing` is gone. It went undocumented, untested, and unused throughout CPython once [**PEP 442**](https://peps.python.org/pep-0442/) was implemented. Patch by Joannah Nanjekye. (Contributed by Joannah Nanjekye in [bpo-15088](https://bugs.python.org/issue?@action=redirect&bpo=15088))

- `base64.encodestring()` and `base64.decodestring()`, aliases that had been deprecated since Python 3.1, are gone: rely on [`base64.encodebytes()`](https://docs.python.org/3.14/library/base64.html#base64.encodebytes) and [`base64.decodebytes()`](https://docs.python.org/3.14/library/base64.html#base64.decodebytes) instead. (Contributed by Victor Stinner in [bpo-39351](https://bugs.python.org/issue?@action=redirect&bpo=39351).)

- The `fractions.gcd()` function is gone, having been deprecated since Python 3.5 ([bpo-22486](https://bugs.python.org/issue?@action=redirect&bpo=22486)): rely on [`math.gcd()`](https://docs.python.org/3.14/library/math.html#math.gcd) instead. (Contributed by Victor Stinner in [bpo-39350](https://bugs.python.org/issue?@action=redirect&bpo=39350).)

- The *buffering* parameter of [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) is gone. From Python 3.0 onward it had been ignored, and passing it raised a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Hand in an open file object to govern how the file gets opened. (Contributed by Victor Stinner in [bpo-39357](https://bugs.python.org/issue?@action=redirect&bpo=39357).)

- The *encoding* parameter of [`json.loads()`](https://docs.python.org/3.14/library/json.html#json.loads) is gone. Starting in Python 3.1 it was deprecated and ignored; passing it has triggered a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) since Python 3.8. (Contributed by Inada Naoki in [bpo-39377](https://bugs.python.org/issue?@action=redirect&bpo=39377))

- The `with (await asyncio.lock):` and `with (yield from asyncio.lock):` statements no longer work; reach for `async with lock` in their place. The same holds true for `asyncio.Condition` and `asyncio.Semaphore`. (Contributed by Andrew Svetlov in [bpo-34793](https://bugs.python.org/issue?@action=redirect&bpo=34793).)

- Three things are gone: the `sys.getcounts()` function, the `-X showalloccount` command line option, plus the `show_alloc_count` member within the C structure [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig). Each one depended on a special Python build that defined the `COUNT_ALLOCS` macro. (Contributed by Victor Stinner in [bpo-39489](https://bugs.python.org/issue?@action=redirect&bpo=39489).)

- The `_field_types` attribute on the [`typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) class is gone. It had been deprecated since Python 3.8. Use the `__annotations__` attribute in its place. (Contributed by Serhiy Storchaka in [bpo-40182](https://bugs.python.org/issue?@action=redirect&bpo=40182).)

- The `symtable.SymbolTable.has_exec()` method is gone. Deprecated since 2006, it had done nothing but return `False` whenever it was called. (Contributed by Batuhan Taskaya in [bpo-40208](https://bugs.python.org/issue?@action=redirect&bpo=40208))

-

The `asyncio.Task.current_task()` and `asyncio.Task.all_tasks()` are gone. Deprecated since Python 3.7, they give way to [`asyncio.current_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.current_task) and [`asyncio.all_tasks()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.all_tasks). (Contributed by Rémi Lapeyre in [bpo-40967](https://bugs.python.org/issue?@action=redirect&bpo=40967))

- The `unescape()` method on the [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) class is gone (it had been deprecated since Python 3.4). To turn character references into the matching unicode characters, use [`html.unescape()`](https://docs.python.org/3.14/library/html.html#html.unescape).

[Subject index](INDEX.md) · [Previous source section](deprecated.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](porting-to-python-3-9.md)
