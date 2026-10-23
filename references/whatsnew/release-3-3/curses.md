# What's New In Python 3.3 / curses - curses

### curses

- Where the [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module links against the ncursesw library, fall back on the Unicode functions for any Unicode strings or characters handed in (such as `waddwstr()`), and otherwise on the bytes functions (for example `waddstr()`).

- Encode Unicode strings with the locale encoding rather than `utf-8`.

- A fresh [`curses.window.encoding`](https://docs.python.org/3.14/library/curses.html#curses.window.encoding) attribute now belongs to [`curses.window`](https://docs.python.org/3.14/library/curses.html#curses.window).

- To fetch a wide character, the [`curses.window`](https://docs.python.org/3.14/library/curses.html#curses.window) class now offers a new [`get_wch()`](https://docs.python.org/3.14/library/curses.html#curses.window.get_wch) method

- For pushing a wide character back so that the following [`get_wch()`](https://docs.python.org/3.14/library/curses.html#curses.window.get_wch) hands it over, the [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module gains a new [`unget_wch()`](https://docs.python.org/3.14/library/curses.html#curses.unget_wch) function

(This was contributed by Iñigo Serna under [bpo-6755](https://bugs.python.org/issue?@action=redirect&bpo=6755).)

[Subject index](INDEX.md) · [Previous source section](crypt.md) · [Next source section](datetime.md) · [Release/subject declaration](summary-release-highlights.md)
