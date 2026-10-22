# Python 3.6.0 alpha 1 / idle / functions and types

[bpo-25507](https://bugs.python.org/issue?@action=redirect&bpo=25507): Corrected a faulty change in IOBinding that had blocked printing. The IOBinding htest is broadened to exercise every major IOBinding function.

[bpo-24455](https://bugs.python.org/issue?@action=redirect&bpo=24455): Keep IDLE from hanging in cases where you a) close the shell while the debugger is running (15347); b) close the debugger using the [X] button (15348); and c) start up the debugger when it is already running (24455). Mark Roseman's patch accomplishes this with two adjustments. 1. Suspend and resume the gui.interaction method by means of the tcl vwait mechanism designed for exactly this (rather than root.mainloop & .quit). 2. Inside gui.run, let any ongoing interaction finish first.

- In an IDLE "kill program"? message, "The program" becomes "Your program" so it is plainer that the program in question is the user program presently running, not IDLE itself.

[bpo-24988](https://bugs.python.org/issue?@action=redirect&bpo=24988): Idle ScrolledList context menus (the ones used in the debugger) now function on Mac Aqua. Mark Roseman contributed this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
