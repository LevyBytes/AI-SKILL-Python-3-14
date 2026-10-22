# What's new in Python 3.14 / `build-details.json` — sysconfig

### `build-details.json`

A new file named `build-details.json` now ships inside Python installations. It is a static JSON document recording how CPython was built, enabling introspection that does not require running any code. Such data helps with cases like Python launchers, cross-compilation, and similar needs.

The `build-details.json` file has to land in the platform-independent standard library directory. That maps to the ["stdlib"](https://docs.python.org/3.14/library/sysconfig.html#installation-paths) [`sysconfig`](https://docs.python.org/3.14/library/sysconfig.html#module-sysconfig) installation path, discoverable by calling `sysconfig.get_path('stdlib')`.

See also

[**PEP 739**](https://peps.python.org/pep-0739/) — `build-details.json` 1.0 — a static description file for Python build details

[Subject index](INDEX.md) · [Previous source section](build-changes.md) · [Next source section](discontinuation-of-pgp-signatures.md) · [Release/subject declaration](summary-release-highlights.md)
