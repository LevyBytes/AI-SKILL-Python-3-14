# platform — Unix platforms

### Unix platforms

 platform.libc_ver(*executable=sys.executable*, *lib=''*, *version=''*, *chunksize=16384*)

Attempts to work out which libc version the file executable (the Python interpreter by default) was linked against. Hands back a tuple of strings `(lib, version)` that fall back to the supplied parameters should the lookup come up empty.

Bear in mind that this function relies on close knowledge of how the various libc versions append symbols to the executable, so it is likely serviceable only for executables built with **gcc**.

The file gets read and scanned in *chunksize*-byte chunks.

[Subject index](INDEX.md) · [Previous](platform-ios-ver.md) · [Continue](platform-freedesktop-os-release.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
