# tkinter.ttk.Style: `configure()`, `map()`, `lookup()`

configure(*style*, *query_opt=None*, ***kw*)

Within *style*, query or assign the default value held by the named option(s).

Within *kw*, every key is an option and every value is a string naming that option's value.

For instance, to make every default button into a flat button carrying some padding and a different background color:

```python
from tkinter import ttk
import tkinter

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

btn = ttk.Button(text="Sample")
btn.pack()

root.mainloop()

```

 map(*style*, *query_opt=None*, ***kw*)

Within *style*, query or assign the dynamic values held by the named option(s).

Within *kw*, every key is an option and every value should be a list or a tuple (typically) holding statespecs grouped inside tuples, lists, or another arrangement of choice. A statespec pairs one or more states together with a value.

A worked example may clear this up:

```python
import tkinter
from tkinter import ttk

root = tkinter.Tk()

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

root.mainloop()

```

Keep in mind that the ordering of the (states, value) sequences for an option is significant; were the order switched to `[('active', 'blue'), ('pressed', 'red')]` in the foreground option, say, the outcome would be a blue foreground while the widget sat in the active or pressed states.

 lookup(*style*, *option*, *state=None*, *default=None*)

Returns the value specified for *option* in *style*.

When *state* is supplied, it should be a sequence of one or more states. When the *default* argument is provided, it acts as a fallback value should no specification for option turn up.

To find out which font a Button uses by default:

```python
from tkinter import ttk

print(ttk.Style().lookup("TButton", "font"))

```

[Subject index](INDEX.md) · [Previous](tkinter-ttk-style-class.md) · [Continue](tkinter-ttk-style-layout.md) · [Owning module, declaration or section: tkinter.ttk](tkinter-ttk-tk-themed-widgets.md) · [Owning module, declaration or section: tkinter.ttk.Style](tkinter-ttk-style-class.md) · [Owning module, declaration or section: Ttk Styling](tkinter-ttk-style-class.md)
