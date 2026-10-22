# Python 3.5.1 release candidate 1 / idle / functions and types

[bpo-24455](https://bugs.python.org/issue?@action=redirect&bpo=24455): Keep IDLE from freezing in three situations: a) shutting the shell while the debugger remains active (15347); b) dismissing the debugger via the [X] button (15348); and c) turning on the debugger when it is already running (24455). Mark Roseman's patch accomplishes this through two adjustments. 1. Pause and continue the gui.interaction method by way of the tcl vwait mechanism designed for it (rather than root.mainloop & .quit). 2. Within gui.run, let any in-progress interaction finish first.

- In the IDLE "kill program"? prompt, swap "The program" for "Your program" so it is plainer that the reference is to the user program now running, not to IDLE.

[bpo-24988](https://bugs.python.org/issue?@action=redirect&bpo=24988): The Idle ScrolledList context menus, which the debugger uses, now function under Mac Aqua. Mark Roseman contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
