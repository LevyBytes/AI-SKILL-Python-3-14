# What's New In Python 3.2 / datetime and time - datetime

### datetime and time

- A fresh type [`timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone) now lives in the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module; it realizes the [`tzinfo`](https://docs.python.org/3.14/library/datetime.html#datetime.tzinfo) interface by handing back a fixed UTC offset together with a timezone name. That eases the construction of timezone-aware datetime objects:

```python
>>> import datetime as dt

>>> dt.datetime.now(dt.timezone.utc)
datetime.datetime(2010, 12, 8, 21, 4, 2, 923754, tzinfo=datetime.timezone.utc)

>>> dt.datetime.strptime("01/01/2000 12:00 +0000", "%m/%d/%Y %H:%M %z")
datetime.datetime(2000, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)

```

- On top of that, [`timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) objects may now be multiplied by [`float`](https://docs.python.org/3.14/library/functions.html#float) and divided by `float` along with [`int`](https://docs.python.org/3.14/library/functions.html#int) objects. Plus `timedelta` objects can now divide each other.

- No longer is the [`datetime.date.strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.strftime) method confined to years past 1900. The fresh supported year span runs from 1000 through 9999 inclusive.

- Any time a two-digit year shows up in a time tuple, `time.accept2dyear` has dictated the reading. Its default of `True` means that for a two-digit year the century is inferred per the POSIX rules covering the `%y` strptime format.

From Py3.2 onward, relying on the century-guessing heuristic raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). The advised approach is to assign `time.accept2dyear` a value of `False`, which lets wide date spans be handled without any guessing:

```python
>>> import time, warnings
>>> warnings.resetwarnings()      # remove the default warning filters

>>> time.accept2dyear = True      # guess whether 11 means 11 or 2011
>>> time.asctime((11, 1, 1, 12, 34, 56, 4, 1, 0))
Warning (from warnings module):
  ...
DeprecationWarning: Century info guessed for a 2-digit year.
'Fri Jan  1 12:34:56 2011'

>>> time.accept2dyear = False     # use the full range of allowable dates
>>> time.asctime((11, 1, 1, 12, 34, 56, 4, 1, 0))
'Fri Jan  1 12:34:56 11'

```

A handful of functions gained much broader acceptable date spans. With `time.accept2dyear` set to false, [`time.asctime()`](https://docs.python.org/3.14/library/time.html#time.asctime) takes any year representable as a C int, whereas [`time.mktime()`](https://docs.python.org/3.14/library/time.html#time.mktime) together with [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) honor whatever range the underlying operating system routines permit.

(Contributed by Alexander Belopolsky and Victor Stinner in [bpo-1289118](https://bugs.python.org/issue?@action=redirect&bpo=1289118), [bpo-5094](https://bugs.python.org/issue?@action=redirect&bpo=5094), [bpo-6641](https://bugs.python.org/issue?@action=redirect&bpo=6641), [bpo-2706](https://bugs.python.org/issue?@action=redirect&bpo=2706), [bpo-1777412](https://bugs.python.org/issue?@action=redirect&bpo=1777412), [bpo-8013](https://bugs.python.org/issue?@action=redirect&bpo=8013), and [bpo-10827](https://bugs.python.org/issue?@action=redirect&bpo=10827).)

[Subject index](INDEX.md) · [Previous source section](threading.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Next source section](math.md)
