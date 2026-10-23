# zoneinfo - Globals

### Globals

 zoneinfo.TZPATH

A read-only sequence standing for the time zone search path – while building a `ZoneInfo` from a key, that key is joined onto each entry of the `TZPATH`, and the first file located is the one used.

Whatever its configuration, `TZPATH` is allowed to hold absolute paths exclusively and never relative ones.

A call to `reset_tzpath()` can swap out the object that `zoneinfo.TZPATH` references, which is why the advice is to refer to `zoneinfo.TZPATH` directly rather than importing `TZPATH` from `zoneinfo` or pinning a long-lived variable to `zoneinfo.TZPATH`.

For further detail on configuring the time zone search path, consult Configuring the data sources.

[Subject index](INDEX.md) · [Previous](zoneinfo-available-timezones-to-zoneinfo-reset-tzpath.md) · [Continue](timezone-data-errors-and-path-warnings.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
