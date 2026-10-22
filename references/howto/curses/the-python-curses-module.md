# The Python curses module

### The Python curses module

This Python module wraps the C functions that curses exposes in a fairly thin layer; anyone who already knows curses programming in C will find moving that knowledge to Python genuinely easy. The chief contrast is that the Python interface streamlines matters by collapsing several C functions—`addstr()`, `mvaddstr()`, and `mvwaddstr()`—down to one [`addstr()`](https://docs.python.org/3.14/library/curses.html#curses.window.addstr) method. We’ll cover this with more depth further on.

Consider this HOWTO an introduction to building text-mode programs using curses and Python. A full reference to the curses API isn’t the aim here; for that, turn to the ncurses section in the Python library guide together with the C manual pages for ncurses. Still, the core ideas are what you’ll come away with.

[Subject index](INDEX.md) · [Previous source context](what-is-curses.md) · [Following source context](starting-and-ending-a-curses-application.md)
