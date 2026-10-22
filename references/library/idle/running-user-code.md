# Running user code

### Running user code

Barring a few exceptions, running Python code through IDLE is meant to give the very same outcome as running that code the usual way — straight through Python inside a text-mode system console or terminal window. Even so, the distinct interface and behavior can now and then change what you actually see. As an example, `sys.modules` begins with extra entries, and `threading.active_count()` comes back as 2 instead of 1.

Out of the box, IDLE executes user code inside a separate OS process rather than within the user-interface process hosting the shell and editor. Inside that execution process, it swaps out `sys.stdin`, `sys.stdout`, and `sys.stderr` for objects that draw input from, and push output to, the Shell window. The originals kept in `sys.__stdin__`, `sys.__stdout__`, and `sys.__stderr__` stay untouched, though they may hold `None`.

Routing print output from one process into a text widget belonging to another runs slower than printing to a system terminal within the same process. The slowdown is most pronounced with several arguments, because each argument's string, each separator, and the newline travel one at a time. For development this rarely matters, but to speed up printing in IDLE, build and join everything you want shown into one piece and print that single string. Format strings as well as [`str.join()`](https://docs.python.org/3.14/library/stdtypes.html#str.join) are both handy for stitching fields and lines together.

Subprocesses spawned inside the execution process — whether directly by user code or by modules like multiprocessing — don't inherit IDLE's standard stream replacements. When such a subprocess uses `input` on sys.stdin, or `print` or `write` on sys.stdout or sys.stderr, you should launch IDLE from a command-line window. (Under Windows, choose `python` or `py` instead of `pythonw` or `pyw`.) The secondary subprocess then binds to that window for its input and output.

Reset `sys` from within user code — say through `importlib.reload(sys)` — and IDLE's modifications vanish, leaving keyboard input and screen output broken.

While the Shell holds focus, it owns the keyboard and screen. That's ordinarily seamless, but any function that reaches straight for the keyboard and screen won't operate. Among these are the platform-specific functions that report whether a key was pressed and, if so, which one.

IDLE's code in the execution process pushes extra frames onto the call stack that wouldn't be present otherwise. To soften the impact of those added stack frames, IDLE wraps `sys.getrecursionlimit` and `sys.setrecursionlimit`.

Should user code raise SystemExit, either on its own or via sys.exit, IDLE drops back to a Shell prompt rather than shutting down.

[Subject index](INDEX.md) · [Previous](startup-failure.md) · [Continue](user-output-in-shell.md)
