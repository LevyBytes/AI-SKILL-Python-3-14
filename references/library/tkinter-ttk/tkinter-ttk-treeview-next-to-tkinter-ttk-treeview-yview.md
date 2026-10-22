# tkinter.ttk / ttk.Treeview: `next()`, `parent()`, `prev()`, `reattach()`, `see()`, `selection()`, `selection_set()`, `selection_add()`, `selection_remove()`, `selection_toggle()`, `set()`, `tag_bind()`, `tag_configure()`, `tag_has()`, `xview()`, `yview()`

next(*item*)

Gives back the identifier of *item*'s next sibling, or '' when *item* is its parent's last child.

 parent(*item*)

Gives back the ID of *item*'s parent, or '' when *item* sits at the top level of the hierarchy.

 prev(*item*)

Gives back the identifier of *item*'s previous sibling, or '' when *item* is its parent's first child.

 reattach(*item*, *parent*, *index*)

An alias for `Treeview.move()`.

 see(*item*)

Ensure that *item* is visible.

Switches every one of *item*'s ancestors open option to `True`, and scrolls the widget when needed so that *item* falls within the tree's visible portion.

 selection()

Returns a tuple of selected items.

Changed in version 3.8: arguments are no longer accepted by `selection()`. To alter the selection state, reach for the selection methods listed below.

 selection_set(**items*)

*items* becomes the new selection.

Changed in version 3.6: rather than a lone tuple, *items* now accepts being supplied as individual arguments.

 selection_add(**items*)

Add *items* to the selection.

Changed in version 3.6: you may now hand over *items* as distinct arguments instead of one single tuple.

 selection_remove(**items*)

Remove *items* from the selection.

Changed in version 3.6: *items* may be given through several separate arguments and not only via a lone tuple.

 selection_toggle(**items*)

Toggle the selection state of each item in *items*.

Changed in version 3.6: supplying *items* as a number of individual arguments is now allowed, not merely one tuple.

 set(*item*, *column=None*, *value=None*)

Given a single argument, returns a dictionary of column/value pairs for the named *item*. Given two arguments, returns the present value of the named *column*. Given three arguments, sets the value of the named *column* within the named *item* to the named *value*.

 tag_bind(*tagname*, *sequence=None*, *callback=None*)

Bind a callback for the given event *sequence* to the tag *tagname*. Whenever an event reaches an item, the callbacks tied to each of that item's tags option fire.

 tag_configure(*tagname*, *option=None*, ***kw*)

Query or modify the options for the specified *tagname*.

When *kw* is absent, a dict of the option settings for *tagname* is returned. When *option* is named, the value for that *option* against the named *tagname* comes back. Failing those, the options are set to their matching values for the given *tagname*.

 tag_has(*tagname*, *item=None*)

When *item* is supplied, returns 1 or 0 according to whether the named *item* carries the given *tagname*. Failing that, returns a list of every item carrying the named tag.

Availability: Tk 8.6

 xview(**args*)

Query or modify horizontal position of the treeview.

 yview(**args*)

Query or modify vertical position of the treeview.

[Subject index](INDEX.md) · [Previous](tkinter-ttk-treeview-heading-to-tkinter-ttk-treeview-move.md) · [Continue](tkinter-ttk-style-class.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Treeview; bbox](tkinter-ttk-treeview-class-to-bbox.md) · [Owning module, declaration or section: ttk.Treeview](tkinter-ttk-treeview-class-to-bbox.md)
