# turtle: `turtle.pen()`

turtle.pen(*pen=None*, ***pendict*)

Parameters:

- **pen** ? a dictionary with some or all of the below listed keys

- **pendict** ? one or several keyword-arguments whose keywords are the keys listed below

Read back or assign the pen's attributes via a ?pen-dictionary? holding these key/value pairs:

- ?shown?: True/False

- ?pendown?: True/False

- ?pencolor?: color-string or color-tuple

- ?fillcolor?: color-string or color-tuple

- ?pensize?: positive number

- ?speed?: number in range 0..10

- ?resizemode?: ?auto? or ?user? or ?noresize?

- ?stretchfactor?: (positive number, positive number)

- ?outline?: positive number

- ?tilt?: number

Such a dictionary may be passed into a later `pen()` call to bring back the earlier pen-state. Beyond that, one or several of these attributes can arrive as keyword-arguments, which lets you assign multiple pen attributes within a single statement.

```pycon
>>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
>>> sorted(turtle.pen().items())
[('fillcolor', 'black'), ('outline', 1), ('pencolor', 'red'),
 ('pendown', True), ('pensize', 10), ('resizemode', 'noresize'),
 ('shearfactor', 0.0), ('shown', True), ('speed', 9),
 ('stretchfactor', (1.0, 1.0)), ('tilt', 0.0)]
>>> penstate=turtle.pen()
>>> turtle.color("yellow", "")
>>> turtle.penup()
>>> sorted(turtle.pen().items())[:3]
[('fillcolor', ''), ('outline', 1), ('pencolor', 'yellow')]
>>> turtle.pen(penstate, fillcolor="green")
>>> sorted(turtle.pen().items())[:3]
[('fillcolor', 'green'), ('outline', 1), ('pencolor', 'red')]

```

[Subject index](INDEX.md) · [Previous](turtle-pendown-to-turtle-width.md) · [Continue](turtle-isdown.md) · [Owning module, declaration or section: Drawing state](turtle-pendown-to-turtle-width.md)
