# tkinter — How do I…? What option does…?

### How do I…? What option does…?

If how to accomplish something in Tkinter eludes you, and you can’t spot it straight away in whatever tutorial or reference documentation you’re consulting, a few tactics may come in handy.

To start, keep in mind that the particulars of how individual widgets behave can shift between different versions of Tkinter and of Tcl/Tk alike. When you search the documentation, be sure it lines up with the Python and Tcl/Tk versions present on your system.

In searching for how to wield an API, knowing the precise name of the class, option, or method you’re after helps. Introspection — whether in an interactive Python shell or by way of [`print()`](https://docs.python.org/3.14/library/functions.html#print) — can help you work out what you need.

To discover which configuration options a given widget exposes, call its `configure()` method; it returns a dictionary packed with assorted information about each object, default and current values included. Reach for `keys()` to pull out just the names of each option.

```python
btn = ttk.Button(frm, ...)
print(btn.configure().keys())

```

Because the great majority of widgets share so many configuration options, it’s often worthwhile to single out those unique to one particular widget class. One way to do so is to contrast the option list against that of a simpler widget, like a frame.

```python
print(set(btn.configure().keys()) - set(frm.configure().keys()))

```

In the same vein, you can list the methods available on a widget object via the standard [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) function. Give it a try and you’ll find over 200 common widget methods, so once more it helps to single out the ones particular to a widget class.

```python
print(dir(btn))
print(set(dir(btn)) - set(dir(frm)))

```

[Subject index](INDEX.md) · [Previous](understanding-how-tkinter-wraps-tcl-tk.md) · [Continue](navigating-the-tcl-tk-reference-manual.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
