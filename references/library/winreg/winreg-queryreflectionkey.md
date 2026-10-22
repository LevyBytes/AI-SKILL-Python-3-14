# Functions: `winreg.QueryReflectionKey()`

winreg.QueryReflectionKey(*key*)

Works out what the reflection state is for the named key.

*key* is a key that is already open, or else one of the predefined HKEY_* constants.

Returns `True` if reflection is disabled.

On a 32-bit operating system, running this will usually raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `winreg.QueryReflectionKey` with argument `key`.

[Subject index](INDEX.md) · [Previous](winreg-savekey-to-winreg-enablereflectionkey.md) · [Continue](constants.md) · [Owning module, declaration or section: Functions](winreg-closekey-to-winreg-createkeyex.md)
