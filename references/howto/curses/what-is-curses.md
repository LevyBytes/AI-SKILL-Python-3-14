# What is curses?

### What is curses?

For text-based terminals, the curses library offers a terminal-independent way to paint the screen and handle keyboard input; among such terminals are VT100s, the Linux console, and the emulated terminal that assorted programs supply. To carry out routine actions—relocating the cursor, scrolling the display, clearing regions—display terminals recognize a range of control codes. The codes employed vary substantially from one terminal to the next, and individual terminals frequently carry their own small idiosyncrasies.

Given how prevalent graphical displays now are, you might wonder “why bother”? Character-cell display terminals are admittedly a dated technology, yet certain niches remain where doing clever things with them still pays off. Small-footprint or embedded Unixes lacking an X server form one such niche. Utilities like OS installers and kernel configurators, which sometimes must operate before any graphical support exists, form another.

What curses delivers is reasonably basic: it hands the programmer an abstract display made up of several text windows that do not overlap. You can alter a window’s contents in several ways—inserting text, clearing it, adjusting how it looks—and curses will work out which control codes must reach the terminal to render the correct result. Concepts from user interfaces—buttons, checkboxes, dialogs—are largely absent from curses; should you require them, look at a user interface library like [Urwid](https://pypi.org/project/Urwid/).

Originally curses was authored for BSD Unix; AT&T’s subsequent System V releases of Unix contributed numerous new functions and improvements. No longer maintained, BSD curses has given way to ncurses, an open-source realization of the AT&T interface. On an open-source Unix like Linux or FreeBSD, your system is virtually guaranteed to rely on ncurses. Because the bulk of today’s commercial Unix releases derive from System V code, every function documented here is most likely present. That said, some proprietary Unixes ship older curses versions that might not cover everything.

The [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module is absent from the Windows build of Python. There is a port named [UniCurses](https://pypi.org/project/UniCurses/) you can use.

[Subject index](INDEX.md) · [Previous source context](curses-programming-with-python.md) · [Following source context](the-python-curses-module.md)
