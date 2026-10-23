# tkinter.ttk - Virtual events

### Virtual events

When the user picks an item out of the value list, the combobox widgets fire a **<&lt;ComboboxSelected&gt;>** virtual event.

### Virtual events

Pressing &lt;Up&gt; makes the spinbox widget fire an **<&lt;Increment&gt;>** virtual event, while pressing &lt;Down&gt; makes it fire a **<&lt;Decrement&gt;>** virtual event.

### Virtual Events

Once a different tab is chosen, this widget fires a **<&lt;NotebookTabChanged&gt;>** virtual event.

### Virtual Events

The following virtual events are emitted by the Treeview widget.

| Event | Description |
| --- | --- |
| <&lt;TreeviewSelect&gt;> | Generated whenever the selection changes. |
| <&lt;TreeviewOpen&gt;> | Generated just before settings the focus item to open=True. |
| <&lt;TreeviewClose&gt;> | Generated just after setting the focus item to open=False. |

To find out which item or items were affected, use the `Treeview.focus()` and `Treeview.selection()` methods.

[Subject index](INDEX.md) · [Previous](options.md) · [Continue](tkinter-ttk-combobox-class-to-current.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Continue](tkinter-ttk-spinbox-class-to-get.md) · [Previous](tab-identifiers.md) · [Continue](tkinter-ttk-notebook-class-to-add.md) · [Previous](column-identifiers.md) · [Continue](tkinter-ttk-treeview-class-to-bbox.md)
