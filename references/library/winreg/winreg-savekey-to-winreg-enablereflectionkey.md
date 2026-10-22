# Functions: `winreg.SaveKey()`, `winreg.SetValue()`, `winreg.SetValueEx()`, `winreg.DisableReflectionKey()`, `winreg.EnableReflectionKey()`

winreg.SaveKey(*key*, *file_name*)

Writes the named key together with every one of its subkeys into the file you name.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*file_name* gives the name of the file that registry data is written to. That file must not already be present. When this filename bears an extension, the `LoadKey()` method cannot use it on file allocation table (FAT) file systems.

When *key* points at a key residing on a remote computer, the path given by *file_name* is taken relative to that remote computer. Whoever invokes this method has to hold the **SeBackupPrivilege** security privilege. Be aware that privileges and permissions are not the same thing ? consult the [Conflicts Between User Rights and Permissions documentation](https://msdn.microsoft.com/en-us/library/ms724878%28v=VS.85%29.aspx) for further details.

This function passes `NULL` for *security_attributes* to the API.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.SaveKey` with arguments `key`, `file_name`.

 winreg.SetValue(*key*, *sub_key*, *type*, *value*)

Ties a value to a given key.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*sub_key* is a string naming the subkey the value is bound to.

*type* is an integer stating the data's type. For now it has to be `REG_SZ`, so only strings are handled. Reach for the `SetValueEx()` function when you need other data types supported.

*value* is a string stating the new value.

Should no key match the *sub_key* parameter, the SetValue function brings it into being.

The length a value can have depends on the memory you have available. Values that run long (over 2048 bytes) are best kept as files, with the configuration registry holding the filenames instead. Doing so keeps the registry running efficiently.

The key picked out by the *key* parameter has to have been opened carrying `KEY_SET_VALUE` access.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.SetValue` with arguments `key`, `sub_key`, `type`, `value`.

 winreg.SetValueEx(*key*, *value_name*, *reserved*, *type*, *value*)

Writes data into the value field belonging to an open registry key.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*value_name* is a string naming the subkey the value is bound to.

*reserved* may be set to anything ? the API is always handed zero.

*type* is an integer stating the data's type. Refer to Value Types for the types you can use.

*value* is a string stating the new value.

This method can additionally record further value and type information for the named key. The key picked out by the key parameter has to have been opened carrying `KEY_SET_VALUE` access.

To open the key, use the `CreateKey()` or `OpenKey()` methods.

The length a value can have depends on the memory you have available. Values that run long (over 2048 bytes) are best kept as files, with the configuration registry holding the filenames instead. Doing so keeps the registry running efficiently.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.SetValue` with arguments `key`, `sub_key`, `type`, `value`.

 winreg.DisableReflectionKey(*key*)

Switches off registry reflection for 32-bit processes that run atop a 64-bit operating system.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

On a 32-bit operating system, running this will usually raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

When the key sits off the reflection list, the call returns successfully yet does nothing. Turning off reflection for one key leaves reflection of its subkeys untouched.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.DisableReflectionKey` with argument `key`.

 winreg.EnableReflectionKey(*key*)

Brings registry reflection back for the named key that was disabled.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

On a 32-bit operating system, running this will usually raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Bringing reflection back for a key leaves reflection of its subkeys untouched.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.EnableReflectionKey` with argument `key`.

[Subject index](INDEX.md) · [Previous](winreg-openkey-to-winreg-queryvalueex.md) · [Continue](winreg-queryreflectionkey.md) · [Owning module, declaration or section: Functions](winreg-closekey-to-winreg-createkeyex.md)
