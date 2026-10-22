# tkinter.ttk / ttk.Notebook: `forget()`, `hide()`, `identify()`, `index()`, `insert()`, `select()`, `tab()`, `tabs()`, `enable_traversal()`

forget(*tab_id*)

Removes the tab specified by *tab_id*, unmaps and unmanages the associated window.

 hide(*tab_id*)

Hides the tab specified by *tab_id*.

The tab won't appear on screen, yet the window it goes with stays managed by the notebook and its configuration is retained. You can bring hidden tabs back with the `add()` command.

 identify(*x*, *y*)

Gives back the tab element's name at position *x*, *y*, or an empty string when there is none.

 index(*tab_id*)

Gives back the numeric index of the tab named by *tab_id*, or the tab count when *tab_id* is the string "end".

 insert(*pos*, *child*, ***kw*)

Inserts a pane at the specified position.

*pos* may be the string "end", an integer index, or a managed child's name. Should *child* already be under the notebook's management, it gets moved to the given position.

See Tab Options for the list of available options.

 select(*tab_id=None*)

Selects the specified *tab_id*.

The child window it goes with gets shown, and whichever window was selected before (if it differs) is unmapped. When *tab_id* is left out, this returns the widget name of the pane currently selected.

 tab(*tab_id*, *option=None*, ***kw*)

Query or modify the options of the specific *tab_id*.

When *kw* is omitted, it gives back a dictionary of the tab option values. When *option* is supplied, it gives back that *option*'s value. Failing those, it assigns the options their matching values.

 tabs()

Returns a list of windows managed by the notebook.

 enable_traversal()

Enable keyboard traversal for a toplevel window containing this notebook.

Doing so broadens the bindings on the toplevel window that holds the notebook in the following ways:

- Control-Tab: selects the tab following the currently selected one.

- Shift-Control-Tab: selects the tab preceding the currently selected one.

- Alt-K: with *K* standing for the mnemonic (underlined) character of any tab, selects that tab.

You may turn on traversal for more than one notebook within a single toplevel, nested notebooks included. Be aware, though, that notebook traversal behaves correctly only when every pane treats the notebook it sits in as its master.

[Subject index](INDEX.md) · [Previous](tkinter-ttk-notebook-class-to-add.md) · [Continue](progressbar.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Notebook; add](tkinter-ttk-notebook-class-to-add.md) · [Owning module, declaration or section: ttk.Notebook](tkinter-ttk-notebook-class-to-add.md)
