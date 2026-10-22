# Python 3.9.0 alpha 1 / library / imports and modules

[bpo-38142](https://bugs.python.org/issue?@action=redirect&bpo=38142): The _hashlib OpenSSL wrapper extension module now conforms to PEP-384.

[bpo-36543](https://bugs.python.org/issue?@action=redirect&bpo=36543): Took out the Element.getchildren(), Element.getiterator() and ElementTree.getiterator() methods along with the xml.etree.cElementTree module.

[bpo-37742](https://bugs.python.org/issue?@action=redirect&bpo=37742): When handed the name ?root?, logging.getLogger() hands back the root logger today; earlier releases instead produced a non-root logger carrying the name ?root?. Code that deliberately requests a non-root logger called ?root?, or that calls logging.getLogger(__name__) inside a top-level module named ?root.py?, may notice the difference.

[bpo-28292](https://bugs.python.org/issue?@action=redirect&bpo=28292): Flagged the calendar.py helper functions as private. Doing so follows PEP 8 guidance about keeping the module's style conventions consistent and clears up a known source of user confusion.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
