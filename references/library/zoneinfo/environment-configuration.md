# zoneinfo - Environment configuration

#### Environment configuration

While `TZPATH` is being initialized (at import time, or any time `reset_tzpath()` runs without arguments), the `zoneinfo` module consults the environment variable `PYTHONTZPATH`, should it exist, to establish the search path.

 PYTHONTZPATH

A string, separated by [`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep), that holds the time zone search path to apply. Only absolute paths are permitted, never relative ones. Relative pieces given inside `PYTHONTZPATH` are skipped, though beyond that the response to a relative path is left up to the implementation; CPython issues an `InvalidTZPathWarning`, whereas other implementations may quietly drop the bad component or raise an exception instead.

If you want the system to disregard its own data and rely on the tzdata package, assign `PYTHONTZPATH=""`.

[Subject index](INDEX.md) · [Previous](compile-time-configuration.md) · [Continue](runtime-configuration.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
