# sys.int_info

sys.int_info

A [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying information about how Python represents integers internally. These attributes are read only.

 int_info.bits_per_digit

How many bits each digit carries. Internally, Python keeps integers in base `2**int_info.bits_per_digit`.

 int_info.sizeof_digit

The byte count of the C type that backs a single digit.

 int_info.default_max_str_digits

The default value for `sys.get_int_max_str_digits()` when it is not otherwise explicitly configured.

 int_info.str_digits_check_threshold

The minimum non-zero value for `sys.set_int_max_str_digits()`, [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS), or [`-X int_max_str_digits`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X).

Added in version 3.1.

Changed in version 3.11: Added `default_max_str_digits` and `str_digits_check_threshold`.

[API family](INDEX.md) · [sys context index](../INDEX.md).
