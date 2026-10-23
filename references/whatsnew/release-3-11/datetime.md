# What's New In Python 3.11 / datetime - datetime

### datetime

- [`datetime.UTC`](https://docs.python.org/3.14/library/datetime.html#datetime.UTC) was added as a handy shorthand for [`datetime.timezone.utc`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone.utc). (Contributed by Kabir Kwatra in [gh-91973](https://github.com/python/cpython/issues/91973).)

- [`datetime.date.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.fromisoformat), [`datetime.time.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.fromisoformat) and [`datetime.datetime.fromisoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromisoformat) are now capable of reading nearly every ISO 8601 layout (the lone exceptions being those allowing fractional hours and minutes). (Contributed by Paul Ganssle in [gh-80010](https://github.com/python/cpython/issues/80010).)

[Subject index](INDEX.md) · [Previous source section](dataclasses.md) · [Next source section](enum.md) · [Release/subject declaration](summary-release-highlights.md)
