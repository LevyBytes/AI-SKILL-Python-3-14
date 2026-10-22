# Run menu (Editor window only)

### Run menu (Editor window only)

Run Module

Perform Check Module. When there is no error, restart the shell to wipe the environment, then run the module. The Shell window shows the output. Keep in mind output relies on `print` or `write`. Once execution finishes, the Shell keeps focus and shows a prompt. From there you can interactively examine what the run produced. This resembles running a file via `python -i file` from a command line.

Run… Customized

Just like Run Module, except the module runs with customized settings. *Command Line Arguments* append to [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) exactly as though supplied on a command line. The module may run in the Shell with no restart.

Check Module

Verify the syntax of whichever module is currently open in the Editor window. When the module is unsaved, IDLE will either ask the user to save or autosave it, according to the choice on the General tab of the Idle Settings dialog. When a syntax error exists, its rough position is marked in the Editor window.

Python Shell

Open or wake up the Python Shell window.

[Subject index](INDEX.md) · [Previous](format-menu-editor-window-only.md) · [Continue](shell-menu-shell-window-only.md)
