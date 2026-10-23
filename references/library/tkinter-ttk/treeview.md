# tkinter.ttk - Treeview

### Treeview

The `ttk.Treeview` widget renders a hierarchical set of items. Every item carries a text label, an optional image, and an optional list of data values. Those data values appear in consecutive columns following the tree label.

You steer the order in which data values appear by setting the `displaycolumns` widget option. The tree widget is also able to render column headings. You reach columns either by number or by the symbolic names given in the columns widget option. See Column Identifiers.

A unique name identifies each item. When the caller doesn't supply item IDs, the widget creates them. One special root item exists, named `{}`. The root item itself stays hidden; its children show up at the top level of the hierarchy.

Each item also keeps a list of tags, which you can use to tie event bindings to individual items and to govern how an item looks.

The Treeview widget can scroll both horizontally and vertically, per the options laid out in Scrollable Widget Options together with the `Treeview.xview()` and `Treeview.yview()` methods.

[Subject index](INDEX.md) · [Previous](bugs.md) · [Continue](options.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
