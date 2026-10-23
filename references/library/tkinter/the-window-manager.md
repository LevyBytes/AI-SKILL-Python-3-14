# tkinter - The Window Manager

### The Window Manager

Tk ships a utility command, `wm`, for talking to the window manager. The options you give the `wm` command let you govern things such as titles, placement, icon bitmaps, and so forth. Within `tkinter` these commands turn up as methods on the `Wm` class. Since Toplevel widgets subclass `Wm`, they can invoke the `Wm` methods straight away.

Reaching the toplevel window that holds a given widget is often as simple as referring to that widget’s `master`. Naturally, when the widget has been packed inside a frame, `master` won’t stand for a toplevel window. To reach the toplevel window holding any widget at all, call the `_root()` method. Its leading underscore signals that this function belongs to the implementation rather than serving as an interface onto Tk’s functionality.

Below are a few examples of everyday usage:

```python
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()

```

[Subject index](INDEX.md) · [Previous](coupling-widget-variables.md) · [Continue](tk-option-data-types.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
