# tkinter - Architecture

### Architecture

Far from being one monolithic library, Tcl/Tk is made of several separate modules, each carrying its own functionality and its own official documentation. Python’s binary releases additionally bundle an add-on module alongside it.

Tcl

Much like Python, Tcl is a dynamic, interpreted programming language. While it can stand alone as a general-purpose language, its most frequent role is being embedded inside C applications, either as a scripting engine or as the gateway to the Tk toolkit. Through its C interface, the Tcl library lets you create and manage one or more Tcl interpreter instances, run Tcl commands and scripts within them, and register custom commands written in either Tcl or C. Every interpreter owns an event queue, and there are mechanisms for dispatching events to it and handling them. Whereas Python differs here, Tcl’s execution model is built around cooperative multitasking, a gap that Tkinter spans (consult Threading model for the specifics).

Tk

Implemented in C, Tk is a [Tcl package](https://wiki.tcl-lang.org/37432) that contributes custom commands for building and operating on GUI widgets. Every `Tk` object carries its own embedded Tcl interpreter instance with Tk loaded inside. Although Tk’s widgets are highly customizable, that flexibility comes paired with an outdated look. To produce and dispatch GUI events, Tk relies on Tcl’s event queue.

Ttk

A newer collection of Tk widgets, Themed Tk (Ttk) delivers a far better appearance across platforms than a lot of the classic Tk widgets manage. As of Tk version 8.5, Ttk ships as part of Tk. A dedicated module, [`tkinter.ttk`](https://docs.python.org/3.14/library/tkinter.ttk.html#module-tkinter.ttk), supplies the Python bindings.

Beneath the surface, Tk and Ttk draw on services from the host operating system — that is, Xlib on Unix/X11, Cocoa on macOS, GDI on Windows.

Say your Python program uses one of Tkinter’s classes, for instance to build a widget: the `tkinter` module begins by composing a Tcl/Tk command string. That string is handed off to an internal `_tkinter` binary module, which in turn asks the Tcl interpreter to evaluate it. From there the Tcl interpreter invokes the Tk and/or Ttk packages, which themselves issue calls to Xlib, Cocoa, or GDI.

[Subject index](INDEX.md) · [Previous](tkinter-python-interface-to-tcl-tk.md) · [Continue](tkinter-modules.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
