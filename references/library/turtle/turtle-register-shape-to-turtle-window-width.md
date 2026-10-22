# turtle: `turtle.register_shape()`, `turtle.addshape()`, `turtle.turtles()`, `turtle.window_height()`, `turtle.window_width()`

turtle.register_shape(*name*, *shape=None*)

 turtle.addshape(*name*, *shape=None*)

This function can be invoked in four distinct ways:

1.

*name* identifies an image file (PNG, GIF, PGM, and PPM) and *shape* is `None`: Register the matching image shape.

```python
>>> screen.register_shape("turtle.gif")

```

Note

Because image shapes *do not* spin as the turtle turns, the turtle’s heading is never shown by them!

2.

*name* is any string of your choosing and *shape* names an image file (PNG, GIF, PGM, and PPM): Register the matching image shape.

```python
>>> screen.register_shape("turtle", "turtle.gif")

```

Note

Because image shapes *do not* spin as the turtle turns, the turtle’s heading is never shown by them!

3.

*name* is any string of your choosing and *shape* is a tuple holding coordinate pairs: Register the matching polygon shape.

```pycon
>>> screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))

```

4.

*name* is any string of your choosing and *shape* is a (compound) `Shape` object: Register the matching compound shape.

Append a turtle shape onto the shapelist of TurtleScreen. Shapes are usable through the `shape(shapename)` command only once they have been registered this way.

Changed in version 3.14: The PNG, PGM, and PPM image formats are now supported. You may supply a shape name together with an image file name.

 turtle.turtles()

Provide the list of turtles present on the screen.

```pycon
>>> for turtle in screen.turtles():
...     turtle.color("red")

```

 turtle.window_height()

Provide the height of the turtle window.

```python
>>> screen.window_height()
480

```

 turtle.window_width()

Provide the width of the turtle window.

```python
>>> screen.window_width()
640

```

[Subject index](INDEX.md) · [Previous](turtle-mode-to-turtle-getshapes.md) · [Continue](turtle-bye-to-turtle-title.md) · [Owning module, declaration or section: Settings and special methods](turtle-mode-to-turtle-getshapes.md)
