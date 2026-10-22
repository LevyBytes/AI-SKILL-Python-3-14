# Python 3.6.0 alpha 1 / library / memory and lifetimes

[bpo-25725](https://bugs.python.org/issue?@action=redirect&bpo=25725): Closed a reference leak within pickle.loads() that occurred while unpickling malformed data carrying tuple instructions.

[bpo-25688](https://bugs.python.org/issue?@action=redirect&bpo=25688): Repaired a file leak occurring when ElementTree.iterparse() raises an error.

[bpo-25357](https://bugs.python.org/issue?@action=redirect&bpo=25357): An optional newline parameter was added to binascii.b2a_base64(). To dodge a memory copy, base64.b64encode() makes use of it.

[bpo-25578](https://bugs.python.org/issue?@action=redirect&bpo=25578): Corrected one more memory leak within SSLSocket.getpeercer().

[bpo-25569](https://bugs.python.org/issue?@action=redirect&bpo=25569): Corrected a memory leak inside SSLSocket.getpeercert().

[bpo-24103](https://bugs.python.org/issue?@action=redirect&bpo=24103): Corrected a possible use-after-free within ElementTree.XMLPullParser.

[bpo-25902](https://bugs.python.org/issue?@action=redirect&bpo=25902): Corrected assorted refcount problems in ElementTree iteration.

[bpo-26588](https://bugs.python.org/issue?@action=redirect&bpo=26588): The _tracemalloc machinery can now trace memory allocations across several address spaces (domains).

[bpo-25945](https://bugs.python.org/issue?@action=redirect&bpo=25945): Corrected a crash that happened when unpickling a functools.partial object holding bad state, and plugged a leak when the functools.partial constructor fails. The "args" and "keywords" attributes of functools.partial are now always of types tuple and dict respectively.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
