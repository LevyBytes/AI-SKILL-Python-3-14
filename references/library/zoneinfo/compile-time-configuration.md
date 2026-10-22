# zoneinfo — Compile-time configuration

#### Compile-time configuration

By default `TZPATH` covers a handful of widespread deployment spots for the time zone database (Windows being the exception, since it has no “well-known” spots for time zone data). On POSIX systems, downstream distributors and anyone building Python from source who knows where their system's time zone data lives can override the default time zone path through the compile-time option `TZPATH` (or, more commonly, the [`configure flag --with-tzpath`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-tzpath)), which is expected to be a string separated by [`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep).

Across every platform, you can read the configured value back out via the `TZPATH` key of [`sysconfig.get_config_var()`](https://docs.python.org/3.14/library/sysconfig.html#sysconfig.get_config_var).

[Subject index](INDEX.md) · [Previous](configuring-the-data-sources.md) · [Continue](environment-configuration.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
