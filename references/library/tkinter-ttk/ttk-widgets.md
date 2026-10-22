# tkinter.ttk — Ttk Widgets

### Ttk Widgets

Ttk ships with 18 widgets, of which twelve were already part of tkinter: `Button`, `Checkbutton`, `Entry`, `Frame`, `Label`, `LabelFrame`, `Menubutton`, `PanedWindow`, `Radiobutton`, `Scale`, `Scrollbar`, and `Spinbox`. The remaining six are newcomers: `Combobox`, `Notebook`, `Progressbar`, `Separator`, `Sizegrip` and `Treeview`. Every one of them descends from `Widget`.

Adopting the Ttk widgets lends your application a nicer look and feel. Per the discussion above, the way styling gets written differs.

Tk code:

```python
l1 = tkinter.Label(text="Test", fg="black", bg="white")
l2 = tkinter.Label(text="Test", fg="black", bg="white")

```

Ttk code:

```python
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

```

To learn more about TtkStyling, turn to the `Style` class documentation.

[Subject index](INDEX.md) · [Previous](using-ttk.md) · [Continue](widget.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md)
