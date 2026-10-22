# `winreg` ? Windows registry access

# Winreg

### `winreg` — Windows registry access

---

This module makes the Windows registry API available from Python. Rather than representing a registry handle as a plain integer, a handle object is supplied so that handles get closed properly, even when the programmer forgets to close them explicitly.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Changed in version 3.3: A number of this module's functions formerly raised [`WindowsError`](https://docs.python.org/3.14/library/exceptions.html#WindowsError), which is today an alias for [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

[Subject index](INDEX.md) · [Continue](winreg-closekey-to-winreg-createkeyex.md)
