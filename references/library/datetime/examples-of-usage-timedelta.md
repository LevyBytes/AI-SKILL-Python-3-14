# datetime - Examples of usage: `timedelta`

### Examples of usage: `timedelta`

One more normalization example:

```python
>>> # Components of another_year add up to exactly 365 days
>>> import datetime as dt
>>> year = dt.timedelta(days=365)
>>> another_year = dt.timedelta(weeks=40, days=84, hours=23,
...                             minutes=50, seconds=600)
>>> year == another_year
True
>>> year.total_seconds()
31536000.0

```

Examples of `timedelta` arithmetic:

```python
>>> import datetime as dt
>>> year = dt.timedelta(days=365)
>>> ten_years = 10 * year
>>> ten_years
datetime.timedelta(days=3650)
>>> ten_years.days // 365
10
>>> nine_years = ten_years - year
>>> nine_years
datetime.timedelta(days=3285)
>>> three_years = nine_years // 3
>>> three_years, three_years.days // 365
(datetime.timedelta(days=1095), 3)

```

[Subject index](INDEX.md) · [Previous](timedelta-microseconds-to-timedelta-total-seconds.md) · [Continue](datetime-date-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md)
