# Python 3.5.3 release candidate 1 / library / ctypes

[bpo-25659](https://bugs.python.org/issue?@action=redirect&bpo=25659): Within ctypes, head off a crash when from_buffer() and from_buffer_copy() are invoked on abstract classes such as Array.

[bpo-27330](https://bugs.python.org/issue?@action=redirect&bpo=27330): Closed potential leaks inside the ctypes module.

[bpo-18893](https://bugs.python.org/issue?@action=redirect&bpo=18893): Repair faulty exception handling within Lib/ctypes/macholib/dyld.py. Madison May supplied the patch.

[bpo-27570](https://bugs.python.org/issue?@action=redirect&bpo=27570): Steer clear of zero-length memcpy() and similar calls that carry null source pointers within the "ctypes" and "array" modules.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
