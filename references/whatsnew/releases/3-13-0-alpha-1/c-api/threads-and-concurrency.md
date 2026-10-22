# Python 3.13.0 alpha 1 / c api / threads and concurrency

[gh-105603](https://github.com/python/cpython/issues/105603): The `PyInterpreterConfig.own_gil` field added in 3.12 has been renamed to `PyInterpreterConfig.gil`, and its value type shifts from ?bool? to an integer accepting `PyInterpreterConfig_DEFAULT_GIL`, `PyInterpreterConfig_SHARED_GIL`, and `PyInterpreterConfig_OWN_GIL`. ?shared? is the default.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
