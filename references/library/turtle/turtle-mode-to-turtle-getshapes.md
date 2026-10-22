# turtle: `turtle.mode()`, `turtle.colormode()`, `turtle.getcanvas()`, `turtle.getshapes()`

### Settings and special methods

 turtle.mode(*mode=None*)

Parameters:

**mode** – one of the strings “standard”, “logo” or “world”

Configure the turtle mode (“standard”, “logo” or “world”) and trigger a reset. When no mode argument is passed, the active mode is returned instead.

The “standard” mode matches the behaviour of the old `turtle`. The “logo” mode aligns with the majority of Logo turtle graphics. The “world” mode relies on user-defined “world coordinates”. **Attention**: under this mode, angles look skewed whenever the `x/y` unit-ratio differs from 1.

| Mode | Initial turtle heading | positive angles |
| --- | --- | --- |
| “standard” | to the right (east) | counterclockwise |
| “logo” | upward (north) | clockwise |

```pycon
>>> mode("logo")   # resets turtle heading to north
>>> mode()
'logo'

```

 turtle.colormode(*cmode=None*)

Parameters:

**cmode** – one of the values 1.0 or 255

Either report the current colormode or assign it the value 1.0 or 255. From then on, the *r*, *g*, *b* components of color triples must fall within 0..*cmode*.

```pycon
>>> screen.colormode(1)
>>> turtle.pencolor(240, 160, 80)
Traceback (most recent call last):
     ...
TurtleGraphicsError: bad color sequence: (240, 160, 80)
>>> screen.colormode()
1.0
>>> screen.colormode(255)
>>> screen.colormode()
255
>>> turtle.pencolor(240,160,80)

```

 turtle.getcanvas()

Hand back the Canvas belonging to this TurtleScreen. Handy for advanced users who understand how to work with a Tkinter Canvas.

```pycon
>>> cv = screen.getcanvas()
>>> cv
<turtle.ScrolledCanvas object ...>

```

 turtle.getshapes()

Provide a list containing the names of every turtle shape currently on hand.

```pycon
>>> screen.getshapes()
['arrow', 'blank', 'circle', ..., 'turtle']

```

[Subject index](INDEX.md) · [Previous](input-methods.md) · [Continue](turtle-register-shape-to-turtle-window-width.md)
