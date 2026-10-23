# curses.textpad`curses.textpad` - Text input widget for curses programs

### `curses.textpad` - Text input widget for curses programs

Within the `curses.textpad` module sits a `Textbox` class for basic text editing inside a curses window, wired up with keybindings that echo those of Emacs (and therefore Netscape Navigator, BBedit 6.x, FrameMaker, and a host of other programs too). The module throws in a rectangle-drawing function as well, handy for boxing in text areas or whatever else you need.

Here is the function that the `curses.textpad` module defines:

 curses.textpad.rectangle(*win*, *uly*, *ulx*, *lry*, *lrx*)

Render a rectangle. A window object has to be the first argument, while everything after it gives coordinates measured against that window. Arguments two and three carry the y and x coordinates marking the rectangle’s upper left hand corner; arguments four and five carry the y and x coordinates of its lower right hand corner. On terminals capable of it — xterm and the bulk of other software terminal emulators among them — the rectangle comes out in VT100/IBM PC forms characters. Failing that, it falls back to ASCII dashes, vertical bars, and plus signs.

[Subject index](INDEX.md) · [Previous](../curses/terminal-color-constants-table.md) · [Continue](curses-textpad-textbox-class.md)
