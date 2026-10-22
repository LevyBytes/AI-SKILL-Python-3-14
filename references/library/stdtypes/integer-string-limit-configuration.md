# Configuring integer string conversion limits

Should you settle on a low limit, put your application through rigorous testing. Arrange for the limit to take effect early — through either the environment or the flag — so that it is already in force at startup, and likewise throughout any install phase where Python might be called on to compile `.py` sources down to `.pyc` files.

### Recommended configuration

For the majority of programs, the out-of-the-box [`sys.int_info.default_max_str_digits`](https://docs.python.org/3.14/library/sys.html#sys.int_info.default_max_str_digits) ought to suffice. Where a program calls for some other limit, apply it at the main entry point and write the code so it stays agnostic across Python versions, since these APIs landed in security patch releases shipped prior to 3.12.

Example:

```python
>>> import sys
>>> if hasattr(sys, "set_int_max_str_digits"):
...     upper_bound = 68000
...     lower_bound = 4004
...     current_limit = sys.get_int_max_str_digits()
...     if current_limit == 0 or current_limit > upper_bound:
...         sys.set_int_max_str_digits(upper_bound)
...     elif current_limit < lower_bound:
...         sys.set_int_max_str_digits(lower_bound)

```

To switch it off completely, assign it a value of `0`.

Footnotes

[Subject index](INDEX.md)
