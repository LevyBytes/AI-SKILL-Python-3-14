# turtle: `turtle.onclick()`, `turtle.onscreenclick()`, `turtle.ontimer()`, `turtle.mainloop()`, `turtle.done()`

turtle.onclick(*fun*, *btn=1*, *add=None*)

 turtle.onscreenclick(*fun*, *btn=1*, *add=None*)

Parameters:

- **fun** – a function taking two arguments, which will receive the coordinates of the point clicked on the canvas

- **btn** – number of the mouse-button, defaults to 1 (left mouse button)

- **add** – `True` or `False` – when `True`, an additional binding is registered; otherwise it supersedes an earlier binding

Attach *fun* to mouse-click events occurring on this screen. When *fun* is `None`, present bindings get cleared.

Example using a TurtleScreen instance named `screen` together with a Turtle instance named `turtle`:

```pycon
>>> screen.onclick(turtle.goto) # Subsequently clicking into the TurtleScreen will
>>>                             # make the turtle move to the clicked point.
>>> screen.onclick(None)        # remove event binding again

```

Note

This TurtleScreen method is reachable as a global function exclusively under the name `onscreenclick`. The global function `onclick` is a separate one, derived from the Turtle method `onclick`.

 turtle.ontimer(*fun*, *t=0*)

Parameters:

- **fun** – a function with no arguments

- **t** – a number >= 0

Set up a timer that invokes *fun* once *t* milliseconds have elapsed.

```pycon
>>> running = True
>>> def f():
...     if running:
...         fd(50)
...         lt(60)
...         screen.ontimer(f, 250)
>>> f()   ### makes the turtle march around
>>> running = False

```

 turtle.mainloop()

 turtle.done()

Begins the event loop — invoking Tkinter's mainloop function. It has to be the final statement within a turtle graphics program. It must *not* be invoked when a script runs inside IDLE in -n mode (No subprocess) — used for interactive turtle graphics.

```python
>>> screen.mainloop()

```

[Subject index](INDEX.md) · [Previous](turtle-listen-to-turtle-onkeypress.md) · [Continue](turtle-textinput-to-turtle-numinput.md) · [Owning module, declaration or section: Using screen events](turtle-listen-to-turtle-onkeypress.md)
