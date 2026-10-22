# Access Rights

### Access Rights

For more information, see [Registry Key Security and Access](https://msdn.microsoft.com/en-us/library/ms724878%28v=VS.85%29.aspx).

 winreg.KEY_ALL_ACCESS

Combines the STANDARD_RIGHTS_REQUIRED, `KEY_QUERY_VALUE`, `KEY_SET_VALUE`, `KEY_CREATE_SUB_KEY`, `KEY_ENUMERATE_SUB_KEYS`, `KEY_NOTIFY`, and `KEY_CREATE_LINK` access rights.

 winreg.KEY_WRITE

Combines the STANDARD_RIGHTS_WRITE, `KEY_SET_VALUE`, and `KEY_CREATE_SUB_KEY` access rights.

 winreg.KEY_READ

Combines the STANDARD_RIGHTS_READ, `KEY_QUERY_VALUE`, `KEY_ENUMERATE_SUB_KEYS`, and `KEY_NOTIFY` values.

 winreg.KEY_EXECUTE

Equivalent to `KEY_READ`.

 winreg.KEY_QUERY_VALUE

Required to query the values of a registry key.

 winreg.KEY_SET_VALUE

Required to create, delete, or set a registry value.

 winreg.KEY_CREATE_SUB_KEY

Required to create a subkey of a registry key.

 winreg.KEY_ENUMERATE_SUB_KEYS

Required to enumerate the subkeys of a registry key.

 winreg.KEY_NOTIFY

Needed in order to ask for change notifications on a registry key, or on its subkeys.

 winreg.KEY_CREATE_LINK

Reserved for system use.

[Subject index](INDEX.md) · [Previous](winreg-hkey-classes-root-to-winreg-hkey-dyn-data.md) · [Continue](winreg-key-wow64-64key-to-winreg-key-wow64-32key.md)
