# tkinter - Important Tk Concepts

### Important Tk Concepts

Simple as it is, this program already shows off the following key Tk concepts:

widgets

A Tkinter user interface is assembled from individual *widgets*. Every widget appears as a Python object, created from classes such as `ttk.Frame`, `ttk.Label`, and `ttk.Button`.

widget hierarchy

Widgets sit within a *hierarchy*. Both the label and the button lived inside a frame, which itself lived inside the root window. As each *child* widget is built, its *parent* widget gets passed in as the first argument to the widget constructor.

configuration options

Widgets carry *configuration options* that adjust how they look and behave — for example, the text shown in a label or a button. Distinct widget classes come with distinct sets of options.

geometry management

Creating a widget doesn’t place it into the user interface on its own. A *geometry manager* such as `grid` dictates where in the user interface it ends up.

event loop

Tkinter only responds to user input, to changes from your program, and even to display refreshes while an *event loop* is actively running. Without your program running the event loop, your user interface won’t refresh.

[Subject index](INDEX.md) · [Previous](a-hello-world-program.md) · [Continue](understanding-how-tkinter-wraps-tcl-tk.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
