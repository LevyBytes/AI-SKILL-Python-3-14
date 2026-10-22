# Python 3.10.0 alpha 4 / library / importlib metadata

[bpo-42382](https://bugs.python.org/issue?@action=redirect&bpo=42382): Within `importlib.metadata`: - `EntryPoint` objects now carry a `.dist` object that points to the `Distribution` whenever they are built out of a `Distribution`. - Package discovery now honors package normalization rules. - What `metadata()` hands back now follows a formally specified protocol named `PackageMetadata`, which declares the `.get_all()` method. - Brought into sync with importlib_metadata 3.3.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
