# Windows and Pads

### Windows and Pads

In curses the fundamental abstraction is windows. A window object stands for a rectangular region of the screen and offers methods to show text, clear it, let the user enter strings, and so on.

That `stdscr` object handed back by the [`initscr()`](https://docs.python.org/3.14/library/curses.html#curses.initscr) function is a window object spanning the full screen. While plenty of programs will need nothing beyond this lone window, you might prefer to split the screen into smaller windows so you can redraw or clear each one on its own. Building a fresh window of a specified size is the job of the [`newwin()`](https://docs.python.org/3.14/library/curses.html#curses.newwin) function, which returns the new window object.

```python
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

```

Be aware that curses adopts an unusual coordinate system. The order in which coordinates are always passed is *y,x*, and a window’s top-left corner is coordinate (0,0). That goes against the usual coordinate-handling convention in which the *x* coordinate is given first. It’s a regrettable departure from most other computer applications, yet it has been part of curses ever since it was first written, and changing it now is simply too late.

Calling on the [`curses.LINES`](https://docs.python.org/3.14/library/curses.html#curses.LINES) and [`curses.COLS`](https://docs.python.org/3.14/library/curses.html#curses.COLS) variables lets your application find out the screen’s size by reading the *y* and *x* sizes. Valid coordinates accordingly run from `(0,0)` through `(curses.LINES - 1, curses.COLS - 1)`.

Whenever you invoke a method to show or erase text, the result doesn’t appear on the display right away. You must instead invoke the [`refresh()`](https://docs.python.org/3.14/library/curses.html#curses.window.refresh) method on window objects to refresh the screen.

The reason is that curses was first written for slow 300-baud terminal links; on those terminals, cutting down the time it took to redraw the screen mattered a great deal. So curses gathers up the screen’s changes and renders them as efficiently as it can once you call `refresh()`. As an illustration, if your program shows some text in a window and then wipes the window, there’s no point sending the original text since it’s never seen.

Realistically, having to tell curses outright to redraw a window doesn’t add all that much complication to programming with curses. The typical program bursts into a round of activity and then halts, waiting on a keystroke or some other user action. The only thing you must do is make sure the screen has been redrawn before you halt to await user input, which you do by first calling `stdscr.refresh()` or the `refresh()` method on whichever other window is relevant.

A pad is a special kind of window; it may exceed the size of the real display screen, with only a slice of the pad shown at any one time. To create a pad you supply the pad’s height and width, whereas to refresh a pad you give the coordinates of the on-screen region where a slice of the pad is to appear.

```python
pad = curses.newpad(100, 100)
# These loops fill the pad with letters; addch() is
# explained in the next section
for y in range(0, 99):
    for x in range(0, 99):
        pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

# Displays a section of the pad in the middle of the screen.
# (0,0) : coordinate of upper-left corner of pad area to display.
# (5,5) : coordinate of upper-left corner of window area to be filled
#         with pad content.
# (20, 75) : coordinate of lower-right corner of window area to be
#          : filled with pad content.
pad.refresh( 0,0, 5,5, 20,75)

```

What the `refresh()` call does is render a slice of the pad inside the rectangle that stretches between coordinate (5,5) and coordinate (20,75) on the display; the shown slice has its upper left corner at coordinate (0,0) on the pad. Apart from that one distinction, pads behave just like ordinary windows and offer the same methods.

When several windows and pads sit on screen, there’s a more efficient route for refreshing the display that avoids the irritating flicker that occurs as each region is updated one at a time. In fact `refresh()` performs two operations:

1.

Invokes the [`noutrefresh()`](https://docs.python.org/3.14/library/curses.html#curses.window.noutrefresh) method on every window to refresh an underlying data structure that records the screen’s desired state.

2.

Invokes the function [`doupdate()`](https://docs.python.org/3.14/library/curses.html#curses.doupdate) function to bring the physical screen in line with the desired state held in that data structure.

What you can do instead is invoke `noutrefresh()` across several windows to refresh the data structure, and then invoke `doupdate()` a single time to refresh the screen.

[Subject index](INDEX.md) · [Previous source context](starting-and-ending-a-curses-application.md) · [Following source context](displaying-text.md)
