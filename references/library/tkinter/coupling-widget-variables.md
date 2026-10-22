# tkinter — Coupling Widget Variables

### Coupling Widget Variables

For certain widgets (text entry widgets, for one) the current-value setting can be wired straight to application variables by means of special options. Those options are `variable`, `textvariable`, `onvalue`, `offvalue`, and `value`. The wiring runs in both directions: should the variable change for whatever reason, the widget tied to it refreshes to show the new value.

Regrettably, as `tkinter` stands today, you cannot pass just any Python variable to a widget by way of a `variable` or `textvariable` option. The sole variables this works with are ones subclassed from a class named Variable that `tkinter` defines.

Plenty of handy Variable subclasses come predefined: `StringVar`, `IntVar`, `DoubleVar`, and `BooleanVar`. Read such a variable’s current value by calling its `get()` method, and alter that value by calling its `set()` method. Stick to this protocol and the widget keeps pace with the variable’s value automatically, with nothing further required of you.

For example:

```python
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()

```

[Subject index](INDEX.md) · [Previous](packer-options.md) · [Continue](the-window-manager.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
