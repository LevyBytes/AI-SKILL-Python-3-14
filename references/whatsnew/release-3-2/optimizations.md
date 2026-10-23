# What's New In Python 3.2 / Optimizations - configparser, http.server, operator, pickle, threading

### Optimizations

Several modest speed improvements have been folded in:

- The peephole optimizer in Python now spots patterns like `x in {1, 2, 3}` and treats them as a membership check against a set of constants. The optimizer rewrites the [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) into a [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) and keeps the prebuilt constant.

With the speed cost removed, adopting set-notation for membership checks becomes worthwhile. The resulting style reads clearly while still executing quickly:

```python
extension = name.rpartition('.')[2]
if extension in {'xml', 'html', 'xhtml', 'css'}:
    handle(name)

```

(Patch and additional tests contributed by Dave Malcolm; [bpo-6690](https://bugs.python.org/issue?@action=redirect&bpo=6690)).

- Turning data into and out of its serialized form through the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module now happens several times quicker.

(Credited to Alexandre Vassalotti plus Antoine Pitrou together with the Unladen Swallow team, tracked under [bpo-9410](https://bugs.python.org/issue?@action=redirect&bpo=9410) and [bpo-3873](https://bugs.python.org/issue?@action=redirect&bpo=3873).)

- The [Timsort algorithm](https://en.wikipedia.org/wiki/Timsort) behind [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) and [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) is quicker now and burns less memory whenever you pass a [key function](https://docs.python.org/3.14/glossary.html#term-key-function). Formerly each list element got boxed inside a throwaway object holding the key value belonging to that element. These days a pair of arrays, one of keys and one of values, are sorted side by side. That spares the memory the sort wrappers ate and recovers the time previously lost handing off comparisons.

(Patch by Daniel Stutzbach in [bpo-9915](https://bugs.python.org/issue?@action=redirect&bpo=9915).)

- Decoding JSON runs faster and uses up less memory any time one string recurs across several keys. Furthermore, JSON encoding taps the C speedups whenever the `sort_keys` argument holds true.

(Credited to Antoine Pitrou under [bpo-7451](https://bugs.python.org/issue?@action=redirect&bpo=7451), together with Raymond Hettinger plus Antoine Pitrou under [bpo-10314](https://bugs.python.org/issue?@action=redirect&bpo=10314).)

- Recursive locks (made with the [`threading.RLock()`](https://docs.python.org/3.14/library/threading.html#threading.RLock) API) now gain from a C implementation that puts them on par with ordinary locks, running roughly 10x to 15x quicker than the older pure Python version did.

(Contributed by Antoine Pitrou; [bpo-3001](https://bugs.python.org/issue?@action=redirect&bpo=3001).)

- Stringlib’s fast-search algorithm now backs the [`split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split), [`rsplit()`](https://docs.python.org/3.14/library/stdtypes.html#str.rsplit), [`splitlines()`](https://docs.python.org/3.14/library/stdtypes.html#str.splitlines) and [`replace()`](https://docs.python.org/3.14/library/stdtypes.html#str.replace) methods on [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects. The same algorithm likewise serves [`rfind()`](https://docs.python.org/3.14/library/stdtypes.html#str.rfind), [`rindex()`](https://docs.python.org/3.14/library/stdtypes.html#str.rindex), `rsplit()` and [`rpartition()`](https://docs.python.org/3.14/library/stdtypes.html#str.rpartition).

(Patch by Florent Xicluna in [bpo-7622](https://bugs.python.org/issue?@action=redirect&bpo=7622) and [bpo-7462](https://bugs.python.org/issue?@action=redirect&bpo=7462).)

- Converting integers to strings now proceeds two “digits” per step, which cuts down how many division and modulo operations run.

([bpo-6713](https://bugs.python.org/issue?@action=redirect&bpo=6713) by Gawain Bolton, Mark Dickinson, and Victor Stinner.)

A handful of other minor optimizations exist too. Set differencing goes quicker when one operand vastly outsizes the other (patch by Andress Bennetts in [bpo-8685](https://bugs.python.org/issue?@action=redirect&bpo=8685)). A speedier implementation now backs the `array.repeat()` method ([bpo-1569291](https://bugs.python.org/issue?@action=redirect&bpo=1569291) by Alexander Belopolsky). Buffering inside the [`BaseHTTPRequestHandler`](https://docs.python.org/3.14/library/http.server.html#http.server.BaseHTTPRequestHandler) is more efficient ([bpo-3709](https://bugs.python.org/issue?@action=redirect&bpo=3709) by Andrew Schaaf). The [`operator.attrgetter()`](https://docs.python.org/3.14/library/operator.html#operator.attrgetter) function was made faster ([bpo-10160](https://bugs.python.org/issue?@action=redirect&bpo=10160) by Christos Georgiou). And [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) reads multi-line arguments somewhat more quickly ([bpo-7113](https://bugs.python.org/issue?@action=redirect&bpo=7113) by Łukasz Langa).

[Subject index](INDEX.md) · [Previous source section](multi-threading.md) · [Next source section](unicode.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
