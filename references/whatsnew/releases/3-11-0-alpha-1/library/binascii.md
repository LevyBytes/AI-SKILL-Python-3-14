# Python 3.11.0 alpha 1 / library / binascii

[bpo-45085](https://bugs.python.org/issue?@action=redirect&bpo=45085): The `binhex` module, which was deprecated in Python 3.9, has now been deleted. These [`binascii`](https://docs.python.org/3.14/library/binascii.html#module-binascii) functions, likewise deprecated in Python 3.9, are gone as well:

  - `a2b_hqx()`, `b2a_hqx()`;

  - `rlecode_hqx()`, `rledecode_hqx()`.

The [`binascii.crc_hqx()`](https://docs.python.org/3.14/library/binascii.html#binascii.crc_hqx) function is still around.

Victor Stinner wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
