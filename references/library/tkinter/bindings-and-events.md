# tkinter — Bindings and Events

### Bindings and Events

By way of the widget command’s bind method you can watch for particular events and have a callback function fire whenever that kind of event happens. The bind method takes this shape:

```python
def bind(self, sequence, func, add=''):

```

where:

sequence

is a string spelling out which kind of event you’re targeting. (For the particulars, turn to the *[bind(3tk)](https://manpages.debian.org/bind(3tk))* man page, along with John Ousterhout’s book — Tcl and the Tk Toolkit (2nd edition) — at page 201).

func

is a Python function of one argument, to be run when the event fires. An Event instance gets handed in as that argument. (Functions wired up like this typically go by the name *callbacks*.)

add

is optional, being either `''` or `'+'`. An empty string says this binding should supplant whatever other bindings this event already carries. A `'+'` says this function should join the roster of functions bound to this kind of event.

For example:

```python
def turn_red(self, event):
    event.widget["activeforeground"] = "red"

self.button.bind("<Enter>", self.turn_red)

```

See how the `turn_red()` callback reaches into the event’s widget field. That field holds whichever widget caught the X event. The table below sets out the remaining event fields available to you and the notation Tk gives each — handy when you’re cross-referencing the Tk man pages.

| Tk | Tkinter Event Field | Tk | Tkinter Event Field |
| --- | --- | --- | --- |
| %f | focus | %A | char |
| %h | height | %E | send_event |
| %k | keycode | %K | keysym |
| %s | state | %N | keysym_num |
| %t | time | %T | type |
| %w | width | %W | widget |
| %x | x | %X | x_root |
| %y | y | %Y | y_root |

[Subject index](INDEX.md) · [Previous](tk-option-data-types.md) · [Continue](the-index-parameter.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
