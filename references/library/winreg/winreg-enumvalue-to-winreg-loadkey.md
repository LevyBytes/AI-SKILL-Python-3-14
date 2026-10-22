# Functions: `winreg.EnumValue()`, `winreg.ExpandEnvironmentStrings()`, `winreg.FlushKey()`, `winreg.LoadKey()`

winreg.EnumValue(*key*, *index*)

Walks through the values of an open registry key, giving back a tuple.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

*index* is an integer pinpointing the index of the value you want fetched.

On every invocation the function returns one subkey's name. Typically you keep invoking it over and over until an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) exception is raised, marking that nothing else is left.

What you get is a tuple holding 3 items:

| Index | Meaning |
| --- | --- |
| `0` | A string that identifies the value name |
| `1` | An object carrying the value data, whose type hinges on the underlying registry type |
| `2` | An integer naming the type of the value data (consult the table in the docs for `SetValueEx()`) |

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.EnumValue` with arguments `key`, `index`.

Changed in version 3.3: See above.

 winreg.ExpandEnvironmentStrings(*str*)

Expands environment variable placeholders `%NAME%` in strings like `REG_EXPAND_SZ`:

```python
>>> ExpandEnvironmentStrings('%windir%')
'C:\\Windows'

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.ExpandEnvironmentStrings` with argument `str`.

 winreg.FlushKey(*key*)

Writes all the attributes of a key to the registry.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

Calling `FlushKey()` to alter a key is unnecessary. The registry's lazy flusher takes care of moving registry edits to disk. Such edits also get flushed to disk when the system shuts down. In contrast to `CloseKey()`, the `FlushKey()` method comes back only after every piece of data has landed in the registry. A program ought to invoke `FlushKey()` solely when it demands complete assurance that registry edits are on disk.

Note

When you're unsure whether a `FlushKey()` call is needed, the odds are it isn't.

 winreg.LoadKey(*key*, *sub_key*, *file_name*)

Builds a subkey beneath the named key and loads registration data drawn from a given file into that subkey.

*key* is a handle returned by `ConnectRegistry()` or one of the constants `HKEY_USERS` or `HKEY_LOCAL_MACHINE`.

*sub_key* is a string that identifies the subkey to load.

*file_name* gives the name of the file that registry data is read from. The `SaveKey()` function must have produced this file. On a file allocation table (FAT) file system, the filename is not allowed to carry an extension.

When the calling process lacks the `SE_RESTORE_PRIVILEGE` privilege, the `LoadKey()` call fails. Be aware that privileges and permissions are not the same thing ? consult the [RegLoadKey documentation](https://msdn.microsoft.com/en-us/library/ms724889%28v=VS.85%29.aspx) for further details.

When *key* is a handle that `ConnectRegistry()` returned, the path given in *file_name* is taken relative to the remote computer.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.LoadKey` with arguments `key`, `sub_key`, `file_name`.

[Subject index](INDEX.md) · [Previous](winreg-deletekey-to-winreg-enumkey.md) · [Continue](winreg-openkey-to-winreg-queryvalueex.md) · [Owning module, declaration or section: Functions](winreg-closekey-to-winreg-createkeyex.md)
