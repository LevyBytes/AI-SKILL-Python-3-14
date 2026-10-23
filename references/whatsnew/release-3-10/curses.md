# What's New In Python 3.10 / curses - curses

### curses

Whenever ncurses 6.1 introduced its extended color functions, they will now be picked up automatically by [`curses.color_content()`](https://docs.python.org/3.14/library/curses.html#curses.color_content), [`curses.init_color()`](https://docs.python.org/3.14/library/curses.html#curses.init_color), [`curses.init_pair()`](https://docs.python.org/3.14/library/curses.html#curses.init_pair), and [`curses.pair_content()`](https://docs.python.org/3.14/library/curses.html#curses.pair_content). A fresh function, [`curses.has_extended_color_support()`](https://docs.python.org/3.14/library/curses.html#curses.has_extended_color_support), tells you whether the ncurses library underneath offers extended color support. (Contributed by Jeffrey Kintscher and Hans Petter Jansson in [bpo-36982](https://bugs.python.org/issue?@action=redirect&bpo=36982).)

Should the underlying curses library supply them, the `BUTTON5_*` constants are now surfaced through the [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module. (Contributed by Zackery Spytz in [bpo-39273](https://bugs.python.org/issue?@action=redirect&bpo=39273).)

[Subject index](INDEX.md) · [Previous source section](contextlib.md) · [Next source section](dataclasses-slots.md) · [Release/subject declaration](summary-release-highlights.md)
