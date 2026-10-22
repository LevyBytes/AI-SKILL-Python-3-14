# turtle: `turtle.listen()`, `turtle.onkey()`, `turtle.onkeyrelease()`, `turtle.onkeypress()`

### Using screen events

 turtle.listen(*xdummy=None*, *ydummy=None*)

Put focus on the TurtleScreen (so it can gather key-events). The dummy arguments exist so that `listen()` can be handed to the onclick method.

 turtle.onkey(*fun*, *key*)

 turtle.onkeyrelease(*fun*, *key*)

Parameters:

- **fun** – a function with no arguments or `None`

- **key** – a string holding a key (such as “a”) or a key-symbol (such as “space”)

Attach *fun* to the key-release event of key. When *fun* is `None`, event bindings get cleared. Remark: registering key-events requires that the TurtleScreen hold the focus. (See method `listen()`.)

```pycon
>>> def f():
...     fd(50)
...     lt(60)
...
>>> screen.onkey(f, "Up")
>>> screen.listen()

```

 turtle.onkeypress(*fun*, *key=None*)

Parameters:

- **fun** – a function with no arguments or `None`

- **key** – a string holding a key (such as “a”) or a key-symbol (such as “space”)

Attach *fun* to the key-press event of key when key is supplied, or to every key-press-event when no key is supplied. Remark: registering key-events requires that the TurtleScreen hold focus. (See method `listen()`.)

```pycon
>>> def f():
...     fd(50)
...
>>> screen.onkey(f, "Up")
>>> screen.listen()

```

[Subject index](INDEX.md) · [Previous](turtle-no-animation-to-turtle-update.md) · [Continue](turtle-onclick-to-turtle-done.md)
