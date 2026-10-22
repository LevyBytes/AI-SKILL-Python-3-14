# What’s New In Python 3.8 / API and Feature Removals — collections, collections.abc, os, tarfile, time, xml.etree.elementtree

### API and Feature Removals

The following features and APIs have been removed from Python 3.8:

- From Python 3.3 onward, importing ABCs out of [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) was deprecated, with the import expected to come from [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) instead. Although the ability to import from collections was flagged for removal in 3.8, that step was pushed back to 3.9. (See [gh-81134](https://github.com/python/cpython/issues/81134).)

- Having been deprecated back in Python 3.7, the `macpath` module is now gone. (Contributed by Victor Stinner in [bpo-35471](https://bugs.python.org/issue?@action=redirect&bpo=35471).)

- The `platform.popen()` function has been removed, having stayed deprecated ever since Python 3.3: use [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen) instead. (Contributed by Victor Stinner in [bpo-35345](https://bugs.python.org/issue?@action=redirect&bpo=35345).)

- The `time.clock()` function has been removed, having stayed deprecated ever since Python 3.3: depending on what you need for well-defined behavior, use [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter) or [`time.process_time()`](https://docs.python.org/3.14/library/time.html#time.process_time) instead. (Contributed by Matthias Bussonnier in [bpo-36895](https://bugs.python.org/issue?@action=redirect&bpo=36895).)

- The `pyvenv` script has been removed in favor of `python3.8 -m venv`, clearing up any confusion over which Python interpreter the `pyvenv` script was bound to. (Contributed by Brett Cannon in [bpo-25427](https://bugs.python.org/issue?@action=redirect&bpo=25427).)

- From the `cgi` module, `parse_qs`, `parse_qsl`, and `escape` are now gone. Their deprecation dates to Python 3.2 or earlier. Pull them from the `urllib.parse` and `html` modules in their place.

- The `filemode` function is removed from the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module. Undocumented, it has been deprecated since Python 3.3.

- The *html* argument is no longer accepted by the [`XMLParser`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser) constructor. That argument did nothing and had been deprecated since Python 3.4. Every remaining parameter is now [keyword-only](https://docs.python.org/3.14/glossary.html#keyword-only-parameter). (Contributed by Serhiy Storchaka in [bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209).)

- Removed the `doctype()` method of [`XMLParser`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser). (Contributed by Serhiy Storchaka in [bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209).)

- The "unicode_internal" codec is removed. (Contributed by Inada Naoki in [bpo-36297](https://bugs.python.org/issue?@action=redirect&bpo=36297).)

-

User code can no longer reach the `Cache` and `Statement` objects belonging to the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module. (Contributed by Aviv Palivoda in [bpo-30262](https://bugs.python.org/issue?@action=redirect&bpo=30262).)

- Both [`fileinput.input()`](https://docs.python.org/3.14/library/fileinput.html#fileinput.input) and [`fileinput.FileInput()`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput) had a `bufsize` keyword argument that was disregarded and marked deprecated starting in Python 3.6; it is now gone. [bpo-36952](https://bugs.python.org/issue?@action=redirect&bpo=36952) (Contributed by Matthias Bussonnier.)

- Dropped in this release are `sys.set_coroutine_wrapper()` and `sys.get_coroutine_wrapper()`, both of which carried a deprecation notice from Python 3.7; [bpo-36933](https://bugs.python.org/issue?@action=redirect&bpo=36933) (Contributed by Matthias Bussonnier.)

[Subject index](INDEX.md) · [Previous source section](deprecated.md) · [Release/subject declaration](assignment-expressions.md) · [Next source section](porting-to-python-3-8.md)
