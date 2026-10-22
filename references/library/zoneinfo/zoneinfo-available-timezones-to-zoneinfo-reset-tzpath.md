# zoneinfo — Functions

### Functions

 zoneinfo.available_timezones()

Fetch a set holding every valid key for the IANA time zones reachable anywhere along the time zone path. The result is recomputed on each call to the function.

Only canonical zone names appear in this function's output; it leaves out “special” zones, like those beneath the `posix/` and `right/` directories or the `posixrules` zone.

Caution

This function might open quite a lot of files, since reading the “magic string” at the start is the surest way to tell whether a file on the time zone path is a valid time zone.

Note

These values aren't meant for display to end users; for user-facing elements, an application ought to lean on something like CLDR (the Unicode Common Locale Data Repository) for friendlier strings. See also the cautionary note attached to `ZoneInfo.key`.

`zoneinfo.reset_tzpath(*to=None*)`

Establishes or resets the module's time zone search path (`TZPATH`). Called with no arguments, `TZPATH` reverts to its default value.

A call to `reset_tzpath` does not invalidate the `ZoneInfo` cache, so the primary `ZoneInfo` constructor only picks up the new `TZPATH` upon a cache miss.

The `to` parameter has to be a [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) of strings or [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) — not a string itself — with each entry an absolute path. Pass anything other than an absolute path and [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

[Subject index](INDEX.md) · [Previous](pickle-serialization.md) · [Continue](zoneinfo-tzpath.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
