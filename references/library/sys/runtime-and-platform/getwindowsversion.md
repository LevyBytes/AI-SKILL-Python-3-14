# sys.getwindowsversion

sys.getwindowsversion()

Hand back a named tuple that describes the Windows version now in use. Its named members are *major*, *minor*, *build*, *platform*, *service_pack*, *service_pack_minor*, *service_pack_major*, *suite_mask*, *product_type* and *platform_version*. Here *service_pack* holds a string, *platform_version* a 3-tuple, and every remaining member is an integer. Since the pieces are reachable by name as well, `sys.getwindowsversion()[0]` matches `sys.getwindowsversion().major`. To stay compatible with earlier versions, only the first 5 members can be reached by indexing.

*platform* will be `2` (VER_PLATFORM_WIN32_NT).

*product_type* may be one of the following values:

| Constant | Meaning |
| --- | --- |
| `1` (VER_NT_WORKSTATION) | The system is a workstation. |
| `2` (VER_NT_DOMAIN_CONTROLLER) | The system is a domain controller. |
| `3` (VER_NT_SERVER) | The system is a server, but not a domain controller. |

This function is a wrapper around the Win32 `GetVersionEx()` function; consult Microsoft's documentation on `OSVERSIONINFOEX()` for fuller detail about these fields.

*platform_version* reports the major version, minor version and build number of the live operating system, instead of whatever version is being emulated for the process. Its purpose is logging, not feature detection.

Note

*platform_version* takes the version from kernel32.dll, which may carry a different version than the OS itself. For an accurate OS version, please rely on the [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform) module.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Changed in version 3.2: Switched to a named tuple, with *service_pack_minor*, *service_pack_major*, *suite_mask*, and *product_type* newly included.

Changed in version 3.6: Added *platform_version*

[API family](INDEX.md) · [sys context index](../INDEX.md).
