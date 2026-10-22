# How do I freeze Tkinter applications?

### Tkinter questions

### How do I freeze Tkinter applications?

Freeze is a tool for producing stand-alone applications. Frozen Tkinter applications won't actually be stand-alone, however, since they'll still depend on the Tcl and Tk libraries.

One approach is to bundle the application alongside the Tcl and Tk libraries and direct it to them at run-time through the `TCL_LIBRARY` and `TK_LIBRARY` environment variables.

A number of third-party freeze libraries, such as py2exe and cx_Freeze, come with built-in support for Tkinter applications.

[Subject index](INDEX.md)
