# tkinter.ttk — Widget States

### Widget States

A bitmap of independent state flags is what the widget state amounts to.

| Flag | Description |
| --- | --- |
| active | The mouse cursor sits over the widget, and clicking a mouse button will trigger some action |
| disabled | The widget has been disabled by the program |
| focus | The widget holds keyboard focus |
| pressed | The widget is currently being pressed |
| selected | "On", "true", or "current" for the likes of Checkbuttons and radiobuttons |
| background | Both Windows and Mac recognize an "active" or foreground window. The *background* state is applied to widgets within a background window and removed from those within the foreground window |
| readonly | The widget ought to block user modification |
| alternate | An alternate display format particular to the widget |
| invalid | The widget holds an invalid value |

A state specification consists of a sequence of state names, each one optionally carrying a leading exclamation point to mark that the bit is off.

[Subject index](INDEX.md) · [Previous](compatibility-options.md) · [Continue](tkinter-ttk-widget-class-to-identify.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
