# Python 3.5.3 release candidate 1 / library / curses

[bpo-28549](https://bugs.python.org/issue?@action=redirect&bpo=28549): Repair a segfault in the addch() routine of curses when used with ncurses6.

[bpo-26750](https://bugs.python.org/issue?@action=redirect&bpo=26750): unittest.mock.create_autospec() now behaves correctly with subclasses of property() and with other data descriptors.

- Within the curses module, an error is now raised whenever window.getstr() or window.instr() receives a negative value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
