# platform — iOS platform

### iOS platform

 platform.ios_ver(*system=''*, *release=''*, *model=''*, *is_simulator=False*)

Collects iOS version details and hands them back as a [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) carrying these attributes:

- `system` holds the OS name — either `'iOS'` or `'iPadOS'`.

- `release` holds the iOS version number written as a string (for example `'17.2'`).

- `model` holds the device model identifier; for a physical device this reads like `'iPhone13,2'`, while on a simulator it reads `'iPhone'`.

- `is_simulator` holds a boolean telling you whether the app runs on a simulator or on real hardware.

Any entry that cannot be worked out takes the default supplied through its parameter.

[Subject index](INDEX.md) · [Previous](platform-mac-ver.md) · [Continue](platform-libc-ver.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
