# Startup failure

### Startup failure

To talk between the IDLE GUI process and the process that runs user code, IDLE relies on a socket. Each time the Shell starts up or restarts, a connection has to be made. (A restart shows up as a divider line reading ‘RESTART’.) When the user process can't reach the GUI process, what you usually get is a `Tk` error box bearing a ‘cannot connect’ message that points the user to this page, after which it quits.

On Unix systems, one particular kind of connection failure traces back to masquerading rules that have been misconfigured somewhere in the machine's network setup. Start IDLE from a terminal and you'll see a message that opens with `** Invalid host:`. Its correct value is `127.0.0.1 (idlelib.rpc.LOCALHOST)`. To investigate, run `tcpconnect -irv 127.0.0.1 6543` in one terminal window and `tcplisten <same args>` in a second.

Failures often come from a file the user wrote that shares its name with a standard library module — *random.py* and *tkinter.py* are typical examples. With such a file sitting in the same directory as the one about to run, IDLE is unable to import the stdlib module. For now the remedy is to rename the user's file.

Rarer than it once was, an antivirus or firewall tool can still block the connection. When that tool can't be configured to permit it, you have to disable it for IDLE to operate. Permitting this internal connection poses no risk, since nothing is exposed on external ports. A related trouble is network misconfiguration that prevents connections.

Now and then a Python installation problem halts IDLE: several versions may conflict, or one install may demand admin rights. If you resolve the conflict, or you can't or would rather not run as admin, the simplest path is often to uninstall Python completely and begin afresh.

A lingering pythonw.exe process can also cause trouble. Under Windows, open Task Manager to look for one and end it if present. Occasionally a restart set off by a program crash or by a Keyboard Interrupt (control-C) won't reconnect. Closing the error box, or choosing Restart Shell from the Shell menu, can clear up a passing glitch.

On first launch, IDLE tries to read the user's configuration files at `~/.idlerc/` (with ~ standing for one's home directory). Any trouble there ought to surface an error message. Random disk hiccups aside, you can head this off by never hand-editing those files; rely on the configuration dialog beneath Options instead. Once a user configuration file is corrupted, your best bet may be to remove it and rebuild it from the settings dialog.

When IDLE exits silently and you didn't launch it from a console, try launching it from a console or terminal with `python -m idlelib` to see whether an error message turns up.

Under Unix-based systems running tcl/tk earlier than `8.6.11` (check `About IDLE`), particular characters in particular fonts can provoke a tk failure that prints a message to the terminal. It may strike when you open IDLE to edit a file holding such a character, or later as you type one. Where upgrading tcl/tk isn't possible, switch IDLE over to a font that handles things better.

[Subject index](INDEX.md) · [Previous](command-line-usage.md) · [Continue](running-user-code.md)
