# time: POSIX timezone month-week-day transition rules

`start[/time], end[/time]`

Marks the moments at which DST begins and ends. Both the start and the end dates may be written in any one of these forms:

`J*n*`

The Julian day *n* (1 <= *n* <= 365). Because leap days go uncounted, February 28 lands on day 59 and March 1 on day 60 in every year.

`*n*`

The zero-indexed Julian day (0 <= *n* <= 365). Here leap days do count, which makes it possible to name February 29.

`M*m*.*n*.*d*`

The *d*’th day (0 <= *d* <= 6) within week *n* of month *m* across the year (1 <= *n* <= 5, 1 <= *m* <= 12, with a week 5 meaning “the final *d* day in month *m*”, landing in either the fourth or the fifth week). Week 1 denotes the earliest week that contains the *d*’th day. Day zero corresponds to Sunday.

`time` follows the same shape as `offset`, save that no leading sign (‘-’ or ‘+’) may appear. Should time be omitted, it defaults to 02:00:00.

```python
>>> os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
>>> time.tzset()
>>> time.strftime('%X %x %Z')
'02:07:36 05/08/03 EDT'
>>> os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
>>> time.tzset()
>>> time.strftime('%X %x %Z')
'16:08:12 05/08/03 AEST'

```

Across a good many Unix platforms (*BSD, Linux, Solaris, and Darwin among them), the handier route to defining timezone rules is the system’s own zoneinfo (*[tzfile(5)](https://manpages.debian.org/tzfile(5))*) database. You accomplish this by pointing the `TZ` environment variable at the desired timezone datafile’s path, taken relative to the root of the system’s ‘zoneinfo’ timezone database, which normally sits at `/usr/share/zoneinfo`. As examples, consider `'US/Eastern'`, `'Australia/Melbourne'`, `'Egypt'` or `'Europe/Amsterdam'`.

```python
>>> os.environ['TZ'] = 'US/Eastern'
>>> time.tzset()
>>> time.tzname
('EST', 'EDT')
>>> os.environ['TZ'] = 'Egypt'
>>> time.tzset()
>>> time.tzname
('EET', 'EEST')

```

[Subject index](INDEX.md) · [Previous](time-tzset.md) · [Continue](time-clock-boottime-to-time-clock-thread-cputime-id.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md)
