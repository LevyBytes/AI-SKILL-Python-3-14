# Python 3.7.0 alpha 1 / library / empty slots added abc abc letting subclassers refuse dict weakref

[bpo-30463](https://bugs.python.org/issue?@action=redirect&bpo=30463): An empty __slots__ was added to abc.ABC, letting subclassers refuse __dict__ and __weakref__ creation. Aaron Hall provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
