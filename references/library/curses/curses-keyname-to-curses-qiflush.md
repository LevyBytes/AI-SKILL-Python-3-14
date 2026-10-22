# curses: Key names, mouse options, windows and terminal input modes

curses.keyname(*k*)

Give back the name of the key numbered *k* as a bytes object. For a key producing a printable ASCII character, the name equals the key's character. For a control-key combination, the name is a two-byte bytes object made of a caret (`b'^'`) followed by the matching printable ASCII character. For an alt-key combination (128–255), the name is a bytes object made of the prefix `b'M-'` followed by the name of the matching ASCII character.

 curses.killchar()

Hand back, as a one-byte bytes object, whatever line kill character the user currently has. Under Unix operating systems this is a trait of the curses program's controlling tty, and the curses library itself does not configure it.

 curses.longname()

Give back a bytes object holding the terminfo long name field that describes the present terminal. A verbose description runs to at most 128 characters. It exists only once `initscr()` has been called.

 curses.meta(*flag*)

When *flag* is `True`, permit 8-bit characters as input. When *flag* is `False`, permit only 7-bit chars.

 curses.mouseinterval(*interval*)

Set the longest span, in milliseconds, allowed to pass between a press event and a release event for the two to count as a click, and give back the prior interval value. The default sits at 200 milliseconds, which is one fifth of a second.

 curses.mousemask(*mousemask*)

Choose which mouse events get reported, and give back a tuple `(availmask, oldmask)`. *availmask* tells which of the requested mouse events are reportable; on a total failure it gives back `0`. *oldmask* is the prior value of that window's mouse event mask. While this function goes uncalled, no mouse events are reported at all.

 curses.napms(*ms*)

Sleep for *ms* milliseconds.

 curses.newpad(*nlines*, *ncols*)

Build and give back a pointer to a fresh pad data structure carrying the supplied count of lines and columns. The pad comes back as a window object.

A pad behaves like a window, save that the screen size does not bound it and it need not tie to any particular region of the screen. Pads work well when a large window is called for and only a slice of it will sit on the screen at any moment. Pads do not refresh automatically (for instance from scrolling or echoing of input). A pad's `refresh()` and `noutrefresh()` methods take 6 arguments that pin down which slice of the pad is shown and where on the screen the display goes. Those arguments are *pminrow*, *pmincol*, *sminrow*, *smincol*, *smaxrow*, *smaxcol*; the *p* arguments point at the upper left corner of the pad region being shown, and the *s* arguments mark out a clipping box on the screen inside which that pad region is shown.

 curses.newwin(*nlines*, *ncols*)

 curses.newwin(*nlines*, *ncols*, *begin_y*, *begin_x*)

Give back a fresh window whose upper-left corner sits at `(begin_y, begin_x)` and whose height/width is *nlines*/*ncols*.

By default the window reaches from the named position out to the lower right corner of the screen.

 curses.nl()

Switch into newline mode. This mode turns the return key into a newline on input, and turns a newline into a return plus a line-feed on output. Newline mode starts out on.

 curses.nocbreak()

Exit cbreak mode. Go back to the ordinary “cooked” mode that has line buffering.

 curses.noecho()

Exit echo mode. Echoing of input characters is switched off.

 curses.nonl()

Exit newline mode. Stop translating a return into a newline on input, and stop the low-level translation of a newline into newline/return on output (though this leaves the behavior of `addch('\n')` unchanged, which always performs the equivalent of a return plus a line feed on the virtual screen). With translation switched off, curses can occasionally pick up vertical motion a bit; it also becomes able to spot the return key on input.

 curses.noqiflush()

When the `noqiflush()` routine is in play, the normal flushing of the input and output queues tied to the `INTR`, `QUIT` and `SUSP` characters does not happen. You might wish to invoke `noqiflush()` inside a signal handler when you want output to keep going as though the interrupt never happened, once the handler returns.

 curses.noraw()

Exit raw mode. Go back to the ordinary “cooked” mode that has line buffering.

 curses.pair_content(*pair_number*)

Give back a tuple `(fg, bg)` carrying the colors of the requested color pair. *pair_number* has to fall between `0` and `COLOR_PAIRS - 1`.

 curses.pair_number(*attr*)

Give back the number of the color-pair fixed by the attribute value *attr*. The function `color_pair()` is this one's inverse.

 curses.putp(*str*)

The same as `tputs(str, 1, putchar)`; emit the value of a named terminfo capability for the present terminal. Be aware that whatever `putp()` produces always heads to standard output.

 curses.qiflush([*flag*])

When *flag* is `False`, the outcome matches a call to `noqiflush()`. When *flag* is `True`, or when no argument is given, the queues get flushed upon reading these control characters.

[Subject index](INDEX.md) · [Previous](curses-erasechar-to-curses-isendwin.md) · [Continue](curses-raw-to-curses-tigetnum.md) · [Owning module, declaration or section: curses](curses-terminal-handling-for-character-cell-displays.md) · [Owning module, declaration or section: Functions](curses-error-to-curses-endwin.md)
