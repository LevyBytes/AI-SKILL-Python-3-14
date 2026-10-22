# tkinter.ttk.Style: `layout()`

layout(*style*, *layoutspec=None*)

Establish the widget layout belonging to the supplied *style*. Should *layoutspec* be left out, the layout specification for that style is returned instead.

When *layoutspec* is given, it should be a list or another sequence type (strings excluded), where every item should be a tuple whose first item is the layout name and whose second item should follow the format laid out under Layouts.

To grasp the format, study the example that follows (it is not meant to accomplish anything useful):

```python
from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()
style.layout("TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "left", "expand": 1})]
           })]
       })]
   }),
])

mbtn = ttk.Menubutton(text='Text')
mbtn.pack()
root.mainloop()

```

[Subject index](INDEX.md) · [Previous](tkinter-ttk-style-configure-to-tkinter-ttk-style-lookup.md) · [Continue](tkinter-ttk-style-element-create.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Style](tkinter-ttk-style-class.md) · [Owning module, declaration or section: Ttk Styling](tkinter-ttk-style-class.md)
