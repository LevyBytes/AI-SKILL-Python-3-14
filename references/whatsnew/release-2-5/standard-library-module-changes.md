# What's New in Python 2.5 / New, Improved, and Removed Modules - codecs, collections, contextlib, csv, datetime, difflib, profile, time

### New, Improved, and Removed Modules

Python 2.5 brought numerous improvements and bug fixes to the standard library. What follows is a partial roundup of the most significant changes, arranged alphabetically by module name. For a fuller accounting, see the `Misc/NEWS` file in the source tree, or dig through the SVN logs for every detail.

- The `audioop` module now handles the a-LAW encoding, and the u-LAW encoding code has been refined. (Contributed by Lars Immisch.)

- The [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module picked up support for incremental codecs. Its `codec.lookup()` function now hands back a `CodecInfo` instance rather than a tuple. To stay backward compatible, `CodecInfo` instances act like a 4-tuple while also exposing the attributes `encode`, `decode`, `incrementalencoder`, `incrementaldecoder`, `streamwriter`, and `streamreader`. An incremental codec can take input and emit output across several chunks, with the combined output identical to feeding the whole input through the non-incremental codec at once. Consult the `codecs` module documentation for the specifics. (Designed and implemented by Walter Dörwald.)

- The [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module added a new type, `defaultdict`, which subclasses the standard [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) type. For the most part it behaves like an ordinary dictionary, but when a key is missing it builds a default value, automatically inserting it for the key that was asked for.

`defaultdict`'s constructor takes as its first argument a factory function that fires every time a requested key turns out to be absent. Since this factory function is called with no arguments, you can hand it built-in type constructors like [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list) or [`int()`](https://docs.python.org/3.14/library/functions.html#int). For instance, here is how you might index words by the letter they start with:

```python
words = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura
che la diritta via era smarrita""".lower().split()

index = defaultdict(list)

for w in words:
    init_letter = w[0]
    index[init_letter].append(w)

```

Printing `index` yields this output:

```python
defaultdict(<type 'list'>, {'c': ['cammin', 'che'], 'e': ['era'],
        'd': ['del', 'di', 'diritta'], 'm': ['mezzo', 'mi'],
        'l': ['la'], 'o': ['oscura'], 'n': ['nel', 'nostra'],
        'p': ['per'], 's': ['selva', 'smarrita'],
        'r': ['ritrovai'], 'u': ['una'], 'v': ['vita', 'via']}

```

(Contributed by Guido van Rossum.)

- The `deque` double-ended queue type from the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module now provides a `remove(value)` method that drops the first occurrence of *value* in the queue, raising [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the value is absent. (Contributed by Raymond Hettinger.)

- New module: the [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module holds helper functions meant to accompany the new "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement. The section The contextlib module covers this module in greater depth.

- New module: the [`cProfile`](https://docs.python.org/3.14/library/profile.html#module-cProfile) module is a C rewrite of the existing [`profile`](https://docs.python.org/3.14/library/profile.html#module-profile) module carrying far less overhead. Its interface mirrors `profile`: you call `cProfile.run('main()')` to profile a function, you can write profile data to a file, and so on. Whether the Hotshot profiler — likewise written in C but not conforming to the `profile` module's interface — will keep being maintained in later Python releases remains uncertain. (Contributed by Armin Rigo.)

The [`pstats`](https://docs.python.org/3.14/library/profile.html#module-pstats) module, used to analyze the data the profiler gathers, now lets you route its output to any file object by passing a *stream* argument to the `Stats` constructor. (Contributed by Skip Montanaro.)

- The [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) module, which reads files in comma-separated value format, gained several improvements together with a batch of bugfixes. You can now cap the maximum field size in bytes by calling the `csv.field_size_limit(new_limit)` function; leave out the *new_limit* argument and it returns the limit currently in effect. The `reader` class now carries a `line_num` attribute tracking how many physical lines have been read from the source; because a single record may stretch over several physical lines, `line_num` differs from the count of records read.

The CSV parser has grown stricter regarding multi-line quoted fields. Formerly, when a line finished inside a quoted field with no closing newline character, a newline got spliced into the field that was returned. That behavior caused trouble when reading files holding carriage return characters inside fields, so the code was revised to return the field without inserting any newlines. Consequently, when embedded newlines within fields matter, you should break the input into lines in a way that retains the newline characters.

(Contributed by Skip Montanaro and Andrew McNamara.)

- The [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) class within the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module now offers a `strptime(string, format)` method for parsing date strings, contributed by Josh Spoerri. It relies on the same format characters as [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) and [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime):

```python
import datetime as dt

ts = dt.datetime.strptime('10:13:15 2006-03-07',
                          '%H:%M:%S %Y-%m-%d')

```

- The `SequenceMatcher.get_matching_blocks()` method of the [`difflib`](https://docs.python.org/3.14/library/difflib.html#module-difflib) module now promises to return a minimal list of blocks that describe matching subsequences. In the past, the algorithm would now and then split one block of matching elements across two list entries. (Enhancement by Tim Peters.)

-

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](new-improved-and-removed-modules-individual-messages.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
