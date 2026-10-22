# Python 3.6.0 alpha 1 / core and builtins / numeric behavior

[bpo-24731](https://bugs.python.org/issue?@action=redirect&bpo=24731): Repair the crash that occurred when objects whose special methods __bytes__, __trunc__, and __float__ returned instances of subclasses of bytes, int, and float were converted to subclasses of bytes, int, and float correspondingly.

[bpo-24802](https://bugs.python.org/issue?@action=redirect&bpo=24802): Steer clear of buffer overreads when int(), float(), compile(), exec() and eval() receive bytes-like objects. Such objects need not end with a null byte, yet the functions had assumed they did.

[bpo-26171](https://bugs.python.org/issue?@action=redirect&bpo=26171): Repair the possible integer overflow plus heap corruption within zipimporter.get_data().

[bpo-27005](https://bugs.python.org/issue?@action=redirect&bpo=27005): Tune the float.fromhex() class method for exact float. The result runs 2 times faster now.

[bpo-26107](https://bugs.python.org/issue?@action=redirect&bpo=26107): The layout of the `co_lnotab` attribute on code objects shifts so that negative line number deltas are supported.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
