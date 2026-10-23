# zoneinfo - Exceptions and warnings

### Exceptions and warnings

`*exception *zoneinfo.ZoneInfoNotFoundError`

Raised when building a `ZoneInfo` object fails because the named key turned up nowhere on the system. It is a subclass of [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

`*exception *zoneinfo.InvalidTZPathWarning`

Raised when `PYTHONTZPATH` holds an invalid component, such as a relative path, that ends up filtered out.

[Subject index](INDEX.md) · [Previous](zoneinfo-tzpath.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
