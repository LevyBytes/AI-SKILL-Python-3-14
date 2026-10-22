# tkinter.ttk — Scrollable Widget Options

### Scrollable Widget Options

Widgets steered by a scrollbar back the options below.

| Option | Description |
| --- | --- |
| xscrollcommand | Serves as the channel to horizontal scrollbars. As the view inside the widget's window shifts, the widget emits a Tcl command built from the scrollcommand. Typically this option holds the `Scrollbar.set()` method belonging to some scrollbar, which refreshes that scrollbar each time the window's view shifts. |
| yscrollcommand | Serves as the channel to vertical scrollbars. The preceding entry has further detail. |

[Subject index](INDEX.md) · [Previous](standard-options.md) · [Continue](label-options.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
