# tkinter.ttk / ttk.Widget: `instate()`, `state()`

instate(*statespec*, *callback=None*, **args*, ***kw*)

Check the widget's state. When no callback is given, it returns `True` should the widget state line up with *statespec* and `False` if not. When a callback is given, that callback runs with args provided the widget state lines up with *statespec*.

 state(*statespec=None*)

Change or query the widget state. When *statespec* is provided, it sets the widget state from that and returns a fresh *statespec* showing which flags shifted. When *statespec* is left out, it returns the state flags currently turned on.

*statespec* will usually be a list or a tuple.

[Subject index](INDEX.md) · [Previous](tkinter-ttk-widget-class-to-identify.md) · [Continue](combobox.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Widget; identify](tkinter-ttk-widget-class-to-identify.md) · [Owning module, declaration or section: ttk.Widget](tkinter-ttk-widget-class-to-identify.md)
