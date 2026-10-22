# Python 3.8.0 alpha 1 / c api / sequence

[bpo-32500](https://bugs.python.org/issue?@action=redirect&bpo=32500): Repaired the error messages from [`PySequence_Size()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_Size), [`PySequence_GetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_GetItem), [`PySequence_SetItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_SetItem) and [`PySequence_DelItem()`](https://docs.python.org/3.14/c-api/sequence.html#c.PySequence_DelItem) invoked using a mapping, plus [`PyMapping_Size()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_Size) invoked using a sequence.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
