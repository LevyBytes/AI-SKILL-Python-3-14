# Python 3.9.0 alpha 1 / build / ossaudiodev

[bpo-36210](https://bugs.python.org/issue?@action=redirect&bpo=36210): Revise how optional extension modules are detected on AIX. Since ossaudiodev and spwd have no role on AIX, they are no longer flagged as absent. Because third-party ncurses packaging (carrying ASIS support) collides with the officially backed AIX curses library, AIX is configured toward libcurses.a. Building _curses_panel is, however, skipped.

patch by M Felt

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
