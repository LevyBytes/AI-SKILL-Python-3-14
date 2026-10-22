# Python 3.11.0 beta 1 / library / files and paths

[gh-91526](https://github.com/python/cpython/issues/91526): Drop the `os.device_encoding(file.fileno())` call inside `TextIOWrapper`. The call was convoluted, lacked documentation, and failed in the majority of situations. (Inada Naoki authored this patch.)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
