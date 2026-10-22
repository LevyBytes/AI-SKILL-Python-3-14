# Configuring the limit

### Configuring the limit

Ahead of Python’s startup you may set the cap through an environment variable or an interpreter command line flag:

- [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS), for instance `PYTHONINTMAXSTRDIGITS=640 python3` to put the cap at 640, or `PYTHONINTMAXSTRDIGITS=0 python3` to switch the limitation off.

- [`-X int_max_str_digits`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X), for instance `python3 -X int_max_str_digits=640`

- [`sys.flags.int_max_str_digits`](https://docs.python.org/3.14/library/sys.html#sys.flags.int_max_str_digits) holds the value of [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS) or [`-X int_max_str_digits`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X). When both the env var and the `-X` option are present, the `-X` option wins. A value of *-1* signals that neither was set, so a value of [`sys.int_info.default_max_str_digits`](https://docs.python.org/3.14/library/sys.html#sys.int_info.default_max_str_digits) was applied during initialization.

From within code, you can read the current cap and assign a new one through these [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) APIs:

- [`sys.get_int_max_str_digits()`](https://docs.python.org/3.14/library/sys.html#sys.get_int_max_str_digits) and [`sys.set_int_max_str_digits()`](https://docs.python.org/3.14/library/sys.html#sys.set_int_max_str_digits) form a getter and setter for the interpreter-wide cap. Each subinterpreter keeps its own cap.

Details on the default and the minimum live in [`sys.int_info`](https://docs.python.org/3.14/library/sys.html#sys.int_info):

- [`sys.int_info.default_max_str_digits`](https://docs.python.org/3.14/library/sys.html#sys.int_info) is the compiled-in default cap.

- [`sys.int_info.str_digits_check_threshold`](https://docs.python.org/3.14/library/sys.html#sys.int_info) is the smallest cap value accepted (apart from 0, which turns it off).

Added in version 3.11.

Caution

Choosing a low cap *can* bring on trouble. Though uncommon, some code carries integer constants written in decimal in its source that go beyond the minimum threshold. One side effect of setting the cap is that Python source code holding decimal integer literals longer than the cap will hit an error while parsing, generally at startup time or import time or even at installation time — any moment when an up to date `.pyc` is not already present for the code. For source carrying constants that large, the workaround is to rewrite them in `0x` hexadecimal form, since that carries no cap.

[Subject index](INDEX.md) · [Previous](affected-apis.md)
