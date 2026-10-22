# zoneinfo — Configuring the data sources

### Configuring the data sources

Upon a `ZoneInfo(key)` call, the constructor begins by scanning the directories named in `TZPATH` for a file that matches `key`; should that fail, it then hunts for a match inside the tzdata package. Three avenues exist for configuring this behavior:

1.

When left unspecified, the default `TZPATH` may be set at compile time.

2.

An environment variable can configure `TZPATH`.

3.

While the program runs, the `reset_tzpath()` function can adjust the search path.

[Subject index](INDEX.md) · [Previous](data-sources.md) · [Continue](compile-time-configuration.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
