# platform - macOS platform

### macOS platform

 platform.mac_ver(*release=''*, *versioninfo=('', '', '')*, *machine=''*)

Collects macOS version details and hands them back as the tuple `(release, versioninfo, machine)`, where *versioninfo* is itself a tuple `(version, dev_stage, non_release_version)`.

Any entry that cannot be worked out is set to `''`. Every tuple entry is a string.

[Subject index](INDEX.md) · [Previous](platform-win32-ver-to-platform-win32-is-iot.md) · [Continue](platform-ios-ver.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)
