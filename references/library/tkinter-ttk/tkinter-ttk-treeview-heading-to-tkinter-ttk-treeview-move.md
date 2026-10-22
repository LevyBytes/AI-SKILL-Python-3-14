# tkinter.ttk / ttk.Treeview: `heading()`, `identify()`, `identify_row()`, `identify_column()`, `identify_region()`, `identify_element()`, `index()`, `insert()`, `item()`, `move()`

heading(*column*, *option=None*, ***kw*)

Query or modify the heading options for the specified *column*.

When *kw* is absent, a dict holding the heading option values is returned. When *option* is named, the value belonging to that *option* comes back. Failing those, the options are set to their matching values.

The valid options/values are:

*text*: text

The text shown within the column heading.

*image*: imageName

Names an image to show to the right of the column heading.

*anchor*: anchor

States how the heading text ought to line up. One of the standard Tk anchor values.

*command*: callback

A callback fired whenever the heading label is pressed.

To set up the tree column heading, invoke this with column = "#0".

 identify(*component*, *x*, *y*)

Gives back a description of the named *component* sitting under the point at *x* and *y*, or an empty string when no such *component* occupies that spot.

 identify_row(*y*)

Gives back the item ID for the item found at position *y*.

 identify_column(*x*)

Gives back the data column identifier for the cell found at position *x*.

The tree column has ID #0.

 identify_region(*x*, *y*)

Returns one of:

| region | meaning |
| --- | --- |
| heading | Tree heading area. |
| separator | Space between two columns headings. |
| tree | The tree area. |
| cell | A data cell. |

Availability: Tk 8.6.

 identify_element(*x*, *y*)

Gives back the element sitting at position *x*, *y*.

Availability: Tk 8.6.

 index(*item*)

Gives back the integer index of *item* inside the list of children held by its parent.

 insert(*parent*, *index*, *iid=None*, ***kw*)

Builds a fresh item and returns the item identifier of that newly built item.

For *parent*, pass the item ID belonging to the parent item, or pass the empty string when a fresh top-level item is wanted. For *index*, pass an integer or the value "end" to mark where among the parent's children the new item belongs. When *index* is zero or lower, the new node lands at the start; when *index* meets or exceeds the present child count, it lands at the end. When *iid* is supplied, it serves as the item identifier; *iid* must not already exist in the tree. Failing that, a fresh unique identifier gets generated.

See Item Options for the list of available options.

 item(*item*, *option=None*, ***kw*)

Query or modify the options for the specified *item*.

When no options are supplied, a dict carrying the item's options/values is returned. When *option* is named, the value belonging to that option comes back. Failing those, the options are set to their matching values as supplied through *kw*.

 move(*item*, *parent*, *index*)

Shifts *item* to position *index* within *parent*'s children list.

Moving an item beneath one of its own descendants is not allowed. When *index* is zero or lower, *item* lands at the start; when it meets or exceeds the child count, it lands at the end. A detached *item* is reattached.

[Subject index](INDEX.md) · [Previous](treeview-children-bounds-deletion-and-focus.md) · [Continue](tkinter-ttk-treeview-next-to-tkinter-ttk-treeview-yview.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Treeview; bbox](tkinter-ttk-treeview-class-to-bbox.md) · [Owning module, declaration or section: ttk.Treeview](tkinter-ttk-treeview-class-to-bbox.md)
