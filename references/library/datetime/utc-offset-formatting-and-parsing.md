# UTC offset formatting and strptime directives

Changed in version 3.7: Where the `%z` directive reaches the `strptime()` method, a colon is permitted within UTC offsets to divide the hours, minutes and seconds. To illustrate, `'+01:00:00'` reads as a one-hour offset. On top of that, handing over `'Z'` carries the same meaning as `'+00:00'`.

`%:z`

Acts just like `%z`, except that a colon now divides the hours, minutes and seconds.

`%Z`

Within `strftime()`, should `tzname()` yield `None`, the `%Z` token expands to an empty string; failing that, `%Z` takes on whatever value was returned, and that value has to be a string.

`strptime()` only accepts certain values for `%Z`:

  1.

any value in `time.tzname` for your machine’s locale

  2.

the hard-coded values `UTC` and `GMT`

Thus a person based in Japan might count `JST`, `UTC`, and `GMT` among the acceptable entries, though almost certainly not `EST`. Anything outside the allowed set triggers a `ValueError`.

Changed in version 3.2: Once the `%z` directive is handed to the `strptime()` method, what comes back is an aware `datetime` object. That result has its `tzinfo` populated with a `timezone` instance.

7.

Under the `strptime()` method, `%U` along with `%W` factor into the computation solely when both the weekday and the calendar year (`%Y`) have been supplied.

8.

Much as with `%U` and `%W`, the `%V` token enters the math only where a `strptime()` format string names both the weekday and the ISO year (`%G`). Bear in mind, too, that `%G` cannot stand in for `%Y`.

9.

With the `strptime()` method in play, you may drop the leading zero for the formats `%d`, `%m`, `%H`, `%I`, `%M`, `%S`, `%j`, `%U`, `%W`, and `%V`. The `%y` format, by contrast, insists on a leading zero.

10.

Whenever `strptime()` reads a month together with a day, be sure the format also carries a year. Where the text you are parsing omits a year, tack on a deliberate placeholder leap year. Skip that step and your program throws an exception on leap day, since the parser's fallback year (1900) happens not to be a leap year. People keep tripping over this defect each leap year.

```pycon
>>> month_day = "02/29"
>>> dt.datetime.strptime(f"{month_day};1984", "%m/%d;%Y")  # No leap year bug.
datetime.datetime(1984, 2, 29, 0, 0)

```

Deprecated since version 3.13, will be removed in version 3.15: Any `strptime()` invocation whose format string holds a day of month yet no year will from now on raise a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Come 3.15 or afterward, this might be turned into an outright error, or the fallback year might be shifted to a leap year. Consult [gh-70647](https://github.com/python/cpython/issues/70647).

Footnotes

[Subject index](INDEX.md)
