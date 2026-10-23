# tkinter.ttk - Tab Options

### Tab Options

Tabs have their own options too:

| Option | Description |
| --- | --- |
| state | Either "normal", "disabled" or "hidden". With "disabled", the tab can't be selected. With "hidden", the tab doesn't appear. |
| sticky | Sets where the child window sits inside the pane area. The value is a string made up of any number (including none) of the letters "n", "s", "e" or "w". Every letter denotes a side (north, south, east or west) the child window clings to, just as in the `grid()` geometry manager. |
| padding | Sets how much extra room goes between the notebook and this pane. Its syntax matches the padding option this widget uses. |
| text | Sets a text to show in the tab. |
| image | Sets an image to show in the tab. See the option image covered in `Widget`. |
| compound | Sets where the image goes relative to the text when both the text and image options are supplied. See Label Options for valid values. |
| underline | Sets the index (0-based) of a character within the text string to underline. That underlined character drives mnemonic activation when `Notebook.enable_traversal()` is invoked. |

[Subject index](INDEX.md) · [Previous](options.md) · [Continue](tab-identifiers.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
