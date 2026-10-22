# tkinter — A Hello World Program

### A Hello World Program

Let’s begin by stepping through a “Hello World” application written in Tkinter. It’s not the most minimal example we could produce, yet it carries enough to demonstrate several key concepts worth knowing.

```python
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

```

Following the imports, the next line builds an instance of the `Tk` class, which starts up Tk and creates the Tcl interpreter tied to it. It additionally produces a toplevel window — referred to as the root window — that acts as the application’s main window.

The line after that builds a frame widget, which here is going to hold a label and a button we’ll make next. The frame nests inside the root window.

The following line builds a label widget carrying a fixed text string. The `grid()` method serves to set out the relative layout (position) of the label inside the frame widget that holds it, much the way HTML tables behave.

Next a button widget is built and positioned to the right of the label. Pressing it triggers the `destroy()` method on the root window.

Lastly, the `mainloop()` method renders everything onscreen and keeps responding to user input right up until the program ends.

[Subject index](INDEX.md) · [Previous](tkinter-life-preserver.md) · [Continue](important-tk-concepts.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
