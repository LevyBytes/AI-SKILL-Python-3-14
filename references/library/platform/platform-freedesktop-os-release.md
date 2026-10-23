# platform - Linux platforms

### Linux platforms

 platform.freedesktop_os_release()

Reads operating-system identification out of the `os-release` file and hands it back as a dict. That `os-release` file follows a [freedesktop.org standard](https://www.freedesktop.org/software/systemd/man/os-release.html) and ships with the bulk of Linux distributions — Android and the distributions built atop it being a conspicuous exception.

Throws [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) (or a subclass) whenever neither `/etc/os-release` nor `/usr/lib/os-release` proves readable.

When it succeeds, the function hands back a dictionary whose keys and values are all strings. The values have special characters such as `"` and `$` stripped of their quoting. Per the standard, the `NAME`, `ID`, and `PRETTY_NAME` fields are always present; every other field is optional, and vendors are free to tack on more.

Bear in mind that fields like `NAME`, `VERSION`, and `VARIANT` are strings fit to show to users. To tell Linux distributions apart, programs ought to lean on fields such as `ID`, `ID_LIKE`, `VERSION_ID`, or `VARIANT_ID`.

Example:

```python
def get_like_distro():
    info = platform.freedesktop_os_release()
    ids = [info["ID"]]
    if "ID_LIKE" in info:
        # ids are space separated and ordered by precedence
        ids.extend(info["ID_LIKE"].split())
    return ids

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](platform-libc-ver.md) · [Continue](platform-android-ver.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
