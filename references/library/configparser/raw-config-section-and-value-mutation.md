# configparser.RawConfigParser: `add_section()`, `set()`

add_section(*section*)

Add a section named *section* or `UNNAMED_SECTION` to the instance.

When the given section already exists, `DuplicateSectionError` is raised. When the *default section* name is supplied, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. When `UNNAMED_SECTION` is supplied while support is turned off, `UnnamedSectionDisabledError` is raised.

The type of *section* goes unchecked, which permits users to create non-string named sections. That behaviour is unsupported and may trigger internal errors.

Changed in version 3.14: Added support for `UNNAMED_SECTION`.

 set(*section*, *option*, *value*)

When the given section exists, set the given option to the supplied value; otherwise raise `NoSectionError`. It is possible to keep non-string values *internally* through `RawConfigParser` (or via `ConfigParser` when its *raw* parameters are turned on), yet the full feature set — interpolation plus writing out to files — works solely with string values.

Through this method users can stash non-string values against keys internally. That behaviour is unsupported and breaks down with errors the moment you write to a file or fetch it outside raw mode. **Use the mapping protocol API**, since under it no such assignment is ever permitted.

[Subject index](INDEX.md) · [Previous](configparser-rawconfigparser-class.md) · [Continue](configparser-error-to-configparser-parsingerror.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: configparser.RawConfigParser](configparser-rawconfigparser-class.md) · [Owning module, declaration or section: RawConfigParser Objects](configparser-rawconfigparser-class.md)
