# Python 2.5 changes: Collection, string and source-encoding changes

### Other Language Changes

What follows is every change Python 2.5 applies to the core Python language.

- A new hook on the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) type now lets subclasses supply a fallback value when a key isn't present in the dictionary. Whenever a key is missing, the dictionary's `__missing__(key)` method is called. The new `defaultdict` class in the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module is built on this hook. The example below defines a dictionary handing back zero for whatever key is absent:

```python
class zerodict (dict):
    def __missing__ (self, key):
        return 0

d = zerodict({1:1, 2:2})
print d[1], d[2]   # Prints 1, 2
print d[3], d[4]   # Prints 0, 0

```

- Both 8-bit and Unicode strings now carry fresh `partition(sep)` and `rpartition(sep)` methods, which streamline a frequent use case.

People often call the `find(S)` method to obtain an index, then slice the string with it to grab the parts before and after the separator. `partition(sep)` collapses that whole pattern into one method call returning a 3-tuple: the substring ahead of the separator, the separator itself, and the substring following it. When the separator is absent, the tuple's first element holds the complete string while the remaining two are empty. `rpartition(sep)` likewise returns a 3-tuple but scans starting from the string's end; here the `r` denotes "reverse".

A few examples:

```python
>>> ('http://www.python.org').partition('://')
('http', '://', 'www.python.org')
>>> ('file:/usr/share/doc/index.html').partition('://')
('file:/usr/share/doc/index.html', '', '')
>>> (u'Subject: a quick question').partition(':')
(u'Subject', u':', u' a quick question')
>>> 'www.python.org'.rpartition('.')
('www.python', '.', 'org')
>>> 'www.python.org'.rpartition(':')
('', '', 'www.python.org')

```

(Implemented by Fredrik Lundh after Raymond Hettinger suggested it.)

- String types' `startswith()` and `endswith()` methods will now take tuples of strings to test against.

```python
def is_image_file (filename):
    return filename.endswith(('.gif', '.jpg', '.tiff'))

```

(Implemented by Georg Brandl after a suggestion from Tom Lynn.)

- A `key` keyword parameter, mirroring the `key` argument used by `sort()`, was added to the [`min()`](https://docs.python.org/3.14/library/functions.html#min) and [`max()`](https://docs.python.org/3.14/library/functions.html#max) built-in functions. That parameter provides a function accepting one argument that gets invoked on each value in the list; `min()`/`max()` then returns whichever element yields the smallest/largest value from this function. As an example, to locate the longest string within a list you can write:

```python
L = ['medium', 'longest', 'short']
# Prints 'longest'
print max(L, key=len)
# Prints 'short', because lexicographically 'short' has the largest value
print max(L)

```

(Contributed by Steven Bethard and Raymond Hettinger.)

- A pair of new built-in functions, [`any()`](https://docs.python.org/3.14/library/functions.html#any) and [`all()`](https://docs.python.org/3.14/library/functions.html#all), test whether an iterator yields any true or any false values. `any()` gives back [`True`](https://docs.python.org/3.14/library/constants.html#True) whenever some value the iterator produces is true; otherwise it returns [`False`](https://docs.python.org/3.14/library/constants.html#False). `all()` returns `True` solely when every value the iterator produces evaluates as true. (Suggested by Guido van Rossum, and implemented by Raymond Hettinger.)

- What a class's `__hash__()` method returns may now be a long integer or an ordinary integer. When a long integer comes back, that value's hash is used. Previously the hash had to be an ordinary integer, but in 2.5 the [`id()`](https://docs.python.org/3.14/library/functions.html#id) built-in was altered to always yield non-negative numbers, and people frequently appear to use `id(self)` within `__hash__()` methods (even though that's discouraged).

- ASCII serves as the default encoding for modules from now on. It now counts as a syntax error when a module holds string literals containing 8-bit characters yet lacks an encoding declaration. Python 2.4 produced a warning here rather than a syntax error. Consult [**PEP 263**](https://peps.python.org/pep-0263/) for how to state a module's encoding; you might, for instance, insert a line such as this near the start of the source file:

```python
# -*- coding: latin1 -*-

```

[Subject index](INDEX.md) · [Previous source section](pep-357-the-index-method.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Following release/subject continuation](other-language-changes-c.md)
