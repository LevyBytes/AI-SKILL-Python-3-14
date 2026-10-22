# tkinter.ttk / ttk.Treeview: `get_children()`, `set_children()`, `column()`, `delete()`, `detach()`, `exists()`, `focus()`

get_children(*item=None*)

Gives back the list of children that belong to *item*.

When *item* is omitted, the root children are returned.

 set_children(*item*, **newchildren*)

Swaps out *item*'s child for *newchildren*.

Any children currently under *item* that do not appear in *newchildren* get detached from the tree. None of the items within *newchildren* may be an ancestor of *item*. Be aware that leaving *newchildren* unspecified will detach *item*'s children.

 column(*column*, *option=None*, ***kw*)

Query or modify the options for the specified *column*.

When *kw* is absent, a dict holding the column option values is returned. When *option* is named, the value belonging to that *option* comes back. Failing those, the options are set to their matching values.

The valid options/values are:

*id*

Gives back the column name. This option is read-only.

*anchor*: One of the standard Tk anchor values.

States how the text within this column ought to line up relative to the cell.

*minwidth*: width

The column's smallest allowed width, given in pixels. Whether the widget is resized or the user drags a column, the treeview widget will never shrink the column below this value.

*stretch*: `True`/`False`

States whether the column's width ought to change when the widget gets resized.

*width*: width

The column's width, expressed in pixels.

To set up the tree column, invoke this with column = "#0"

 delete(**items*)

Delete all specified *items* and all their descendants.

The root item may not be deleted.

 detach(**items*)

Detaches every one of the named *items* from the tree.

The items together with all their descendants remain present and can be put back at some other spot in the tree, though they will not appear on screen.

The root item may not be detached.

 exists(*item*)

Gives back `True` when the named *item* exists in the tree.

 focus(*item=None*)

When *item* is supplied, the focus item is set to *item*. Otherwise, the current focus item is returned, or '' when there is none.

[Subject index](INDEX.md) · [Previous](tkinter-ttk-treeview-class-to-bbox.md) · [Continue](tkinter-ttk-treeview-heading-to-tkinter-ttk-treeview-move.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Treeview; bbox](tkinter-ttk-treeview-class-to-bbox.md) · [Owning module, declaration or section: ttk.Treeview](tkinter-ttk-treeview-class-to-bbox.md)
