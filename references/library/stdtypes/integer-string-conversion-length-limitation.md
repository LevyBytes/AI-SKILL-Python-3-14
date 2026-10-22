# Integer string conversion length limitation

### Integer string conversion length limitation

To blunt denial of service attacks, CPython enforces a global cap on converting between [`int`](https://docs.python.org/3.14/library/functions.html#int) and `str`. That cap *only* covers decimal and other non-power-of-two number bases. Conversions in hexadecimal, octal, and binary stay unlimited. The cap is configurable.

Within CPython the [`int`](https://docs.python.org/3.14/library/functions.html#int) type is an arbitrary length number kept in binary form (widely called a “bignum”). No algorithm can turn a string into a binary integer (or the reverse) within linear time whenever the base happens not to be a power of 2. Even the strongest known base 10 algorithms run with sub-quadratic complexity. Converting something large, say `int('1' * 500_000)`, may run for more than a second on a quick CPU.

Capping the conversion size gives a workable means of dodging [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735).

The cap covers the count of digit characters in the input or output string in cases where a non-linear conversion algorithm would come into play. Underscores together with the sign do not count against the cap.

Whenever an operation would push past the cap, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised:

```pycon
>>> import sys
>>> sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
>>> _ = int('2' * 5432)
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5432 digits; use sys.set_int_max_str_digits() to increase the limit
>>> i = int('2' * 4300)
>>> len(str(i))
4300
>>> i_squared = i*i
>>> len(str(i_squared))
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
>>> len(hex(i_squared))
7144
>>> assert int(hex(i_squared), base=16) == i*i  # Hexadecimal is unlimited.

```

By default the cap sits at 4300 digits, as given by [`sys.int_info.default_max_str_digits`](https://docs.python.org/3.14/library/sys.html#sys.int_info). The smallest cap you may configure is 640 digits, as given by `sys.int_info.str_digits_check_threshold`.

Verification:

```pycon
>>> import sys
>>> assert sys.int_info.default_max_str_digits == 4300, sys.int_info
>>> assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
>>> msg = int('578966293710682886880994035146873798396722250538762761564'
...           '9252925514383915483333812743580549779436104706260696366600'
...           '571186405732').to_bytes(53, 'big')
...

```

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](definition-name-to-definition-type-params.md) · [Continue](affected-apis.md)
