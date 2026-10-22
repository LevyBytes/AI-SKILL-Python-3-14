# sys.platform

sys.platform

A string holding a platform identifier. The recognized values are:

| System | `platform` value |
| --- | --- |
| AIX | `'aix'` |
| Android | `'android'` |
| Emscripten | `'emscripten'` |
| FreeBSD | `'freebsd'` |
| iOS | `'ios'` |
| Linux | `'linux'` |
| macOS | `'darwin'` |
| Windows | `'win32'` |
| Windows/Cygwin | `'cygwin'` |
| WASI | `'wasi'` |

On Unix systems absent from the table, the value is the lowercased OS name reported by `uname -s`, with the leading portion of the version reported by `uname -r` appended, e.g. `'sunos5'`, *at the time when Python was built*. So unless you need to check for a particular system version, the recommended idiom is the following:

```python
if sys.platform.startswith('sunos'):
    # SunOS-specific code here...

```

Changed in version 3.3: On Linux, `sys.platform` no longer carries the major version. It is always `'linux'`, rather than `'linux2'` or `'linux3'`.

Changed in version 3.8: On AIX, `sys.platform` no longer carries the major version. It is always `'aix'`, rather than `'aix5'` or `'aix7'`.

Changed in version 3.13: On Android, `sys.platform` now yields `'android'` in place of `'linux'`.

Changed in version 3.14: On FreeBSD, `sys.platform` no longer carries the major version. It is always `'freebsd'`, rather than `'freebsd13'` or `'freebsd14'`.

See also

[`os.name`](https://docs.python.org/3.14/library/os.html#os.name) offers a coarser granularity. [`os.uname()`](https://docs.python.org/3.14/library/os.html#os.uname) supplies system-dependent version information.

The [`platform`](https://docs.python.org/3.14/library/platform.html#module-platform) module supplies thorough checks of the system’s identity.

[API family](INDEX.md) · [sys context index](../INDEX.md).
