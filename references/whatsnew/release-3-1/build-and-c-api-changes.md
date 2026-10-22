# What’s New In Python 3.1 / Build and C API Changes

When given a negative *pylong*, the [`PyLong_AsUnsignedLongLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsUnsignedLongLong) routine now reports the problem via [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) rather than the former [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

(Contributed by Mark Dickinson and Lisandro Dalcrin; [bpo-5175](https://bugs.python.org/issue?@action=redirect&bpo=5175).)

- Deprecated `PyNumber_Int()`. Use [`PyNumber_Long()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Long) instead.

(Contributed by Mark Dickinson; [bpo-4910](https://bugs.python.org/issue?@action=redirect&bpo=4910).)

- A fresh [`PyOS_string_to_double()`](https://docs.python.org/3.14/c-api/conversion.html#c.PyOS_string_to_double) routine was introduced, standing in for the now-deprecated `PyOS_ascii_strtod()` and `PyOS_ascii_atof()`.

(Contributed by Mark Dickinson; [bpo-5914](https://bugs.python.org/issue?@action=redirect&bpo=5914).)

- A new [`PyCapsule`](https://docs.python.org/3.14/c-api/capsule.html#c.PyCapsule) type was introduced to supersede the `PyCObject` API. What chiefly sets it apart is that this newer type offers a clearly specified way to convey type-safety details, plus a simpler calling convention for its destructor. Its predecessor carried a troublesome interface and has therefore been marked deprecated.

(Contributed by Larry Hastings; [bpo-5630](https://bugs.python.org/issue?@action=redirect&bpo=5630).)

### Build and C API Changes

Among the changes to Python’s build process and to the C API are:

- Internally, integers now sit in either base `2**15` or base `2**30`, with the base settled when Python is built. Before, they lived in base `2**15` at all times. Going with base `2**30` brings notable speed gains on 64-bit machines, while on 32-bit machines benchmarks came out mixed. So the default picks base `2**30` for 64-bit machines and base `2**15` for 32-bit machines; under Unix, a fresh configure option `--enable-big-digits` lets you override that default.

Beyond the speed gains, end users should see nothing of this change save for a single case: for testing and debugging there is now a new [`sys.int_info`](https://docs.python.org/3.14/library/sys.html#sys.int_info) reporting details of the internal format, namely the bit count per digit and the byte size of the C type holding each digit:

```python
>>> import sys
>>> sys.int_info
sys.int_info(bits_per_digit=30, sizeof_digit=4)

```

(Contributed by Mark Dickinson; [bpo-4258](https://bugs.python.org/issue?@action=redirect&bpo=4258).)

-

[Subject index](INDEX.md) · [Next source section](porting-to-python-3-1.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md) · [Previous source section](idle.md)
