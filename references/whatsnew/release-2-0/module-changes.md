# What’s New in Python 2.0 / Module changes — calendar, configparser, curses, http, posix, random, re, readline, shelve, socket, urllib, wave

### Module changes

Python’s sizable standard library received a great many enhancements and fixes; the modules touched include [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline), [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#module-configparser), `cgi`, [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar), [`posix`](https://docs.python.org/3.14/library/posix.html#module-posix), `readline`, `xmllib`, `aifc`, `chunk`, [`wave`](https://docs.python.org/3.14/library/wave.html#module-wave), [`random`](https://docs.python.org/3.14/library/random.html#module-random), [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve), and `nntplib`, among others. Turn to the CVS logs if you want the precise change-by-change account.

OpenSSL support for the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module came from Brian Gallew. OpenSSL realizes the Secure Socket Layer, scrambling whatever data travels across a socket. While building Python, you may adjust `Modules/Setup` to fold in SSL support, which equips the `socket` module with one more function: `socket.ssl(socket, keyfile, certfile)`. That function accepts a socket object and gives back an SSL socket. The [`httplib`](https://docs.python.org/3.14/library/http.html#module-http) and [`urllib`](https://docs.python.org/3.14/library/urllib.html#module-urllib) modules picked up handling for `https://` URLs as well, although nobody has yet built FTP or SMTP atop SSL.

Greg Stein reworked the [`httplib`](https://docs.python.org/3.14/library/http.html#module-http) module from the ground up so that it handles HTTP/1.1.

It still stays compatible with the 1.5 release of `httplib`, but tapping HTTP/1.1 capabilities like pipelining means reworking your code against a separate set of interfaces.

These days the `Tkinter` module works with Tcl/Tk version 8.1, 8.2, or 8.3, while the earlier 7.x releases are no longer handled. The Tkinter module can now render Unicode strings inside Tk widgets too. On top of that, Fredrik Lundh donated a tuning change that speeds up calls such as `create_line` and `create_polygon` considerably, most noticeably when many coordinates are involved.

Building on Oliver Andrich’s improved edition, the [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module has grown substantially and now surfaces a host of extra functions drawn from ncurses and SYSV curses — colour, support for alternate character sets, pads, and mouse handling among them. The upshot is that the module will no longer run on operating systems carrying only BSD curses, though no still-maintained OS appears to land in that bucket.

As the earlier section on 2.0’s Unicode support noted, the machinery behind the regular expressions exposed by the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module has been swapped out. The replacement, SRE, is a fresh regular expression engine that Fredrik Lundh wrote with partial backing from Hewlett Packard, and it can match against 8-bit strings as well as Unicode strings.

[Subject index](INDEX.md) · [Previous source section](relationship-to-pyxml.md) · [Next source section](new-modules.md) · [Release/subject declaration](introduction.md)
