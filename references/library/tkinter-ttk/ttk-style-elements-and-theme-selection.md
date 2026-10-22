# tkinter.ttk.Style: `element_names()`, `element_options()`, `theme_create()`, `theme_settings()`, `theme_names()`, `theme_use()`

element_names()

Returns the list of elements defined in the current theme.

 element_options(*elementname*)

Returns the list of *elementname*'s options.

 theme_create(*themename*, *parent=None*, *settings=None*)

Create a new theme.

Should *themename* already exist, that is an error. When *parent* is supplied, the new theme picks up styles, elements and layouts from the parent theme. When *settings* are given, they should follow the same syntax used for `theme_settings()`.

 theme_settings(*themename*, *settings*)

For a brief moment switches the active theme over to *themename*, applies the supplied *settings*, and afterward puts the earlier theme back.

Within *settings*, every key is a style and every value may carry the keys 'configure', 'map', 'layout' and 'element create', which should follow the same format specified by the methods `Style.configure()`, `Style.map()`, `Style.layout()` and `Style.element_create()` respectively.

By way of illustration, let's tweak the Combobox for the default theme a little:

```python
from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()
style.theme_settings("default", {
   "TCombobox": {
       "configure": {"padding": 5},
       "map": {
           "background": [("active", "green2"),
                          ("!disabled", "green4")],
           "fieldbackground": [("!disabled", "green3")],
           "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")]
       }
   }
})

combo = ttk.Combobox().pack()

root.mainloop()

```

 theme_names()

Returns a list of all known themes.

 theme_use(*themename=None*)

When *themename* is omitted, returns the theme currently in use. Failing that, sets the current theme to *themename*, refreshes every widget and fires a <&lt;ThemeChanged&gt;> event.

[Subject index](INDEX.md) · [Previous](tkinter-ttk-style-element-create.md) · [Continue](layouts.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Style](tkinter-ttk-style-class.md) · [Owning module, declaration or section: Ttk Styling](tkinter-ttk-style-class.md)
