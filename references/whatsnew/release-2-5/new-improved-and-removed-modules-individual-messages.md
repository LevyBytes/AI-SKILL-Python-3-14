# What's New in Python 2.5 / New, Improved, and Removed Modules - doctest, email, fileinput, gc, heapq, itertools, locale, mailbox

The [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module gained a `SKIP` option that stops an example from running entirely. It is meant for code snippets that serve as usage examples for the reader rather than as genuine test cases.

An *encoding* parameter was added to both the `testfile()` function and the `DocFileSuite` class so you can declare the file's encoding. This makes it simpler to put non-ASCII characters into tests embedded in a docstring. (Contributed by Bjorn Tillenius.)

- The [`email`](https://docs.python.org/3.14/library/email.html#module-email) package has been brought up to version 4.0. (Contributed by Barry Warsaw.)

- The [`fileinput`](https://docs.python.org/3.14/library/fileinput.html#module-fileinput) module became more flexible. Unicode filenames are now handled, and a *mode* parameter defaulting to `"r"` was added to the [`input()`](https://docs.python.org/3.14/library/functions.html#input) function so files can be opened in binary or [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines) mode. A further new parameter, *openhook*, lets you supply some function besides [`open()`](https://docs.python.org/3.14/library/functions.html#open) to open the input files. While you iterate over the collection of files, the `FileInput` object's new [`fileno()`](https://docs.python.org/3.14/library/fileinput.html#fileinput.fileno) yields the file descriptor of the file currently open. (Contributed by Georg Brandl.)

- Within the [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module, the new `get_count()` function returns a 3-tuple holding the present collection counts for the three GC generations. These are bookkeeping figures for the garbage collector; once the counts hit a set threshold, a garbage collection sweep runs. The existing [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) function now accepts an optional *generation* argument of 0, 1, or 2 to indicate which generation to collect. (Contributed by Barry Warsaw.)

- The `nsmallest()` and `nlargest()` functions of the [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) module now take a `key` keyword parameter much like the one offered by the [`min()`](https://docs.python.org/3.14/library/functions.html#min)/[`max()`](https://docs.python.org/3.14/library/functions.html#max) functions and the `sort()` methods. For instance:

```python
>>> import heapq
>>> L = ["short", 'medium', 'longest', 'longer still']
>>> heapq.nsmallest(2, L)  # Return two lowest elements, lexicographically
['longer still', 'longest']
>>> heapq.nsmallest(2, L, key=len)   # Return two shortest elements
['short', 'medium']

```

(Contributed by Raymond Hettinger.)

- The [`itertools.islice()`](https://docs.python.org/3.14/library/itertools.html#itertools.islice) function now allows `None` for the start and step arguments. That brings it more in line with the attributes of slice objects, letting you now write the following:

```python
s = slice(5)     # Create slice object
itertools.islice(iterable, s.start, s.stop, s.step)

```

(Contributed by Raymond Hettinger.)

- The [`format()`](https://docs.python.org/3.14/library/functions.html#format) function of the [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) module was changed, and two further functions, `format_string()` and `currency()`, were added.

Earlier, the *val* parameter of the [`format()`](https://docs.python.org/3.14/library/functions.html#format) function could be a string provided no more than one %char specifier was present; now the parameter has to be exactly one %char specifier with no text around it. An optional *monetary* parameter was also introduced which, when `True`, applies the locale's currency-formatting rules to insert a separator between groups of three digits.

To format strings carrying several %char specifiers, reach for the new `format_string()` function, which behaves like [`format()`](https://docs.python.org/3.14/library/functions.html#format) yet also permits blending %char specifiers with arbitrary text.

A new `currency()` function was likewise added that formats a number per the current locale's settings.

(Contributed by Georg Brandl.)

- The [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox) module went through a sweeping rewrite that adds the ability to alter mailboxes rather than merely read them. A fresh set of classes — among them `mbox`, `MH`, and `Maildir` — read mailboxes and provide an `add(message)` method for adding messages, `remove(key)` for deleting them, and `lock()`/`unlock()` for locking and unlocking the mailbox. The example below turns a maildir-format mailbox into an mbox-format one:

```python
import mailbox

# 'factory=None' uses email.Message.Message as the class representing
# individual messages.
src = mailbox.Maildir('maildir', factory=None)
dest = mailbox.mbox('/tmp/mbox')

for msg in src:
    dest.add(msg)

```

(Contributed by Gregory K. Johnson. The work was funded through Google's 2005 Summer of Code.)

- New module: the `msilib` module makes it possible to create Microsoft Installer `.msi` files together with CAB files. There is also some support for reading the `.msi` database. (Contributed by Martin von Löwis.)

- The `nis` module now permits access to domains beyond the system default domain by passing a *domain* argument to the `nis.match()` and `nis.maps()` functions. (Contributed by Ben Bell.)

[Subject index](INDEX.md) · [Previous source section](standard-library-module-changes.md) · [Next source section](operator-through-completion-module-changes.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Release/subject declaration](standard-library-module-changes.md)
