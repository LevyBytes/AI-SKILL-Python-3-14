# What's New In Python 3.6 / Optimizations — asyncio-future, asyncio-task, fractions, glob, os, pathlib, pickle, typing, xml.etree.elementtree

### Optimizations

- A 16-bit wordcode now backs the Python interpreter rather than bytecode, which opened the door to several opcode optimizations. (Contributed by Demur Rumed, with reviews and feedback supplied by Serhiy Storchaka along with Victor Stinner, in [bpo-26647](https://bugs.python.org/issue?@action=redirect&bpo=26647) and [bpo-28050](https://bugs.python.org/issue?@action=redirect&bpo=28050).)

- An optimized C implementation now backs the [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) class. (Contributed by Yury Selivanov and INADA Naoki in [bpo-26081](https://bugs.python.org/issue?@action=redirect&bpo=26081).)

- An optimized C implementation now backs the [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) class. (Contributed by Yury Selivanov in [bpo-28544](https://bugs.python.org/issue?@action=redirect&bpo=28544).)

- Several implementation refinements within the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module (caching of generic types among them) deliver as much as 30 times faster performance alongside a smaller memory footprint.

- For the error handlers `surrogateescape`, `ignore` and `replace`, the ASCII decoder now runs as much as 60 times quicker (Contributed by Victor Stinner in [bpo-24870](https://bugs.python.org/issue?@action=redirect&bpo=24870)).

- For the error handler `surrogateescape`, both the ASCII and the Latin1 encoders now run as much as 3 times quicker (Contributed by Victor Stinner in [bpo-25227](https://bugs.python.org/issue?@action=redirect&bpo=25227)).

- For the error handlers `ignore`, `replace`, `surrogateescape`, `surrogatepass`, the UTF-8 encoder now runs as much as 75 times quicker (Contributed by Victor Stinner in [bpo-25267](https://bugs.python.org/issue?@action=redirect&bpo=25267)).

- For the error handlers `ignore`, `replace` and `surrogateescape`, the UTF-8 decoder now runs as much as 15 times quicker (Contributed by Victor Stinner in [bpo-25301](https://bugs.python.org/issue?@action=redirect&bpo=25301)).

- `bytes % args` now runs as much as 2 times quicker. (Contributed by Victor Stinner in [bpo-25349](https://bugs.python.org/issue?@action=redirect&bpo=25349)).

- `bytearray % args` now runs somewhere between 2.5 and 5 times quicker. (Contributed by Victor Stinner in [bpo-25399](https://bugs.python.org/issue?@action=redirect&bpo=25399)).

- Optimize [`bytes.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.fromhex) and [`bytearray.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.fromhex): they now run somewhere between 2x and 3.5x quicker. (Contributed by Victor Stinner in [bpo-25401](https://bugs.python.org/issue?@action=redirect&bpo=25401)).

- Optimize `bytes.replace(b'', b'.')` and `bytearray.replace(b'', b'.')`: as much as 80% quicker. (Contributed by Josh Snider in [bpo-26574](https://bugs.python.org/issue?@action=redirect&bpo=26574)).

- Allocator functions belonging to the [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) domain ([`PYMEM_DOMAIN_MEM`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_MEM)) now rely on the [pymalloc memory allocator](https://docs.python.org/3.14/c-api/memory.html#pymalloc) rather than the C library's `malloc()` function. The pymalloc allocator is tuned for short-lived objects of 512 bytes or fewer, and it falls back on `malloc()` for bigger memory blocks. (Contributed by Victor Stinner in [bpo-26249](https://bugs.python.org/issue?@action=redirect&bpo=26249)).

- [`pickle.load()`](https://docs.python.org/3.14/library/pickle.html#pickle.load) and [`pickle.loads()`](https://docs.python.org/3.14/library/pickle.html#pickle.loads) now run as much as 10% quicker while deserializing numerous small objects (Contributed by Victor Stinner in [bpo-27056](https://bugs.python.org/issue?@action=redirect&bpo=27056)).

- Handing [keyword arguments](https://docs.python.org/3.14/glossary.html#term-keyword-argument) to a function carries overhead next to handing over [positional arguments](https://docs.python.org/3.14/glossary.html#term-positional-argument). For extension functions built with Argument Clinic, that overhead is now cut substantially. (Contributed by Serhiy Storchaka in [bpo-27574](https://bugs.python.org/issue?@action=redirect&bpo=27574)).

- Optimized the [`glob()`](https://docs.python.org/3.14/library/glob.html#glob.glob) and [`iglob()`](https://docs.python.org/3.14/library/glob.html#glob.iglob) functions inside the [`glob`](https://docs.python.org/3.14/library/glob.html#module-glob) module; they now run roughly 3–6 times quicker. (Contributed by Serhiy Storchaka in [bpo-25596](https://bugs.python.org/issue?@action=redirect&bpo=25596)).

- Optimized globbing within [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib) by means of [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir); it now runs roughly 1.5–4 times quicker. (Contributed by Serhiy Storchaka in [bpo-26032](https://bugs.python.org/issue?@action=redirect&bpo=26032)).

- [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) saw substantial gains in parsing, iteration and deepcopy performance. (Contributed by Serhiy Storchaka in [bpo-25638](https://bugs.python.org/issue?@action=redirect&bpo=25638), [bpo-25873](https://bugs.python.org/issue?@action=redirect&bpo=25873), and [bpo-25869](https://bugs.python.org/issue?@action=redirect&bpo=25869).)

- Building [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) instances out of floats and decimals now runs 2 to 3 times quicker. (Contributed by Serhiy Storchaka in [bpo-25971](https://bugs.python.org/issue?@action=redirect&bpo=25971).)

[Subject index](INDEX.md) · [Previous source section](zlib.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](summary-release-highlights.md)
