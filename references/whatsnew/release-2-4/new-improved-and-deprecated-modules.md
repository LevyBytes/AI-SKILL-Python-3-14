# What’s New in Python 2.4 / New, Improved, and Deprecated Modules - base64, bisect, collections, configparser, curses, difflib, threading

### New, Improved, and Deprecated Modules

As is customary, Python's standard library gained a range of improvements and bug fixes. What follows is a partial rundown of the most noteworthy changes, ordered alphabetically by module name. Refer to the `Misc/NEWS` file within the source tree for a fuller list of changes, or browse the CVS logs for every detail.

- The `asyncore` module's `loop()` function now carries a *count* parameter, allowing you to run a bounded number of passes over the polling loop. By default it still loops indefinitely.

- The [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64) module now offers fuller [**RFC 3548**](https://datatracker.ietf.org/doc/html/rfc3548.html) coverage for Base64, Base32, and Base16 encoding and decoding, with optional case folding and optional alternative alphabets included. (Contributed by Barry Warsaw.)

- The [`bisect`](https://docs.python.org/3.14/library/bisect.html#module-bisect) module now rests on an underlying C implementation, giving it better performance. (Contributed by Dmitry Vasiliev.)

- The CJKCodecs assortment of East Asian codecs, looked after by Hye-Shik Chang, was folded into 2.4. The encodings newly added are:

- Chinese (PRC): gb2312, gbk, gb18030, big5hkscs, hz

- Chinese (ROC): big5, cp950

- Japanese: cp932, euc-jis-2004, euc-jp, euc-jisx0213, iso-2022-jp,

iso-2022-jp-1, iso-2022-jp-2, iso-2022-jp-3, iso-2022-jp-ext, iso-2022-jp-2004, shift-jis, shift-jisx0213, shift-jis-2004

- Korean: cp949, euc-kr, johab, iso-2022-kr

- A handful of additional encodings were also brought in: HP Roman8, ISO_8859-11, ISO_8859-16, PCTP-154, and TIS-620.

- The UTF-8 and UTF-16 codecs now deal more gracefully with getting partial input. Earlier the `StreamReader` class would attempt to read additional data, which made it impossible to pick decoding back up from the stream. The `read()` method will now hand back as much data as it has, and later calls will resume decoding from wherever earlier ones stopped. (Implemented by Walter Dörwald.)

- There is a new [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module for various specialized collection datatypes. At present it holds a single type, `deque`, a double-ended queue that efficiently supports adding and removing elements at either end:

```python
>>> from collections import deque
>>> d = deque('ghi')        # make a new deque with three items
>>> d.append('j')           # add a new entry to the right side
>>> d.appendleft('f')       # add a new entry to the left side
>>> d                       # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])
>>> d.pop()                 # return and remove the rightmost item
'j'
>>> d.popleft()             # return and remove the leftmost item
'f'
>>> list(d)                 # list the contents of the deque
['g', 'h', 'i']
>>> 'h' in d                # search the deque
True

```

A number of modules, including the `Queue` and [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) modules, now make use of [`collections.deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) to run faster. (Contributed by Raymond Hettinger.)

- The [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) classes received some minor enhancements. The [`read()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.read) method now hands back a list of the files it parsed successfully, and the [`set()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.set) method raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when given a *value* argument that is not a string. (Contributed by John Belmonte and David Goodger.)

- The [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module now backs the ncurses extension `use_default_colors()`. On platforms whose terminal handles transparency, this lets you employ a transparent background. (Contributed by Jörg Lehmann.)

- The [`difflib`](https://docs.python.org/3.14/library/difflib.html#module-difflib) module now carries an `HtmlDiff` class that builds an HTML table presenting a side-by-side comparison between two versions of some text. (Contributed by Dan Gass.)

-

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](email-through-locale-module-changes.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
