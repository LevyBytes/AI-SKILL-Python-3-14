# curses.panel — Functions

### Functions

These are the functions exposed by the `curses.panel` module:

 curses.panel.bottom_panel()

Gives back the panel sitting at the bottom of the stack.

 curses.panel.new_panel(*win*)

Produces a panel object tied to the supplied window *win*. Keep in mind that you must hold an explicit reference to whatever panel comes back. Should you fail to do so, that panel gets garbage collected and is dropped from the stack.

 curses.panel.top_panel()

Gives back the panel sitting at the top of the stack.

 curses.panel.update_panels()

Refreshes the virtual screen to reflect whatever has shifted in the stack. Note that it stops short of invoking [`curses.doupdate()`](https://docs.python.org/3.14/library/curses.html#curses.doupdate), which is left for you to call.

[Subject index](INDEX.md) · [Previous](curses-panel-a-panel-stack-extension-for-curses.md) · [Continue](panel-above-to-panel-window.md) · [Owning module, declaration or section: curses.panel](curses-panel-a-panel-stack-extension-for-curses.md)
