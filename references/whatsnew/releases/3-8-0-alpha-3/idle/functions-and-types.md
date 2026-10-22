# Python 3.8.0 alpha 3 / idle / functions and types

[bpo-36396](https://bugs.python.org/issue?@action=redirect&bpo=36396): Drop the fgBg param from idlelib.config.GetHighlight(). The param saw use only twice and altered the return type.

[bpo-36152](https://bugs.python.org/issue?@action=redirect&bpo=36152): Drop colorizer.ColorDelegator.close_when_done together with the matching argument on .close(). Inside IDLE, each of these has stayed None or False ever since 2007.

[bpo-36096](https://bugs.python.org/issue?@action=redirect&bpo=36096): Convert class variables over to instance variables inside colorizer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
