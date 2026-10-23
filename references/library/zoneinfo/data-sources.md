# zoneinfo - Data sources

### Data sources

Time zone data is not furnished directly by the `zoneinfo` module; rather, it draws that information from the system time zone database or, where present, the first-party PyPI package [tzdata](https://pypi.org/project/tzdata/). Certain systems — Windows being a prominent case — ship without an IANA database, so any project aiming for cross-platform compatibility that depends on time zone data is advised to declare a dependency on tzdata. Where neither system data nor tzdata can be found, every call to `ZoneInfo` raises `ZoneInfoNotFoundError`.

[Subject index](INDEX.md) · [Previous](using-zoneinfo.md) · [Continue](configuring-the-data-sources.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
