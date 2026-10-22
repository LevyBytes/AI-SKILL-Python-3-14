# What's New In Python 3.4 / Code Cleanups — platform, pydoc, stat, tarfile

### Code Cleanups

- [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) no longer carries the idle, undocumented internal `Scanner` class.

- The private, all-but-dormant `_gestalt` module is gone, together with the private [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform) helpers `_mac_ver_lookup`, `_mac_ver_gstalt`, and `_bcd2str`, none of which would ever have run except on severely damaged OSX machines (consult [bpo-18393](https://bugs.python.org/issue?@action=redirect&bpo=18393)).

- Those hardcoded duplicates of select [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) constants that had lived in the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module namespace are gone.

[Subject index](INDEX.md) · [Previous source section](api-and-feature-removals.md) · [Next source section](porting-to-python-3-4.md) · [Release/subject declaration](release-highlights.md)
