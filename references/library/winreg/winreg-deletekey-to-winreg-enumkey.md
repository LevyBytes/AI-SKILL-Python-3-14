# Functions: `winreg.DeleteKey()`, `winreg.DeleteKeyEx()`, `winreg.DeleteValue()`, `winreg.EnumKey()`

winreg.DeleteKey(*key*, *sub_key*)

Removes the named key.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*sub_key* is a string, and it has to be a subkey beneath the key named by the *key* parameter. This value is not allowed to be `None`, and the key must be free of subkeys.

*This method can not delete keys with subkeys.*

When the method succeeds, the whole key ? every one of its values included ? gets removed. Should the method fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.DeleteKey` with arguments `key`, `sub_key`, `access`.

Changed in version 3.3: See above.

 winreg.DeleteKeyEx(*key*, *sub_key*, *access=KEY_WOW64_64KEY*, *reserved=0*)

Removes the named key.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*sub_key* is a string, and it has to be a subkey beneath the key named by the *key* parameter. This value is not allowed to be `None`, and the key must be free of subkeys.

*reserved* is held in reserve as an integer; it has to be zero, and zero is what it defaults to.

*access* is an integer holding an access mask that spells out the security access you want for the key. Its default is `KEY_WOW64_64KEY`. On 32-bit Windows, the WOW64 constants are ignored. Consult Access Rights for the rest of the permitted values.

*This method can not delete keys with subkeys.*

When the method succeeds, the whole key ? every one of its values included ? gets removed. Should the method fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised.

On unsupported Windows versions, [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError) is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.DeleteKey` with arguments `key`, `sub_key`, `access`.

Added in version 3.2.

Changed in version 3.3: See above.

 winreg.DeleteValue(*key*, *value*)

Removes a named value from a registry key.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*value* is a string that identifies the value to remove.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.DeleteValue` with arguments `key`, `value`.

 winreg.EnumKey(*key*, *index*)

Walks through the subkeys of an open registry key, giving back a string.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*index* is an integer pinpointing the index of the key you want fetched.

Each call to the function fetches the name of a single subkey. The usual pattern is to call it again and again until an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised, which signals that nothing further remains.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.EnumKey` with arguments `key`, `index`.

Changed in version 3.3: See above.

[Subject index](INDEX.md) · [Previous](winreg-closekey-to-winreg-createkeyex.md) · [Continue](winreg-enumvalue-to-winreg-loadkey.md) · [Owning module, declaration or section: Functions](winreg-closekey-to-winreg-createkeyex.md)
