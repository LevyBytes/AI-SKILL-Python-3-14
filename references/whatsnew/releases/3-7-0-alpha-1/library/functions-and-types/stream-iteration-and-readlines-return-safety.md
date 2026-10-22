# Python 3.7.0 alpha 1 / library / iobase methods next readlines crashed whenever readline or next

[bpo-30061](https://bugs.python.org/issue?@action=redirect&bpo=30061): The IOBase methods __next__() and readlines() crashed whenever readline() or __next__() respectively returned a non-sizeable object; this was corrected. Other possible errors from failing to check the results of PyObject_Size(), PySequence_Size(), or PyMapping_Size() were also fixed.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
