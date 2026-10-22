# What's New In Python 3.4 / Deprecations in the Python API

### Deprecations in the Python API

-

Per PEP 451: A ModuleSpec Type for the Import System, several [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) functions and methods have been marked obsolete: `importlib.find_loader()` gives way to [`importlib.util.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.find_spec); `importlib.machinery.PathFinder.find_module()` gives way to [`importlib.machinery.PathFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.PathFinder.find_spec); `importlib.abc.MetaPathFinder.find_module()` gives way to [`importlib.abc.MetaPathFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder.find_spec); both `importlib.abc.PathEntryFinder.find_loader()` and `find_module()` give way to [`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.PathEntryFinder.find_spec); every one of the `*xxx*Loader` ABC `load_module` methods (`importlib.abc.Loader.load_module()`, `importlib.abc.InspectLoader.load_module()`, `importlib.abc.FileLoader.load_module()`, `importlib.abc.SourceLoader.load_module()`) ought no longer be written — loaders are instead expected to supply an `exec_module` method ([`importlib.abc.Loader.exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.Loader.exec_module), [`importlib.abc.InspectLoader.exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.InspectLoader.exec_module) [`importlib.abc.SourceLoader.exec_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.SourceLoader.exec_module)) and leave the remainder to the import machinery; and `importlib.abc.Loader.module_repr()`, `importlib.util.module_for_loader()`, `importlib.util.set_loader()`, plus `importlib.util.set_package()` are now superfluous since the import system performs their jobs on its own.

- The `imp` module sits in a pending-deprecation state. So that Python 2/3 shared code bases keep working, dropping the module has no current timeline.

- The `formatter` module sits in a pending-deprecation state, with removal targeted for Python 3.6.

- Using `MD5` as the implicit *digestmod* for [`hmac.new()`](https://docs.python.org/3.14/library/hmac.html#hmac.new) is now obsolete. Starting with Python 3.6, an explicit digest name or constructor must be supplied as the *digestmod* argument.

- For a long while the docstring of the internal `Netrc` class inside the [`ftplib`](https://docs.python.org/3.14/library/ftplib.html#module-ftplib) module has flagged it as obsolete. That class now raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) and is scheduled for full removal in Python 3.5.

- The undocumented *endtime* parameter on [`subprocess.Popen.wait()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.wait) was never meant to be public and is presumably unused; it is now obsolete and quite likely to disappear in Python 3.5.

- [`HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser)'s *strict* parameter is now obsolete.

- Within [`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib), the `readPlist()`, `writePlist()`, `readPlistFromBytes()`, and `writePlistToBytes()` calls are now obsolete; prefer the matching new routines [`load()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.load), [`dump()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.dump), [`loads()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.loads), and [`dumps()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.dumps). Likewise `Data()` is obsolete; simply rely on the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) constructor in its place.

- Within [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig), the `SO` key is now obsolete; `EXT_SUFFIX` stands in for it.

- The `U` mode that assorted `open` functions accept is now obsolete. Under Python3 it has no useful effect, so swap in suitable calls to [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) (where required) together with its *newline* parameter.

- Both the *parser* parameter of [`xml.etree.ElementTree.iterparse()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse) and the *html* parameter of [`XMLParser()`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser) are now obsolete. Ahead of dropping the latter, every argument handed to `XMLParser` ought to be supplied by keyword.

[Subject index](INDEX.md) · [Previous source section](deprecated.md) · [Release/subject declaration](release-highlights.md) · [Next source section](deprecated-features.md)
