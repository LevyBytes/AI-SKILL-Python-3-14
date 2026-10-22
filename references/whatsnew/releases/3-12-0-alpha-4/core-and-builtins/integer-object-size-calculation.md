# Python 3.12.0 alpha 4 / core and builtins / correct int sizeof computation element ob digit array counted false

[gh-100637](https://github.com/python/cpython/issues/100637): Correct the `int.__sizeof__()` computation so the 1-element `ob_digit` array is counted for `0` and `False`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
