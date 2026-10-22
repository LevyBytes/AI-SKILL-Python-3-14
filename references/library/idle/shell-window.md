# Shell window

### Shell window

Within IDLE’s Shell, type, edit, and recall whole statements. (Most consoles and terminals handle only one physical line at a time.)

Send a single-line statement to be run by pressing Return with the cursor anywhere along the line. When a line is continued using Backslash (\), the cursor has to sit on the final physical line. Send a multi-line compound statement by adding a blank line after it.

Pasting code into Shell does not compile or possibly run it until Return is pressed, as described above. The pasted code may be edited first. Pasting more than one statement into Shell yields a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), because the multiple statements get compiled as though they were one.

A line holding `RESTART` signals that the user execution process has restarted. That happens when the user execution process has crashed, when a restart is requested from the Shell menu, or when code is run in an editor window.

The editing features covered in earlier subsections apply while typing code interactively. IDLE’s Shell window further responds to these:

- C-c attempts to interrupt statement execution (but may fail).

- C-d closes Shell if typed at a `>>>` prompt.

- Alt-p and Alt-n (C-p and C-n on macOS) pull up to the current prompt whichever earlier or later prior statement matches what you have already typed.

- Pressing Return with the cursor resting on an earlier statement tacks that statement onto whatever is already typed at the prompt.

[Subject index](INDEX.md) · [Previous](code-context.md) · [Continue](text-colors.md)
