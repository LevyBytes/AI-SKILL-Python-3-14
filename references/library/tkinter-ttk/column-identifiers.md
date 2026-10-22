# tkinter.ttk — Column Identifiers

### Column Identifiers

Column identifiers may be written in any of these forms:

- A symbolic name drawn from the columns option list.

-

An integer n, identifying the nth data column.

- A string shaped like #n, with n being an integer, identifying the nth display column.

Notes:

- The order in which an item's option values appear may differ from the order in which they were stored.

- Column #0 always points at the tree column, regardless of whether show="tree" was passed.

A data column number serves as an index into the option values list of an item; a display column number is the column position within the tree where those values appear. Labels for the tree are shown in column #0. When the displaycolumns option is left unset, data column n appears in column #n+1. Once more, **column #0 always refers to the tree column**.

[Subject index](INDEX.md) · [Previous](tag-options.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Continue](virtual-events.md)
