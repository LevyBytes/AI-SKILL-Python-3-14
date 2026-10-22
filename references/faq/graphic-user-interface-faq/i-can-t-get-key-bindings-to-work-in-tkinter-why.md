# I can't get key bindings to work in Tkinter: why?

### I can't get key bindings to work in Tkinter: why?

A frequent grievance is that event handlers [bound](https://docs.python.org/3.14/library/tkinter.html#bindings-and-events) to events via the `bind()` method fail to fire even when the right key is struck.

Most often this happens because the widget the binding targets lacks "keyboard focus". Look over the Tk documentation regarding the focus command. A widget normally receives keyboard focus when you click inside it (though not with labels; see the takefocus option).

[Subject index](INDEX.md)
