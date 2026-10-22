# Developing tkinter applications

### Developing tkinter applications

By design, IDLE departs from standard Python to make building tkinter programs easier. Type `import tkinter as tk; root = tk.Tk()` into standard Python and nothing shows up; type the very same thing into IDLE and a tk window opens. With standard Python you also have to type `root.update()` before the window appears. IDLE performs that same step for you behind the scenes, roughly 20 times each second — that is, about once every 50 milliseconds. Then type `b = tk.Button(root, text='button'); b.pack()`. Once more, standard Python shows no visible change until you type `root.update()`.

The bulk of tkinter programs call `root.mainloop()`, which as a rule won't return until the tk app is torn down. Run the program with `python -i` or from an IDLE editor and the `>>>` shell prompt holds off appearing until `mainloop()` returns — by which point nothing remains to interact with.

If you run a tkinter program from an IDLE editor, you can comment out the mainloop call. That gives you a shell prompt right away and lets you work with the running application. The one thing to remember is to put the mainloop call back when you run under standard Python.

[Subject index](INDEX.md) · [Previous](user-output-in-shell.md) · [Continue](running-without-a-subprocess.md)
