# Python 3.6.2 release candidate 1 / library / functions and types

[bpo-30301](https://bugs.python.org/issue?@action=redirect&bpo=30301): Eliminate the AttributeError raised by SimpleQueue.empty() when the *spawn* and *forkserver* start methods are active.

[bpo-30061](https://bugs.python.org/issue?@action=redirect&bpo=30061): Repaired crashes in the IOBase methods __next__() and readlines() arising when readline() or __next__() respectively hand back a non-sizeable object. Also corrected possible other errors stemming from failing to verify the results of PyObject_Size(), PySequence_Size(), or PyMapping_Size().

[bpo-30017](https://bugs.python.org/issue?@action=redirect&bpo=30017): The close() method on the zip entry writer object may now be invoked repeatedly. Any write to a writer that is closed now consistently raises a ValueError.

[bpo-27863](https://bugs.python.org/issue?@action=redirect&bpo=27863): Corrected several ElementTree crashes brought on by wrong types and race conditions.

[bpo-30149](https://bugs.python.org/issue?@action=redirect&bpo=30149): inspect.signature() now copes with callables having variable-argument parameters that are wrapped via partialmethod. Donghee Na wrote the patch.

[bpo-29581](https://bugs.python.org/issue?@action=redirect&bpo=29581): ABCMeta.__new__ now takes `**kwargs`, which lets abstract base classes pass keyword parameters inside __init_subclass__. Nate Soares wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
