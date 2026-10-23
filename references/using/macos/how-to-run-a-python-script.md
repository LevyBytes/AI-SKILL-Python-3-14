# 5.1.2. How to run a Python script

### 5.1.2. How to run a Python script

You can fire up the Python interpreter in two ways. Should a Unix shell in a terminal window be familiar territory, you can run `python3.14` or `python3`, optionally trailed by one or more command line options (covered in [Command line and environment](https://docs.python.org/3.14/using/cmdline.html#using-on-general)). There is also a handy section in the Python tutorial about [using Python interactively from a shell](https://docs.python.org/3.14/tutorial/appendix.html#tut-interac).

The interpreter can likewise be launched from an integrated development environment. [IDLE - Python editor and shell](https://docs.python.org/3.14/library/idle.html#idle) is a simple editor and interpreter environment bundled with Python's standard distribution. **IDLE** carries a Help menu giving you access to the Python documentation. Should Python be wholly new to you, the tutorial introduction is yours to read inside that document.

Plenty of other editors and IDEs exist as well; see [Editors and IDEs](https://docs.python.org/3.14/using/editors.html#editors) for further details.

From the terminal window, you can run a Python script file by handing the interpreter the script file's name:

>

`python3.14` `myscript.py`

To run your script from the Finder, you can either:

- Drag it onto **Python Launcher**.

- Through the Finder Info window, set **Python Launcher** as the default application for opening your script (or any `.py` script), then double-click it. **Python Launcher** offers a range of preferences governing how your script gets launched. Option-dragging lets you adjust these for a single invocation, or you can use its `Preferences` menu to change them globally.

Keep in mind that launching the script straight from the macOS Finder may yield different results than running it from a terminal window, since the script will not run inside the usual shell environment, which includes any environment variables set in shell profiles. And, just as with any other script or program, make sure you know what you are about to run.

[Subject index](INDEX.md) · [Previous source section](installation-steps.md) · [Following source section](alternative-distributions.md)
