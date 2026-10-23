# curses.panel - Panel Objects

### Panel Objects

A panel object — the kind handed back by `new_panel()` above — is essentially a window that also has a place in the layering order. Every panel is paired with a window that supplies its contents, and the panel's own methods govern where that window falls in the stack's depth.

The methods available on panel objects are:

 Panel.above()

Hands back whichever panel lies directly above this one.

 Panel.below()

Hands back whichever panel lies directly beneath this one.

 Panel.bottom()

Sends the panel down to the very bottom of the ordering.

 Panel.hidden()

Yields `True` when the panel is concealed (not on screen), and `False` in every other case.

 Panel.hide()

Conceal the panel. The object itself is not destroyed; this merely takes its window off the visible screen.

 Panel.move(*y*, *x*)

Reposition the panel so it sits at the screen coordinates `(y, x)`.

 Panel.replace(*win*)

Swap out the panel's current window, replacing it with the window *win*.

 Panel.set_userptr(*obj*)

Assign *obj* as the panel's user pointer. This lets you attach any data you like to the panel, and *obj* may be any Python object whatsoever.

 Panel.show()

Bring the panel back into view (it may previously have been concealed).

 Panel.top()

Raise the panel up to the very top of the ordering.

 Panel.userptr()

Hands back the panel's user pointer, which can be any Python object at all.

 Panel.window()

Hands back the window object that the panel is paired with.

[Subject index](INDEX.md) · [Previous](curses-panel-bottom-panel-to-curses-panel-update-panels.md) · [Continue](../custominterp/custom-python-interpreters.md) · [Owning module, declaration or section: curses.panel](curses-panel-a-panel-stack-extension-for-curses.md)
