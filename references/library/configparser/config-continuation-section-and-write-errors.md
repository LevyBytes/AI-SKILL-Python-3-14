# Configuration continuation, section and write errors

Thrown if something goes wrong while trying to read through a file.

Changed in version 3.12: Gone now are the `filename` attribute together with the matching `__init__()` constructor argument. The equivalent has gone by the name `source` ever since 3.2.

`*exception *configparser.MultilineContinuationError`

Thrown if a key that has no matching value gets carried on across an indented line.

Added in version 3.13.

`*exception *configparser.UnnamedSectionDisabledError`

Thrown if you reach for `UNNAMED_SECTION` while it has not been turned on first.

>

Added in version 3.14.

`*exception *configparser.InvalidWriteError`

Thrown if a proposed `ConfigParser.write()` would fail to round-trip correctly through a later `ConfigParser.read()` call.

For instance, a key whose start matches the `ConfigParser.SECTCRE` pattern would, on reading, be mistaken for a section header. Any attempt to write such a key triggers this exception.

Added in version 3.14.

Footnotes

[Subject index](INDEX.md)
