# Python 3.10.0 alpha 2 / library / zipfile

[bpo-42043](https://bugs.python.org/issue?@action=redirect&bpo=42043): Allow `zipfile.Path` to be subclassed. For names that do not exist, `zipfile.Path.is_file()` now reports False. A `.filename` attribute is now surfaced on `zipfile.Path` objects, and that attribute backs the resolution of `.name` and `.parent` when the `Path` object sits at the zipfile's root.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
