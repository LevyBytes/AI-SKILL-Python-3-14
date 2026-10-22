# tkinter: Tkinter modules and Tk interpreter construction

### Tkinter Modules

Tkinter’s support is split among a handful of modules. The bulk of applications will require the central `tkinter` module, along with the [`tkinter.ttk`](https://docs.python.org/3.14/library/tkinter.ttk.html#module-tkinter.ttk) module, the source of the modern themed widget set and API:

```python
from tkinter import *
from tkinter import ttk

```

```text
class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
```

Build a toplevel Tk widget — typically the application’s main window — and set up a Tcl interpreter for it. Every instance is paired with its own Tcl interpreter.

Most often the `Tk` class is created with all defaults left in place. Even so, these keyword arguments are recognized at present:

*screenName*

If supplied (as a string), this sets the `DISPLAY` environment variable. (X11 only)

*baseName*

The profile file’s name. By default *baseName* comes from the program name (`sys.argv[0]`).

*className*

The widget class’s name. Serves both as a profile file and as the name under which Tcl is launched (*argv0* in *interp*).

*useTk*

When `True`, the Tk subsystem is initialized. The `tkinter.Tcl()` function flips this to `False`.

*sync*

When `True`, every X server command runs synchronously so that errors surface right away. Handy for debugging. (X11 only)

*use*

Gives the *id* of the window into which the application should be embedded, instead of creating it as a standalone toplevel window. The *id* must be given the same way as the value of the -use option for toplevel widgets (that is, taking a form like what `winfo_id()` returns).

Be aware that on certain platforms this works properly only when *id* points to a Tk frame or toplevel whose -container option is turned on.

`Tk` loads and interprets profile files — named `.*className*.tcl` and `.*baseName*.tcl` — into the Tcl interpreter, and runs [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) over the contents of `.*className*.py` and `.*baseName*.py`. These profile files are located via the `HOME` environment variable or, when that is undefined, via [`os.curdir`](https://docs.python.org/3.14/library/os.html#os.curdir).

 tk

The Tk application object you obtain by instantiating `Tk`. It grants access to the Tcl interpreter. Any widget bound to the same `Tk` instance shares an identical value for its `tk` attribute.

 master

The widget object acting as this widget’s container. In the case of `Tk`, `master` is [`None`](https://docs.python.org/3.14/library/constants.html#None) since it stands as the main window. As argument names, *master* and *parent* are alike and at times swapped freely; that said, `winfo_parent()` hands back a string holding the widget name while `master` hands back the object. The *parent*/*child* pairing mirrors the tree-like relationship, whereas *master* (or *container*)/*content* mirrors the containment structure.

 children

This widget’s direct descendants, given as a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) whose keys are the child widget names and whose values are the child instance objects.

[Subject index](INDEX.md) · [Previous](architecture.md) · [Continue](tkinter-tcl-to-tkinter-dnd.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
