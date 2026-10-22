# What's New In Python 3.4 / plistlib — plistlib

### plistlib

[`plistlib`](https://docs.python.org/3.14/library/plistlib.html#module-plistlib) now offers an API resembling the usual shape of stdlib serialization protocols, with fresh [`load()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.load), [`dump()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.dump), [`loads()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.loads), and [`dumps()`](https://docs.python.org/3.14/library/plistlib.html#plistlib.dumps) functions. (The earlier API is deprecated now.) Beyond the already supported XML plist format ([`FMT_XML`](https://docs.python.org/3.14/library/plistlib.html#plistlib.FMT_XML)), it handles the binary plist format ([`FMT_BINARY`](https://docs.python.org/3.14/library/plistlib.html#plistlib.FMT_BINARY)) as well. (Contributed by Ronald Oussoren and others in [bpo-14455](https://bugs.python.org/issue?@action=redirect&bpo=14455).)

[Subject index](INDEX.md) · [Previous source section](pickle.md) · [Next source section](poplib.md) · [Release/subject declaration](release-highlights.md)
