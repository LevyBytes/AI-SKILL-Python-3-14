# Python 3.5.4 release candidate 1 / library / functions and types

[bpo-27863](https://bugs.python.org/issue?@action=redirect&bpo=27863): Repaired several ElementTree crashes that stemmed from race conditions and wrong types.

[bpo-30301](https://bugs.python.org/issue?@action=redirect&bpo=30301): Repair the AttributeError that arose from SimpleQueue.empty() under the *spawn* and *forkserver* start methods.

[bpo-30061](https://bugs.python.org/issue?@action=redirect&bpo=30061): Repaired crashes in the IOBase methods __next__() and readlines() that struck when readline() or __next__() respectively gave back a non-sizeable object. Repaired other possible errors brought on by failing to check the results of PyObject_Size(), PySequence_Size(), or PyMapping_Size().

[bpo-30879](https://bugs.python.org/issue?@action=redirect&bpo=30879): os.listdir() together with os.scandir() now yield bytes names whenever invoked with a bytes-like argument.

[bpo-30149](https://bugs.python.org/issue?@action=redirect&bpo=30149): inspect.signature() now copes with callables whose variable-argument parameters are wrapped using partialmethod. Donghee Na contributed the patch.

[bpo-28961](https://bugs.python.org/issue?@action=redirect&bpo=28961): Correct the unittest.mock._Call helper so the name parameter is honored rather than discarded. Jiajun Huang authored the fix.

[bpo-29444](https://bugs.python.org/issue?@action=redirect&bpo=29444): Repair an out-of-bounds buffer read in the group() method belonging to the match object. The work builds on a patch from WGH.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
