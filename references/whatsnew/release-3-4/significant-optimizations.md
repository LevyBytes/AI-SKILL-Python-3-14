# What's New In Python 3.4 / Significant Optimizations - bz2, collections, html, locale, lzma, os, random, re, subprocess

### Significant Optimizations

- The UTF-32 decoder runs 3x to 4x quicker now. (Contributed by Serhiy Storchaka in [bpo-14625](https://bugs.python.org/issue?@action=redirect&bpo=14625).)

- What hash collisions cost for sets has gone down. Every hash table probe now examines a run of consecutive, neighboring key/hash pairs ahead of falling back on random probes across the hash table. Doing so leverages cache locality so that resolving a collision costs less. You can view the collision resolution approach as a blend of linear probing and open addressing. By default the count of extra linear probes is nine. That figure is adjustable at compile-time by setting LINEAR_PROBES to whatever value you like. Setting LINEAR_PROBES=0 disables linear probing altogether. (Contributed by Raymond Hettinger in [bpo-18771](https://bugs.python.org/issue?@action=redirect&bpo=18771).)

- Interpreter startup is roughly 30% quicker. A pair of measures drives the gain. Startup loads fewer modules, so for instance the [`re`](https://docs.python.org/3.14/library/re.html#module-re), [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) and [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) modules together with what they depend on are no longer imported up front. The marshal module got better at loading compiled Python code more quickly. (Contributed by Antoine Pitrou, Christian Heimes and Victor Stinner in [bpo-19219](https://bugs.python.org/issue?@action=redirect&bpo=19219), [bpo-19218](https://bugs.python.org/issue?@action=redirect&bpo=19218), [bpo-19209](https://bugs.python.org/issue?@action=redirect&bpo=19209), [bpo-19205](https://bugs.python.org/issue?@action=redirect&bpo=19205) and [bpo-9548](https://bugs.python.org/issue?@action=redirect&bpo=9548).)

- [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) now matches or beats the Python2 version across most scenarios. [`lzma.LZMAFile`](https://docs.python.org/3.14/library/lzma.html#lzma.LZMAFile) has likewise been tuned. (Contributed by Serhiy Storchaka and Nadeem Vawda in [bpo-16034](https://bugs.python.org/issue?@action=redirect&bpo=16034).)

- [`random.getrandbits()`](https://docs.python.org/3.14/library/random.html#random.getrandbits) runs 20%-40% quicker for small integers (which is the most common use case). (Contributed by Serhiy Storchaka in [bpo-16674](https://bugs.python.org/issue?@action=redirect&bpo=16674).)

- Leveraging the new storage layout for strings, pickling strings has gotten substantially quicker. (Contributed by Victor Stinner and Antoine Pitrou in [bpo-15596](https://bugs.python.org/issue?@action=redirect&bpo=15596).)

- A performance snag in `io.FileIO.readall()` got resolved. Windows feels this most, and it markedly accelerates piping sizeable quantities of data via [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess). (Contributed by Richard Oudkerk in [bpo-15758](https://bugs.python.org/issue?@action=redirect&bpo=15758).)

- [`html.escape()`](https://docs.python.org/3.14/library/html.html#html.escape) runs 10x quicker now. (Contributed by Matt Bryant in [bpo-18020](https://bugs.python.org/issue?@action=redirect&bpo=18020).)

- Under Windows, the native `VirtualAlloc` now stands in for the CRT `malloc` inside `obmalloc`. Synthetic benchmarks point to roughly a 3% memory saving.

- [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) now relies on a lazily opened persistent file descriptor, which keeps it from burning through many file descriptors when many threads run it in parallel. (Contributed by Antoine Pitrou in [bpo-18756](https://bugs.python.org/issue?@action=redirect&bpo=18756).)

[Subject index](INDEX.md) · [Previous source section](other-improvements.md) · [Next source section](deprecated.md) · [Release/subject declaration](release-highlights.md)
