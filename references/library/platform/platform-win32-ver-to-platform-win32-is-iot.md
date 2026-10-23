# platform - Windows platform

### Windows platform

 platform.win32_ver(*release=''*, *version=''*, *csd=''*, *ptype=''*)

Pulls extra version details out of the Windows Registry and hands back a tuple `(release, version, csd, ptype)` that maps to the OS release, the version number, the CSD level (service pack) and the OS type (multi/single processor). Any value that cannot be worked out takes the default supplied through its parameter (each of which defaults to an empty string).

By way of a hint: *ptype* reads `'Uniprocessor Free'` on single-processor NT machines and `'Multiprocessor Free'` on multi-processor ones. Here `'Free'` signals that the OS version carries no debugging code. It may alternatively read `'Checked'`, meaning the OS version does include debugging code — code that vets arguments, ranges, and so forth.

 platform.win32_edition()

Hands back a string standing for the Windows edition in use, or `None` when the value cannot be worked out. Among the possible values — though not the only ones — are `'Enterprise'`, `'IoTUAP'`, `'ServerStandard'`, and `'nanoserver'`.

Added in version 3.8.

 platform.win32_is_iot()

Hands back `True` whenever the Windows edition that `win32_edition()` reports counts as an IoT edition.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](platform-java-ver.md) · [Continue](platform-mac-ver.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
