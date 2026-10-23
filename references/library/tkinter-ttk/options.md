# tkinter.ttk - Options

### Options

The options particular to this widget are:

| Option | Description |
| --- | --- |
| exportselection | Boolean value. When set, the widget selection is tied to the Window Manager selection (retrievable by calling Misc.selection_get, for instance). |
| justify | Sets how text lines up inside the widget. One of "left", "center", or "right". |
| height | Sets the pop-down listbox's height, counted in rows. |
| postcommand | A script (optionally registered through Misc.register) run right before the values appear. It can dictate which values get shown. |
| state | One of "normal", "readonly", or "disabled". Under the "readonly" state, the value cannot be edited outright, and the user is limited to selection of the values from the dropdown list. Under the "normal" state, the text field can be edited directly. Under the "disabled" state, nothing can be interacted with. |
| textvariable | Names a variable whose value is bound to the widget value. Each time the value behind that name shifts, the widget value follows, and the reverse holds too. See `tkinter.StringVar`. |
| values | Names the list of values shown in the drop-down listbox. |
| width | Gives an integer for the wanted width of the entry window, counted in average-size characters of the widget's font. |

### Options

The options particular to this widget are:

| Option | Description |
| --- | --- |
| from | Float value. When set, this marks the lowest value the decrement button can reach. It has to be written as `from_` when passed as an argument, because `from` is a Python keyword. |
| to | Float value. When set, this marks the highest value the increment button can reach. |
| increment | Float value. Fixes the step by which the increment/decrement buttons shift the value. Defaults to 1.0. |
| values | Sequence of string or float values. When given, the increment/decrement buttons step through this sequence's items instead of adding to or subtracting from numbers. |
| wrap | Boolean value. When `True`, the increment and decrement buttons wrap from the `to` value round to the `from` value, or from the `from` value round to the `to` value, respectively. |
| format | String value. This dictates the format of numbers the increment/decrement buttons produce. It has to take the shape "%W.Pf", where W stands for the value's padded width, P stands for the precision, while '%' along with 'f' are taken literally. |
| command | Python callable. Gets invoked with no arguments each time the increment or decrement button is pressed. |

### Options

The options particular to this widget are:

| Option | Description |
| --- | --- |
| height | When supplied and above zero, sets the wanted height of the pane area (leaving out internal padding or tabs). Failing that, the tallest of all panes governs. |
| padding | Sets how much extra room to put around the notebook's outside. The padding is a list of up to four length specifications left top right bottom. With fewer than four elements supplied, bottom falls back to top, right falls back to left, and top falls back to left. |
| width | When supplied and above zero, sets the wanted width of the pane area (leaving out internal padding). Failing that, the widest of all panes governs. |

### Options

The options particular to this widget are:

| Option | Description |
| --- | --- |
| orient | One of "horizontal" or "vertical". Sets which way the progress bar is oriented. |
| length | Sets the length of the progress bar's long axis (width when horizontal, height when vertical). |
| mode | One of "determinate" or "indeterminate". |
| maximum | A number that sets the maximum value. Defaults to 100. |
| value | The progress bar's present value. Under "determinate" mode, it stands for how much work is done. Under "indeterminate" mode, it is read as modulo *maximum*; in other words, the progress bar finishes one "cycle" each time its value climbs by *maximum*. |
| variable | A name bound to the option value. When given, the progress bar's value is set automatically to this name's value each time that name is altered. |
| phase | Read-only option. The widget steps up this option's value at intervals whenever that value exceeds 0 and, in determinate mode, stays under maximum. The active theme may draw on this option to add further animation effects. |

### Options

The option particular to this widget is:

| Option | Description |
| --- | --- |
| orient | One of "horizontal" or "vertical". Sets which way the separator is oriented. |

### Options

The options particular to this widget are:

| Option | Description |
| --- | --- |
| columns | A list of column identifiers that sets how many columns there are along with their names. |
| displaycolumns | A list of column identifiers (whether symbolic or integer indices) that sets which data columns appear and in what order, or else the string "#all". |
| height | Sets how many rows ought to be visible. Note: the requested width follows from adding up the column widths. |
| padding | Sets the widget's internal padding. The padding is a list of up to four length specifications. |
| selectmode | Governs how the built-in class bindings handle the selection. One of "extended", "browse" or "none". When set to "extended" (the default), several items can be selected. When "browse", just one item is selected at any time. When "none", the selection stays put. Keep in mind that the application code and tag bindings may set the selection any way they like, no matter this option's value. |
| show | A list holding zero or more of the values below that picks which elements of the tree appear. - tree: render tree labels within column #0. - headings: render the heading row. Its default is "tree headings", meaning every element is shown. **Note**: Column #0 stands for the tree column at all times, even when show="tree" goes unstated. |

[Subject index](INDEX.md) · [Previous](combobox.md) · [Continue](virtual-events.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Previous](spinbox.md) · [Previous](notebook.md) · [Continue](tab-options.md) · [Previous](progressbar.md) · [Continue](tkinter-ttk-progressbar-class-to-start.md) · [Previous](separator.md) · [Continue](sizegrip.md) · [Previous](treeview.md) · [Continue](item-options.md)
