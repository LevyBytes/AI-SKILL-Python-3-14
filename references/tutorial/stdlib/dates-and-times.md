# 10.8. Dates and times

### 10.8. Dates and times

Classes for handling dates and times — whether the task is easy or involved — come from the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module. Arithmetic on dates and times is available, yet the design concentrates on pulling out members efficiently for formatting and reshaping output. Timezone-aware objects are supported by the module as well.

```python
>>> # dates are easily constructed and formatted
>>> import datetime as dt
>>> now = dt.date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = dt.date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368

```

[Subject index](INDEX.md) · [Previous source section](internet-access.md) · [Following source section](data-compression.md)
