# Functions: `winreg.OpenKey()`, `winreg.OpenKeyEx()`, `winreg.QueryInfoKey()`, `winreg.QueryValue()`, `winreg.QueryValueEx()`

winreg.OpenKey(*key*, *sub_key*, *reserved=0*, *access=KEY_READ*)

 winreg.OpenKeyEx(*key*, *sub_key*, *reserved=0*, *access=KEY_READ*)

Opens the named key and gives back a handle object.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*sub_key* is a string pinpointing the sub_key you wish to open.

*reserved* is held in reserve as an integer; it has to be zero, and zero is what it defaults to.

*access* is an integer holding an access mask that spells out the security access you want for the key. Its default is `KEY_READ`. Consult Access Rights for the rest of the permitted values.

A fresh handle to the named key is what you receive.

Should the function fail, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.OpenKey` with arguments `key`, `sub_key`, `access`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.OpenKey/result` with argument `key`.

Changed in version 3.2: Allow the use of named arguments.

Changed in version 3.3: See above.

 winreg.QueryInfoKey(*key*)

Gives back details about a key, packaged as a tuple.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

What you get is a tuple holding 3 items:

| Index | Meaning |
| --- | --- |
| `0` | An integer giving the number of sub keys this key has. |
| `1` | An integer giving the number of values this key has. |
| `2` | An integer reporting the key's last-modified time (where available), in 100-nanosecond intervals counted from Jan 1, 1601. |

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.QueryInfoKey` with argument `key`.

 winreg.QueryValue(*key*, *sub_key*)

Fetches a key's unnamed value and returns it as a string.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*sub_key* is a string carrying the name of the subkey the value is tied to. Where this parameter comes in as `None` or empty, the function pulls back the value that the `SetValue()` method set for the key named by *key*.

Each registry value carries a name, a type, and a data part. What this method pulls back is the data belonging to a key's first value whose name is `NULL`. Since the underlying API call omits the type, lean on `QueryValueEx()` whenever you can.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.QueryValue` with arguments `key`, `sub_key`, `value_name`.

 winreg.QueryValueEx(*key*, *value_name*)

Pulls back both the type and the data for a given value name attached to an open registry key.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*value_name* is a string pointing to the value you want to query.

What you get is a tuple holding 2 items:

| Index | Meaning |
| --- | --- |
| `0` | The value of the registry item. |
| `1` | An integer stating this value's registry type (consult the table in the docs for `SetValueEx()`) |

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.QueryValue` with arguments `key`, `sub_key`, `value_name`.

[Subject index](INDEX.md) · [Previous](winreg-enumvalue-to-winreg-loadkey.md) · [Continue](winreg-savekey-to-winreg-enablereflectionkey.md) · [Owning module, declaration or section: Functions](winreg-closekey-to-winreg-createkeyex.md)
