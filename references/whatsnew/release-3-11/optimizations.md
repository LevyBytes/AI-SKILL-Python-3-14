# What's New In Python 3.11 / Optimizations — asyncio-protocol, math, statistics, unicodedata

### Optimizations

The optimizations described here stand apart from the Faster CPython project, which gets its own dedicated section.

- On string literals that carry only the format codes `%s`, `%r` and `%a`, the compiler now optimizes plain [printf-style % formatting](https://docs.python.org/3.14/library/stdtypes.html#old-string-formatting), bringing its speed level with an equivalent [f-string](https://docs.python.org/3.14/glossary.html#term-f-string) expression. (Contributed by Serhiy Storchaka in [bpo-28307](https://bugs.python.org/issue?@action=redirect&bpo=28307).)

- Compilers can now optimize integer division (`//`) more effectively. When an [`int`](https://docs.python.org/3.14/library/functions.html#int) is divided by something below `2**30`, it runs roughly 20% faster on x86-64. (Contributed by Gregory P. Smith and Tim Peters in [gh-90564](https://github.com/python/cpython/issues/90564).)

- For integers under `2**30`, [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) now runs almost 30% quicker. (Contributed by Stefan Behnel in [gh-68264](https://github.com/python/cpython/issues/68264).)

- The common path for resizing lists has been streamlined, which accelerates [`list.append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append) by approximately 15% and basic [list comprehension](https://docs.python.org/3.14/glossary.html#term-list-comprehension)s by as much as 20-30% (Contributed by Dennis Sweeney in [gh-91165](https://github.com/python/cpython/issues/91165).)

- Whenever every key is a Unicode object, dictionaries skip storing hash values, which shrinks [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) size. To illustrate, on 64-bit platforms `sys.getsizeof(dict.fromkeys("abcdefg"))` drops from 352 bytes to 272 bytes (23% smaller). (Contributed by Inada Naoki in [bpo-46845](https://bugs.python.org/issue?@action=redirect&bpo=46845).)

- When transferring large files over UDP, [`asyncio.DatagramProtocol`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.DatagramProtocol) now performs orders of magnitude better, clocking more than 100 times the speed on a approximately 60 MiB file. (Contributed by msoxzw in [gh-91487](https://github.com/python/cpython/issues/91487).)

- For large arguments, the [`math`](https://docs.python.org/3.14/library/math.html#module-math) functions [`comb()`](https://docs.python.org/3.14/library/math.html#math.comb) and [`perm()`](https://docs.python.org/3.14/library/math.html#math.perm) now run about approximately 10 times quicker (the bigger *k* gets, the larger the speedup). (Contributed by Serhiy Storchaka in [bpo-37295](https://bugs.python.org/issue?@action=redirect&bpo=37295).)

- Rather than first turning iterators into a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), the [`statistics`](https://docs.python.org/3.14/library/statistics.html#module-statistics) functions [`mean()`](https://docs.python.org/3.14/library/statistics.html#statistics.mean), [`variance()`](https://docs.python.org/3.14/library/statistics.html#statistics.variance) and [`stdev()`](https://docs.python.org/3.14/library/statistics.html#statistics.stdev) now walk them in a single pass. That doubles the speed and may free up a good deal of memory. (Contributed by Raymond Hettinger in [gh-90415](https://github.com/python/cpython/issues/90415).)

- [`unicodedata.normalize()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.normalize) now handles the normalization of pure-ASCII strings in constant time. (Contributed by Donghee Na in [bpo-44987](https://bugs.python.org/issue?@action=redirect&bpo=44987).)

[Subject index](INDEX.md) · [Previous source section](zipfile.md) · [Next source section](faster-cpython.md) · [Release/subject declaration](summary-release-highlights.md)
