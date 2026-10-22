# time — `time` — Time access and conversions

### `time` — Time access and conversions

---

A collection of functions dealing with time lives in this module. The [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) and [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar) modules cover adjacent functionality and are worth a look too.

The module itself ships everywhere, yet a given function may be absent on some platforms. The majority of what this module defines simply forwards to identically named routines in the platform's C library. Reaching for the platform documentation can pay off occasionally, since how these routines behave is not uniform from one platform to the next.

A few terms and conventions deserve clarification before going further.

- The *epoch* marks where time begins — the value you get back from `time.gmtime(0)`. Across every platform that is January 1, 1970, 00:00:00 (UTC).

- What we call *seconds since the epoch* is simply how many seconds have gone by since the epoch, and ordinarily [leap seconds](https://en.wikipedia.org/wiki/Leap_second) are left out of that count. Every POSIX-compliant platform omits leap seconds from this tally.

- Dates and times that fall before the epoch, or that sit far ahead of us, may be beyond what these functions can manage. Where the upper bound lands is set by the C library; on 32-bit systems that ceiling usually arrives around 2038.

- Feed the `%y` format code to `strptime()` and it will read 2-digit years. The conversion of such years follows the POSIX and ISO C standards: the range 69–99 lands in 1969–1999, while 0–68 lands in 2000–2068.

- UTC stands for [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time); it took over from [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time), or GMT, as the foundation for keeping time worldwide. Rather than being a typo, the acronym UTC follows the older, language-neutral pattern used to label time standards like UT0, UT1, and UT2.

- DST stands for Daylight Saving Time, a shift of the timezone by (typically) one hour over a stretch of the year. The rules for DST are magic (set by local law) and may differ from one year to the next. A table of these local rules lives in the C library (frequently loaded from a system file so it stays adjustable), and it serves as the single fount of True Wisdom on the subject.

- How precise the assorted real-time functions actually are can fall short of what the units of their value or argument would imply. For instance, the clock on most Unix systems only "ticks" 50 or 100 times per second.

- By contrast, `time()` and `sleep()` are more precise than their Unix counterparts: their times come as floating-point numbers, `time()` hands back the most precise time it can obtain (drawing on Unix `gettimeofday()` when that exists), and `sleep()` will tolerate a time carrying a nonzero fraction (this leans on Unix `select()` wherever it is available).

- The time value handed back by `gmtime()`, `localtime()`, and `strptime()`, and taken in by `asctime()`, `mktime()` and `strftime()`, comes as a sequence of 9 integers. What `gmtime()`, `localtime()`, and `strptime()` return additionally exposes attribute names for the separate fields.

Consult `struct_time` for what these objects look like.

Changed in version 3.3: When the platform exposes the matching `struct tm` members, the `struct_time` type gained the `tm_gmtoff` and `tm_zone` attributes.

Changed in version 3.6: Every platform now offers the `tm_gmtoff` and `tm_zone` attributes of `struct_time`.

- Convert between the various time representations with the functions below:

| From | To | Use |
| --- | --- | --- |
| seconds since the epoch | `struct_time` in UTC | `gmtime()` |
| seconds since the epoch | `struct_time` in local time | `localtime()` |
| `struct_time` in UTC | seconds since the epoch | `calendar.timegm()` |
| `struct_time` in local time | seconds since the epoch | `mktime()` |

[Subject index](INDEX.md) · [Continue](time-asctime-to-time-ctime.md)
