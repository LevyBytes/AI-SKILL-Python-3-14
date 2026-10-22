# Python 3.11.0 alpha 3 / library / tests and documentation

[bpo-45837](https://bugs.python.org/issue?@action=redirect&bpo=45837): Deprecated as far back as Python 3.1, `turtle.RawTurtle.settiltangle()` now raises a deprecation warning and is slated for removal in Python 3.13.

Reach for `turtle.RawTurtle.tiltangle()` in its place.

Previously `turtle.RawTurtle.tiltangle()` had been wrongly flagged as deprecated, and its docstring has since been put right.

Hugo van Kemenade supplied the patch.

[bpo-45507](https://bugs.python.org/issue?@action=redirect&bpo=45507): Supply tests covering truncated or missing trailers within the gzip.decompress implementation.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
