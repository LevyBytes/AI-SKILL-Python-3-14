# curses c api C API: `PyCursesInitialised`, `PyCursesInitialisedColor`

PyCursesInitialised

Macro checking if [`curses.initscr()`](https://docs.python.org/3.14/library/curses.html#curses.initscr) has been called.

The macro expansion is roughly equivalent to:

```c
{
    typedef int (*predicate_t)(void);
    predicate_t was_initscr_called = (predicate_t)PyCurses_API[2];
    if (!was_initscr_called()) {
        return NULL;
    }
}

```

 PyCursesInitialisedColor

Macro checking if [`curses.start_color()`](https://docs.python.org/3.14/library/curses.html#curses.start_color) has been called.

The macro expansion is roughly equivalent to:

```c
{
    typedef int (*predicate_t)(void);
    predicate_t was_start_color_called = (predicate_t)PyCurses_API[3];
    if (!was_start_color_called()) {
        return NULL;
    }
}

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](import-curses-to-pycursessetuptermcalled.md) · [Following source contract](pycurses-capsule-name.md)
