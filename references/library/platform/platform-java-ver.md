# platform - Java platform

### Java platform

 platform.java_ver(*release=''*, *vendor=''*, *vminfo=('', '', '')*, *osinfo=('', '', '')*)

Version interface for Jython.

Hands back a tuple `(release, vendor, vminfo, osinfo)` in which *vminfo* is itself a tuple `(vm_name, vm_release, vm_vendor)` and *osinfo* a tuple `(os_name, os_version, os_arch)`. Any value that cannot be worked out takes the default supplied through its parameter (every one of which defaults to `''`).

Deprecated as of 3.13 and slated for removal in 3.15: it saw little testing, carried a confusing API, and served no purpose beyond Jython support.

[Subject index](INDEX.md) · [Previous](platform-release-to-platform-invalidate-caches.md) · [Continue](platform-win32-ver-to-platform-win32-is-iot.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
