# curses.textpad: `curses.textpad.Textbox`

### Textbox objects

Creating a `Textbox` object goes like this:

 *class *curses.textpad.Textbox(*win*)

Hand back a textbox widget object. For *win* you supply a curses window object that will hold the textbox. At the start, the textbox’s edit cursor sits at the containing window’s upper left hand corner, at coordinates `(0, 0)`. The instance begins life with its `stripspaces` flag switched on.

The methods carried by `Textbox` objects are these:

[Subject index](INDEX.md) · [Previous](curses-textpad-rectangle.md) · [Continue](curses-textpad-textbox-edit-to-curses-textpad-textbox-gather.md) · [Owning module, declaration or section: curses.textpad](curses-textpad-rectangle.md)
