# turtle: `turtle.poly()`, `turtle.begin_poly()`, `turtle.end_poly()`, `turtle.get_poly()`, `turtle.clone()`, `turtle.getturtle()`, `turtle.getpen()`, `turtle.getscreen()`

### Special Turtle methods

 turtle.poly()

Capture the vertices of a polygon drawn within the `with turtle.poly():` block. A connection joins the first and last vertices.

```pycon
>>> with turtle.poly():
...     turtle.forward(100)
...     turtle.right(60)
...     turtle.forward(100)

```

Added in version 3.14.

 turtle.begin_poly()

Begin capturing a polygon's vertices. The turtle's present position becomes the polygon's first vertex.

 turtle.end_poly()

Halt the capture of a polygon's vertices. The turtle's present position becomes the polygon's last vertex. A connection will join it to the first vertex.

 turtle.get_poly()

Hand back the polygon captured most recently.

```pycon
>>> turtle.home()
>>> turtle.begin_poly()
>>> turtle.fd(100)
>>> turtle.left(20)
>>> turtle.fd(30)
>>> turtle.left(60)
>>> turtle.fd(50)
>>> turtle.end_poly()
>>> p = turtle.get_poly()
>>> register_shape("myFavouriteShape", p)

```

 turtle.clone()

Build and hand back a clone of the turtle carrying the same position, heading and turtle properties.

```pycon
>>> mick = Turtle()
>>> joe = mick.clone()

```

 turtle.getturtle()

 turtle.getpen()

Hand back the Turtle object itself. Its one sensible use: as a function that yields the “anonymous turtle”:

```pycon
>>> pet = getturtle()
>>> pet.fd(50)
>>> pet
<turtle.Turtle object at 0x...>

```

 turtle.getscreen()

Hand back the `TurtleScreen` object on which the turtle draws. TurtleScreen methods may then be invoked on that object.

```pycon
>>> ts = turtle.getscreen()
>>> ts
<turtle._Screen object at 0x...>
>>> ts.bgcolor("pink")

```

[Subject index](INDEX.md) · [Previous](turtle-ondrag.md) · [Continue](turtle-setundobuffer-to-turtle-undobufferentries.md)
