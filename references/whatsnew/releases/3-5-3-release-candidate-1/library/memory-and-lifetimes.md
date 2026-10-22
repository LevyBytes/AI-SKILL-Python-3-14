# Python 3.5.3 release candidate 1 / library / memory and lifetimes

[bpo-27773](https://bugs.python.org/issue?@action=redirect&bpo=27773): Cleared up several memory-management mistakes around server_hostname inside _ssl.wrap_socket().

[bpo-27783](https://bugs.python.org/issue?@action=redirect&bpo=27783): Closed off a potential use of uninitialized memory in operator.methodcaller.

[bpo-28275](https://bugs.python.org/issue?@action=redirect&bpo=28275): Repair a possible use-after-free inside the decompress() methods of the LZMADecompressor and BZ2Decompressor classes. John Leitch supplied the original patch.

[bpo-27932](https://bugs.python.org/issue?@action=redirect&bpo=27932): Head off a memory leak inside win32_ver().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
