# Python 3.5.2 release candidate 1 / library / memory and lifetimes

[bpo-24103](https://bugs.python.org/issue?@action=redirect&bpo=24103): A possible use-after-free in ElementTree.XMLPullParser has been fixed.

[bpo-25902](https://bugs.python.org/issue?@action=redirect&bpo=25902): Several refcount problems in ElementTree iteration have been fixed.

[bpo-25725](https://bugs.python.org/issue?@action=redirect&bpo=25725): Closed a reference leak inside pickle.loads() that surfaced while unpickling bad data that contained tuple instructions.

[bpo-25688](https://bugs.python.org/issue?@action=redirect&bpo=25688): Plugged a file leak that occurred when ElementTree.iterparse() raised an error.

[bpo-25945](https://bugs.python.org/issue?@action=redirect&bpo=25945): A crash that happened while unpickling a functools.partial object holding a bad state has been fixed, along with a leak from a failed functools.partial constructor. The "args" and "keywords" attributes of functools.partial now consistently carry the tuple and dict types respectively.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
