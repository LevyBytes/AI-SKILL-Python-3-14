# What’s New In Python 3.5 / Optimizations — fractions, io, ipaddress, json, marshal, os, random

### Optimizations

On POSIX systems the [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk) function runs 3 to 5 times quicker, and on Windows it runs 7 to 20 times quicker. The gain comes from the new [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) function, which pulls file details from whichever `readdir` or `FindFirstFile`/`FindNextFile` call sits underneath. (Authored by Ben Hoyt, assisted by Victor Stinner, in [bpo-23605](https://bugs.python.org/issue?@action=redirect&bpo=23605).)

Building `bytes(int)` (which fills with zero bytes) now runs quicker and consumes less memory for sizable objects. To allocate the storage for such objects, `calloc()` takes over from `malloc()`. (Contributed by Victor Stinner in [bpo-21233](https://bugs.python.org/issue?@action=redirect&bpo=21233).)

Several [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) operations on [`IPv4Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Network) and [`IPv6Network`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv6Network) became dramatically quicker, among them [`subnets()`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Network.subnets), [`supernet()`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.IPv4Network.supernet), [`summarize_address_range()`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.summarize_address_range), [`collapse_addresses()`](https://docs.python.org/3.14/library/ipaddress.html#ipaddress.collapse_addresses). The improvement spans somewhere between 3 and 15 times over. (Authored by Antoine Pitrou, plus Michel Albert and Markus, in [bpo-21486](https://bugs.python.org/issue?@action=redirect&bpo=21486), [bpo-21487](https://bugs.python.org/issue?@action=redirect&bpo=21487), [bpo-20826](https://bugs.python.org/issue?@action=redirect&bpo=20826), [bpo-23266](https://bugs.python.org/issue?@action=redirect&bpo=23266).)

Serializing [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) objects via pickle was tuned so the resulting output is markedly smaller. (Contributed by Serhiy Storchaka in [bpo-23133](https://bugs.python.org/issue?@action=redirect&bpo=23133).)

A wide range of [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) operations now run 50% to 100% quicker. (Contributed by Serhiy Storchaka in [bpo-15381](https://bugs.python.org/issue?@action=redirect&bpo=15381) and David Wilson in [bpo-22003](https://bugs.python.org/issue?@action=redirect&bpo=22003).)

The [`marshal.dumps()`](https://docs.python.org/3.14/library/marshal.html#marshal.dumps) function picked up speed: 65–85% for versions 3 and 4, 20–25% for versions 0 to 2 on common data, and as much as 5 times in the best scenarios. (Contributed by Serhiy Storchaka in [bpo-20416](https://bugs.python.org/issue?@action=redirect&bpo=20416) and [bpo-23344](https://bugs.python.org/issue?@action=redirect&bpo=23344).)

Encoding with UTF-32 now runs 3 to 7 times quicker. (Contributed by Serhiy Storchaka in [bpo-15027](https://bugs.python.org/issue?@action=redirect&bpo=15027).)

Parsing of regular expressions is now as much as 10% quicker. (Contributed by Serhiy Storchaka in [bpo-19380](https://bugs.python.org/issue?@action=redirect&bpo=19380).)

The [`json.dumps()`](https://docs.python.org/3.14/library/json.html#json.dumps) function was tuned to run under `ensure_ascii=False` just as quickly as it does under `ensure_ascii=True`. (Contributed by Naoki Inada in [bpo-23206](https://bugs.python.org/issue?@action=redirect&bpo=23206).)

When the second argument carries [`type`](https://docs.python.org/3.14/library/functions.html#type) as its metaclass — the usual situation — both [`PyObject_IsInstance()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_IsInstance) and [`PyObject_IsSubclass()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_IsSubclass) now run faster. (Contributed Georg Brandl by in [bpo-22540](https://bugs.python.org/issue?@action=redirect&bpo=22540).)

Caching of methods got a small upgrade, delivering as much as a 5% gain on certain benchmarks. (Contributed by Antoine Pitrou in [bpo-22847](https://bugs.python.org/issue?@action=redirect&bpo=22847).)

On 64-bit builds, objects from the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module take up 50% less memory. (Contributed by Serhiy Storchaka in [bpo-23488](https://bugs.python.org/issue?@action=redirect&bpo=23488).)

Getter calls through [`property()`](https://docs.python.org/3.14/library/functions.html#property) became as much as 25% quicker. (Contributed by Joe Jevnik in [bpo-23910](https://bugs.python.org/issue?@action=redirect&bpo=23910).)

Creating a [`fractions.Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) is now as much as 30% quicker. (Contributed by Stefan Behnel in [bpo-22464](https://bugs.python.org/issue?@action=redirect&bpo=22464).)

The string methods [`find()`](https://docs.python.org/3.14/library/stdtypes.html#str.find), [`rfind()`](https://docs.python.org/3.14/library/stdtypes.html#str.rfind), [`split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split), [`partition()`](https://docs.python.org/3.14/library/stdtypes.html#str.partition) plus the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) string operator now run much faster when hunting for 1-character substrings. (Contributed by Serhiy Storchaka in [bpo-23573](https://bugs.python.org/issue?@action=redirect&bpo=23573).)

[Subject index](INDEX.md) · [Previous source section](other-module-level-changes.md) · [Next source section](build-and-c-api-changes.md) · [Release/subject declaration](summary-release-highlights.md)
