# What’s New in Python 2.7 / Porting to Python 2.7 — datetime, decimal, io, syslog, tarfile, urllib.parse, xml.etree.elementtree

### Porting to Python 2.7

Collected here are the already-described changes plus further bugfixes that might oblige you to adjust your code:

- Arguments handed to the [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) function are treated more uniformly now; it will call [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) on any non-float, non-integer argument it receives. (Fixed by Alexander Belopolsky; [bpo-1533](https://bugs.python.org/issue?@action=redirect&bpo=1533).)

- For floating-point and complex numbers, the string [`format()`](https://docs.python.org/3.14/library/functions.html#format) method shifted its default precision from 6 decimal places up to 12, lining up with the precision that [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) uses. (Changed by Eric Smith; [bpo-5920](https://bugs.python.org/issue?@action=redirect&bpo=5920).)

- Owing to an optimization applied to the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, the special methods [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) have to live on the object's type and can't simply be pinned onto the object's instance. The impact lands on new-style classes (those derived from [`object`](https://docs.python.org/3.14/library/functions.html#object)) and on C extension types. ([bpo-6101](https://bugs.python.org/issue?@action=redirect&bpo=6101).)

- Thanks to a bug present in Python 2.6, the *exc_value* parameter passed to [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods was frequently the string form of the exception rather than an instance. That got corrected in 2.7, so *exc_value* will arrive as the instance you'd expect. (Fixed by Florent Xicluna; [bpo-7853](https://bugs.python.org/issue?@action=redirect&bpo=7853).)

- Where a limited group of attributes had been declared through `__slots__`, removing one that was never set failed to raise [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) the way you would anticipate. Fixed by Benjamin Peterson; [bpo-7604](https://bugs.python.org/issue?@action=redirect&bpo=7604).)

In the standard library:

- Operations on [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instances that produced a year beyond the supported range would not consistently raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError). Those cases are now examined with more rigor and will raise it. (Mark Leander reported this; the patch came from Anand B. Pillai and Alexander Belopolsky; [bpo-7150](https://bugs.python.org/issue?@action=redirect&bpo=7150).)

- Feeding [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) instances to a string's [`format()`](https://docs.python.org/3.14/library/functions.html#format) method used to default to left-alignment. The default is now right-alignment, which could alter what your programs print. (Changed by Mark Dickinson; [bpo-6857](https://bugs.python.org/issue?@action=redirect&bpo=6857).)

Comparisons that involve a signaling NaN value (or `sNAN`) now raise [`InvalidOperation`](https://docs.python.org/3.14/library/decimal.html#decimal.InvalidOperation) rather than quietly handing back a true or false result based on the operator. Quiet NaN values (or `NaN`) can now be hashed. (Fixed by Mark Dickinson; [bpo-7279](https://bugs.python.org/issue?@action=redirect&bpo=7279).)

- The [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) library has stopped escaping ampersands and angle brackets while writing an XML processing instruction (something resembling `<?xml-stylesheet href="#style1"?>`) or comment (which looks like ``). (Patch by Neil Muller; [bpo-2746](https://bugs.python.org/issue?@action=redirect&bpo=2746).)

- Asked for a negative length, the `readline()` method on [`StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) objects now does nothing, matching the behavior of other file-like objects. ([bpo-7348](https://bugs.python.org/issue?@action=redirect&bpo=7348)).

- For its identifier, the [`syslog`](https://docs.python.org/3.14/library/syslog.html#module-syslog) module will now take the value of `sys.argv[0]` in place of the earlier default of `'python'`. (Changed by Sean Reifschneider; [bpo-8451](https://bugs.python.org/issue?@action=redirect&bpo=8451).)

- Default error handling in the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module has shifted so that fatal errors are no longer swallowed. The error level had defaulted to 0, which meant an error merely wrote a message to the debug log; yet since that debug log isn't on by default, such errors slipped past unnoticed. With the new default error level of 1, an exception is raised whenever an error occurs. (Changed by Lars Gustäbel; [bpo-7357](https://bugs.python.org/issue?@action=redirect&bpo=7357).)

- The [`urlsplit()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlsplit) routine in the [`urlparse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) module now deals with unfamiliar URL schemes in a manner that follows [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html): given a URL shaped like `"<something>://..."`, whatever sits ahead of the `://` counts as the scheme, even when it's an invented scheme unknown to the module. Such a change could trip up code that compensated for the prior behaviour. As an illustration, Python 2.6.4 or 2.5 hands back the following:

```pycon
>>> import urlparse
>>> urlparse.urlsplit('invented://host/filename?query')
('invented', '', '//host/filename?query', '', '')

```

Python 2.7 (and Python 2.6.5) will return:

```pycon
>>> import urlparse
>>> urlparse.urlsplit('invented://host/filename?query')
('invented', 'host', '/filename?query', '', '')

```

(What Python 2.7 emits actually differs a little, given that it returns a named tuple rather than an ordinary tuple.)

For C extensions:

- C extensions feeding integer format codes to the `PyArg_Parse*` family of functions will now raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception rather than setting off a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) ([bpo-5080](https://bugs.python.org/issue?@action=redirect&bpo=5080)).

- Reach for the new [`PyOS_string_to_double()`](https://docs.python.org/3.14/c-api/conversion.html#c.PyOS_string_to_double) function rather than the older `PyOS_ascii_strtod()` and `PyOS_ascii_atof()` functions, both of which are deprecated now.

For applications that embed Python:

- To let applications seal a security hole that arose from using the existing `PySys_SetArgv()` function, the `PySys_SetArgvEx()` function was introduced. Check whether `PySys_SetArgv()` is being called and weigh carefully whether the application ought to use `PySys_SetArgvEx()` with *updatepath* set to false.

[Subject index](INDEX.md) · [Previous source section](other-changes-and-fixes.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Next source section](new-features-added-to-python-2-7-maintenance-releases.md)
