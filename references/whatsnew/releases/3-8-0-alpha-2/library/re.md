# Python 3.8.0 alpha 2 / library / re

[bpo-34294](https://bugs.python.org/issue?@action=redirect&bpo=34294): re module, correct mistaken capturing groups in uncommon situations. [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search), [`re.findall()`](https://docs.python.org/3.14/library/re.html#re.findall), [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) along with other functions that scan a string for a match ought to clear capturing groups between successive match attempts. Patch by Ma Lin.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
