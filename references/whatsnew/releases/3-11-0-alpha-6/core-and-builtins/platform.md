# Python 3.11.0 alpha 6 / core and builtins / platform

[bpo-46845](https://bugs.python.org/issue?@action=redirect&bpo=46845): Shrink dict size by dropping the hash value out of the hash table whenever every inserted key is Unicode. As an example, on a 64bit platform `sys.getsizeof(dict.fromkeys("abcdefg"))` drops to 272 bytes from the former 352 bytes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
