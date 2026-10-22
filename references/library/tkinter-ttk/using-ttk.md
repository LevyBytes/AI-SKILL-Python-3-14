# tkinter.ttk — Using Ttk

### Using Ttk

Begin working with Ttk by importing its module:

```python
from tkinter import ttk

```

If you want to supersede the basic Tk widgets, place this import after the Tk import:

```python
from tkinter import *
from tkinter.ttk import *

```

The effect of that code is to have a number of `tkinter.ttk` widgets (`Button`, `Checkbutton`, `Entry`, `Frame`, `Label`, `LabelFrame`, `Menubutton`, `PanedWindow`, `Radiobutton`, `Scale` and `Scrollbar`) silently take the place of their Tk counterparts.

The immediate payoff is that you get the new widgets, which look and feel better across platforms; that said, the substitute widgets aren't entirely interchangeable. The chief discrepancy is that styling-related widget options like "fg", "bg" and similar ones no longer exist on Ttk widgets. To get refined styling effects, reach for the `ttk.Style` class instead.

See also

[Converting existing applications to use Tile widgets](https://tktable.sourceforge.net/tile/doc/converting.txt)

A monograph, framed in Tcl terminology, covering the discrepancies you'll commonly hit while porting applications over to the new widgets.

[Subject index](INDEX.md) · [Previous](tkinter-ttk-tk-themed-widgets.md) · [Continue](ttk-widgets.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
