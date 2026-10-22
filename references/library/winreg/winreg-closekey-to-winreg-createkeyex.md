# Functions: `winreg.CloseKey()`, `winreg.ConnectRegistry()`, `winreg.CreateKey()`, `winreg.CreateKeyEx()`

### Functions

The functions provided by this module are listed below:

 winreg.CloseKey(*hkey*)

Closes a registry key that was opened earlier. The *hkey* argument names a key opened previously.

Note

When *hkey* is left unclosed by this method (or by `hkey.Close()`), Python closes it once the *hkey* object gets destroyed.

 winreg.ConnectRegistry(*computer_name*, *key*)

Opens a connection to a predefined registry handle located on a different computer, and gives back a handle object.

*computer_name* names the remote computer; give it as `r"\\computername"`. With `None` supplied, the local computer is the one used.

*key* is the predefined handle to connect to.

What comes back is the handle of the key that was opened. Should the function fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.ConnectRegistry` with arguments `computer_name`, `key`.

Changed in version 3.3: See above.

 winreg.CreateKey(*key*, *sub_key*)

Either creates the specified key or opens it, returning a handle object.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*sub_key* is a string giving the name of the key that this method either opens or creates.

When *key* happens to be one of the predefined keys, *sub_key* may be `None`. In such a case, the handle you get back is identical to the key handle originally supplied to the function.

Where the key is already present, the function simply opens that existing key.

What gets returned is the handle belonging to the opened key. Should the function fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.CreateKey` with arguments `key`, `sub_key`, `access`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.OpenKey/result` with argument `key`.

Changed in version 3.3: See above.

 winreg.CreateKeyEx(*key*, *sub_key*, *reserved=0*, *access=KEY_WRITE*)

Either creates the specified key or opens it, returning a handle object.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*sub_key* is a string that names the key this method opens or creates.

*reserved* is held in reserve as an integer; it has to be zero, and zero is what it defaults to.

*access* is an integer holding an access mask that spells out the security access you want for the key. Its default is `KEY_WRITE`. Consult Access Rights for the rest of the permitted values.

When *key* is one of the predefined keys, *sub_key* is permitted to be `None`. Under that condition, the handle handed back matches the very key handle that was passed into the function.

Where the key is already present, the function simply opens that existing key.

What gets returned is the handle belonging to the opened key. Should the function fail, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.CreateKey` with arguments `key`, `sub_key`, `access`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.OpenKey/result` with argument `key`.

Added in version 3.2.

Changed in version 3.3: See above.

[Subject index](INDEX.md) · [Previous](winreg-windows-registry-access.md) · [Continue](winreg-deletekey-to-winreg-enumkey.md)
