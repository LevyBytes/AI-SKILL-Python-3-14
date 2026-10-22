# What’s New in Python 2.7 / New and Improved Modules — collections, collections.abc, configparser, copy, http.cookiejar

Three more [`Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter) methods exist as well. [`most_common()`](https://docs.python.org/3.14/library/collections.html#collections.Counter.most_common) hands back the N elements that occur most often together with their tallies. [`elements()`](https://docs.python.org/3.14/library/collections.html#collections.Counter.elements) yields an iterator across the stored elements, emitting each one a number of times equal to its count. [`subtract()`](https://docs.python.org/3.14/library/collections.html#collections.Counter.subtract) accepts an iterable and decrements by one per element rather than incrementing; when the supplied argument is a dictionary or a fellow `Counter`, the tallies are deducted.

```python
>>> c.most_common(5)
[(' ', 6), ('e', 5), ('s', 3), ('a', 2), ('i', 2)]
>>> c.elements() ->
   'a', 'a', ' ', ' ', ' ', ' ', ' ', ' ',
   'e', 'e', 'e', 'e', 'e', 'g', 'f', 'i', 'i',
   'h', 'h', 'm', 'l', 'l', 'o', 'n', 'p', 's',
   's', 's', 'r', 't', 't', 'x'
>>> c['e']
5
>>> c.subtract('very heavy on the letter e')
>>> c['e']    # Count is now lower
-1

```

Contributed by Raymond Hettinger; [bpo-1696199](https://bugs.python.org/issue?@action=redirect&bpo=1696199).

New class: [`OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) gets its writeup in the preceding section PEP 372: Adding an Ordered Dictionary to collections.

New method: The [`deque`](https://docs.python.org/3.14/library/collections.html#collections.deque) data type has acquired a [`count()`](https://docs.python.org/3.14/library/collections.html#collections.deque.count) method, which reports how many stored elements equal the given argument *x*, plus a [`reverse()`](https://docs.python.org/3.14/library/collections.html#collections.deque.reverse) method that flips the deque's elements in-place. `deque` additionally surfaces its upper length bound through the read-only [`maxlen`](https://docs.python.org/3.14/library/collections.html#collections.deque.maxlen) attribute. (Both features added by Raymond Hettinger.)

The [`namedtuple`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) class has picked up an optional *rename* parameter. When *rename* is set to true, any field names that are invalid—either because they repeat or because they aren't valid Python identifiers—get renamed to valid names built from the field's index in the list of fields:

```python
>>> from collections import namedtuple
>>> T = namedtuple('T', ['field1', '$illegal', 'for', 'field2'], rename=True)
>>> T._fields
('field1', '_1', '_2', 'field2')

```

(Added by Raymond Hettinger; [bpo-1818](https://bugs.python.org/issue?@action=redirect&bpo=1818).)

Lastly, the [`Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) abstract base class will now hand back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) whenever a mapping is compared against a different type that is not a `Mapping`. (Fixed by Daniel Stutzbach; [bpo-8729](https://bugs.python.org/issue?@action=redirect&bpo=8729).)

- The constructors for the parsing classes within the [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) module now accept an *allow_no_value* parameter, which defaults to false; setting it to true permits options that carry no value. As an illustration:

```python
>>> import ConfigParser, StringIO
>>> sample_config = """
... [mysqld]
... user = mysql
... pid-file = /var/run/mysqld/mysqld.pid
... skip-bdb
... """
>>> config = ConfigParser.RawConfigParser(allow_no_value=True)
>>> config.readfp(StringIO.StringIO(sample_config))
>>> config.get('mysqld', 'user')
'mysql'
>>> print config.get('mysqld', 'skip-bdb')
None
>>> print config.get('mysqld', 'unknown')
Traceback (most recent call last):
  ...
NoOptionError: No option 'unknown' in section: 'mysqld'

```

(Contributed by Mats Kindahl; [bpo-7005](https://bugs.python.org/issue?@action=redirect&bpo=7005).)

- Deprecated function: `contextlib.nested()`, which lets you manage more than one context manager within a single [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, is now deprecated, given that the `with` statement itself can now take several context managers.

- The [`cookielib`](https://docs.python.org/3.14/library/http.cookiejar.html#module-http.cookiejar) module will now discard cookies whose version field is invalid—that is, one that lacks an integer value. (Fixed by John J. Lee; [bpo-3924](https://bugs.python.org/issue?@action=redirect&bpo=3924).)

- The [`deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy) function in the [`copy`](https://docs.python.org/3.14/library/copy.html#module-copy) module now copies bound instance methods correctly. (Implemented by Robert Collins; [bpo-1515](https://bugs.python.org/issue?@action=redirect&bpo=1515).)

-

[Subject index](INDEX.md) · [Next source section](ctypes-through-io-module-changes.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](standard-library-module-changes.md)
