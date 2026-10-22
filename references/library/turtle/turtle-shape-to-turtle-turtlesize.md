# Appearance: `turtle.shape()`, `turtle.resizemode()`, `turtle.shapesize()`, `turtle.turtlesize()`

#### Appearance

 turtle.shape(*name=None*)

Parameters:

**name** – a string which is a valid shapename

Give the turtle the shape named *name*; when no name is supplied, hand back the name of the current shape. A shape carrying *name* has to be present in the TurtleScreen's shape dictionary. The starting set of polygon shapes is: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”. For details on handling shapes, consult the Screen method `register_shape()`.

```pycon
>>> turtle.shape()
'classic'
>>> turtle.shape("turtle")
>>> turtle.shape()
'turtle'

```

 turtle.resizemode(*rmode=None*)

Parameters:

**rmode** – one of the strings “auto”, “user”, “noresize”

Assign resizemode one of these values: “auto”, “user”, “noresize”. When *rmode* is omitted, hand back the current resizemode. The various resizemodes behave as follows:

- “auto”: matches the turtle's look to the current pensize value.

- “user”: matches the turtle's look to the stretchfactor and outlinewidth (outline) values, which `shapesize()` sets.

- “noresize”: the turtle's look is never adapted.

`shapesize()`, when invoked with arguments, itself calls `resizemode("user")`.

```pycon
>>> turtle.resizemode()
'noresize'
>>> turtle.resizemode("auto")
>>> turtle.resizemode()
'auto'

```

 turtle.shapesize(*stretch_wid=None*, *stretch_len=None*, *outline=None*)

 turtle.turtlesize(*stretch_wid=None*, *stretch_len=None*, *outline=None*)

Parameters:

- **stretch_wid** – positive number

- **stretch_len** – positive number

- **outline** – positive number

Read or assign the pen's x/y-stretchfactors and/or outline attributes. Sets resizemode to “user”. Only when resizemode equals “user” will the turtle render stretched per its stretchfactors: *stretch_wid* is the stretchfactor at right angles to its orientation, *stretch_len* is the stretchfactor along its orientation, and *outline* fixes the width of the shape's outline.

```pycon
>>> turtle.shapesize()
(1.0, 1.0, 1)
>>> turtle.resizemode("user")
>>> turtle.shapesize(5, 5, 12)
>>> turtle.shapesize()
(5, 5, 12)
>>> turtle.shapesize(outline=8)
>>> turtle.shapesize()
(5, 5, 8)

```

[Subject index](INDEX.md) · [Previous](turtle-hideturtle-to-turtle-isvisible.md) · [Continue](turtle-shearfactor-to-turtle-tiltangle.md)
