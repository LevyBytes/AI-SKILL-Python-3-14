# Curses further information and API coverage

### For More Information
A handful of more advanced matters fall outside this HOWTO — pulling back what is already drawn on the screen, say, or trapping mouse activity coming from an xterm instance — yet the Python library entry covering the [`curses`](https://docs.python.org/3.14/library/curses.html#module-curses) module has by now grown fairly thorough. Make that your next stop.

Whenever the precise workings of a curses function leave you uncertain, turn to the manual pages shipped with whatever curses build you run — be that ncurses or some closed-source offering from a Unix vendor. Those pages spell out the oddities and lay out exhaustive rosters of every function, attribute, and [ACS_*](https://docs.python.org/3.14/library/curses.html#curses-acs-codes) character at your disposal.

Given how sprawling the curses API happens to be, a few of its functions never made it into the Python interface. Usually that gap has nothing to do with implementation difficulty — it simply reflects that nobody has called for them so far. On top of that, the menu library that ships alongside ncurses still lacks Python coverage. Contributions filling in any of these would be gladly received; consult [the Python Developer’s Guide](https://devguide.python.org/) for details on how to submit patches to Python.

- [Writing Programs with NCURSES](https://invisible-island.net/ncurses/ncurses-intro.html): an extensive walkthrough aimed at people coding in C.

- [The ncurses man page](https://linux.die.net/man/3/ncurses)

- [The ncurses FAQ](https://invisible-island.net/ncurses/ncurses.faq.html)

- [“Use curses… don’t swear”](https://www.youtube.com/watch?v=eN1eZtjLEnU): a recorded PyCon 2013 session about steering terminals by way of curses or Urwid.

- [“Console Applications with Urwid”](https://pyvideo.org/video/1568/console-applications-with-urwid): a recorded PyCon CA 2012 session showcasing a handful of programs built on Urwid.

[Subject index](INDEX.md) · [Previous source context](user-input.md)
