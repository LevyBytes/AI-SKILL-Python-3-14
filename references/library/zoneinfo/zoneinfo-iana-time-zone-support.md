# zoneinfo`zoneinfo` - IANA time zone support

# Zoneinfo

### `zoneinfo` - IANA time zone support

Added in version 3.9.

**Source code:** [Lib/zoneinfo](https://github.com/python/cpython/tree/3.14/Lib/zoneinfo)

---

A concrete time zone implementation backing the IANA time zone database, as first laid out in [**PEP 615**](https://peps.python.org/pep-0615/), is what the `zoneinfo` module delivers. Out of the box, `zoneinfo` draws on the system's time zone data where that exists; when no such system data is present, the library turns instead to the first-party [tzdata](https://pypi.org/project/tzdata/) package on PyPI.

See also

Module: [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime)

Supplies the [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) and [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) types meant to be used together with the `ZoneInfo` class.

Package [tzdata](https://pypi.org/project/tzdata/)

A first-party package that the CPython core developers keep up, distributing time zone data through PyPI.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is unavailable or non-functional. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

[Subject index](INDEX.md) · [Continue](using-zoneinfo.md)
