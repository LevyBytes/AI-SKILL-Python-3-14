# Python 3.11.0 alpha 1 / build / compiler and parser

[bpo-45067](https://bugs.python.org/issue?@action=redirect&bpo=45067): The ncurses function extended_color_content arrived back in 2017

([https://invisible-island.net/ncurses/NEWS.html#index-t20170401](https://invisible-island.net/ncurses/NEWS.html#index-t20170401)). The

ncurses-devel package shipped in CentOS 7 carried an older ncurses, which produced a compilation error. To compile ncurses with extended color support, the ncurses library version is checked to be >= 20170401.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
