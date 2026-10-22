# Value Types

### Value Types

For more information, see [Registry Value Types](https://msdn.microsoft.com/en-us/library/ms724884%28v=VS.85%29.aspx).

 winreg.REG_BINARY

Binary data in any form.

 winreg.REG_DWORD

32-bit number.

 winreg.REG_DWORD_LITTLE_ENDIAN

A 32-bit number in little-endian format. Equivalent to `REG_DWORD`.

 winreg.REG_DWORD_BIG_ENDIAN

A 32-bit number in big-endian format.

 winreg.REG_EXPAND_SZ

Null-terminated string containing references to environment variables (`%PATH%`).

 winreg.REG_LINK

A Unicode symbolic link.

 winreg.REG_MULTI_SZ

A run of null-terminated strings that ends with a pair of null characters. (This terminating step is taken care of by Python on its own.)

 winreg.REG_NONE

No defined value type.

 winreg.REG_QWORD

A 64-bit number.

Added in version 3.6.

 winreg.REG_QWORD_LITTLE_ENDIAN

A 64-bit number in little-endian format. Equivalent to `REG_QWORD`.

Added in version 3.6.

 winreg.REG_RESOURCE_LIST

A device-driver resource list.

 winreg.REG_FULL_RESOURCE_DESCRIPTOR

A hardware setting.

 winreg.REG_RESOURCE_REQUIREMENTS_LIST

A hardware resource list.

 winreg.REG_SZ

A null-terminated string.

[Subject index](INDEX.md) · [Previous](winreg-key-wow64-64key-to-winreg-key-wow64-32key.md) · [Continue](pyhkey-close-to-pyhkey-exit.md)
