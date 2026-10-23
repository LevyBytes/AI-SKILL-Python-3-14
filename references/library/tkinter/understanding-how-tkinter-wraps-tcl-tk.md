# tkinter - Understanding How Tkinter Wraps Tcl/Tk

### Understanding How Tkinter Wraps Tcl/Tk

Whenever your application calls upon Tkinter’s classes and methods, behind the scenes Tkinter is stitching together strings that stand for Tcl/Tk commands, then running those commands through the Tcl interpreter bound to your application’s `Tk` instance.

Whether you’re working through reference documentation, hunting for the right method or option, reworking some pre-existing code, or debugging your Tkinter application, there will be moments when grasping what those underlying Tcl/Tk commands look like proves useful.

By way of illustration, below is the Tcl/Tk counterpart to the central portion of the Tkinter script shown above.

```python
ttk::frame .frm -padding 10
grid .frm
grid [ttk::label .frm.lbl -text "Hello World!"] -column 0 -row 0
grid [ttk::button .frm.btn -text "Quit" -command "destroy ."] -column 1 -row 0

```

Tcl’s syntax resembles that of many shell languages, where the opening word names the command to run and its arguments trail behind it, separated by spaces. Without diving too deep, take note of the following:

- The commands that create widgets (such as `ttk::frame`) line up with widget classes in Tkinter.

- Tcl widget options (such as `-text`) line up with keyword arguments in Tkinter.

- In Tcl, widgets are addressed by a *pathname* (such as `.frm.btn`), whereas Tkinter forgoes names in favor of object references.

- A widget’s spot within the widget hierarchy is captured in its (hierarchical) pathname, which adopts a `.` (dot) as the path separator. The pathname for the root window is simply `.` (dot). Over in Tkinter, the hierarchy is established not through a pathname but by naming the parent widget as each child widget is built.

- Operations realized as standalone *commands* in Tcl (such as `grid` or `destroy`) show up as *methods* on Tkinter widget objects. As you’ll soon see, on other occasions Tcl employs what look like method calls on widget objects, which sit closer to the style Tkinter uses.

[Subject index](INDEX.md) · [Previous](important-tk-concepts.md) · [Continue](how-do-i-what-option-does.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
