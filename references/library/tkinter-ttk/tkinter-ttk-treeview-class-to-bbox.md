# tkinter.ttk / ttk.Treeview: `tkinter.ttk.Treeview`, `bbox()`

### ttk.Treeview

 *class *tkinter.ttk.Treeview

 bbox(*item*, *column=None*)

Gives back the bounding box (measured relative to the window of the treeview widget) of the named *item* as (x, y, width, height).

When *column* is provided, the bounding box of that particular cell is returned. Should the *item* not be visible (that is, it descends from a closed item or has been scrolled out of view), an empty string comes back.

[Subject index](INDEX.md) · [Previous](virtual-events.md) · [Continue](treeview-children-bounds-deletion-and-focus.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
