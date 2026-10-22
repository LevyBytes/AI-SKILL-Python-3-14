# tkinter.ttk — Standard Options

### Standard Options

Every one of the `ttk` Widgets honors these options:

| Option | Description |
| --- | --- |
| class | Sets the window class. That class drives the lookup of the window's remaining options in the option database, fixes the window's default bindtags, and picks the widget's default layout and style. The option is read-only and can be given only at the moment the window is created. |
| cursor | Sets which mouse cursor the widget uses. When left as the empty string (the default), the cursor is taken from the parent widget. |
| takefocus | Says whether the window takes the focus during keyboard traversal. The returned value is 0, 1 or an empty string. A returned 0 means the window is bypassed completely while traversing with the keyboard. A returned 1 means the window takes the input focus for as long as it stays viewable. An empty string leaves the traversal scripts to decide whether the window gets focus. |
| style | Lets you assign a custom widget style. |

[Subject index](INDEX.md) · [Previous](widget.md) · [Continue](scrollable-widget-options.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
