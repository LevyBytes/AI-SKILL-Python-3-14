# Python 3.9.0 alpha 5 / library / ensurepip

[bpo-38662](https://bugs.python.org/issue?@action=redirect&bpo=38662): `pip` is now launched by the `ensurepip` module through the `runpy` module. As a result, it has shed its tight coupling to the internal API of the bundled `pip` release, which makes moving to a newer `pip` version simpler both internally and for distributors.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
