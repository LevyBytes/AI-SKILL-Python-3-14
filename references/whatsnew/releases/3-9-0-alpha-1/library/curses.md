# Python 3.9.0 alpha 1 / library / curses

[bpo-37738](https://bugs.python.org/issue?@action=redirect&bpo=37738): Corrected how curses `addch(str, color_pair)` is implemented: the color pair is now forwarded to `setcchar()`, in place of the prior behavior of always handing it 0 as the color pair.

[bpo-37695](https://bugs.python.org/issue?@action=redirect&bpo=37695): Fixed the [`curses.unget_wch()`](https://docs.python.org/3.14/library/curses.html#curses.unget_wch) error message. Anthony Sottile authored the patch.

[bpo-38312](https://bugs.python.org/issue?@action=redirect&bpo=38312): Anthony Sottile contributed the [`curses.get_escdelay()`](https://docs.python.org/3.14/library/curses.html#curses.get_escdelay), [`curses.set_escdelay()`](https://docs.python.org/3.14/library/curses.html#curses.set_escdelay), [`curses.get_tabsize()`](https://docs.python.org/3.14/library/curses.html#curses.get_tabsize), and [`curses.set_tabsize()`](https://docs.python.org/3.14/library/curses.html#curses.set_tabsize) functions.

[bpo-36589](https://bugs.python.org/issue?@action=redirect&bpo=36589): On success the [`curses.update_lines_cols()`](https://docs.python.org/3.14/library/curses.html#curses.update_lines_cols) function henceforth returns `None` in place of `1`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
