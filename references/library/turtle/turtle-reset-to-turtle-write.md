# More drawing control

#### More drawing control

 turtle.reset()

Erase this turtle's drawings off the screen, move the turtle back to center, and restore variables to their defaults.

```pycon
>>> turtle.goto(0,-22)
>>> turtle.left(100)
>>> turtle.position()
(0.00,-22.00)
>>> turtle.heading()
100.0
>>> turtle.reset()
>>> turtle.position()
(0.00,0.00)
>>> turtle.heading()
0.0

```

 turtle.clear()

Erase this turtle's drawings off the screen. The turtle stays put. Neither the turtle's state and position nor the drawings made by other turtles are touched.

 turtle.write(*arg*, *move=False*, *align='left'*, *font=('Arial', 8, 'normal')*)

Parameters:

- **arg** – object to be written to the TurtleScreen

- **move** – True/False

- **align** – one of the strings “left”, “center” or right”

- **font** – a triple (fontname, fontsize, fonttype)

Place text — the string form of *arg* — at the turtle's present position, governed by *align* (“left”, “center” or “right”) and rendered in the supplied font. When *move* is true, the pen advances to the text's bottom-right corner. The default for *move* is `False`.

```python
>>> turtle.write("Home = ", True, align="center")
>>> turtle.write((0,0), True)

```

[Subject index](INDEX.md) · [Previous](turtle-filling-to-turtle-end-fill.md) · [Continue](turtle-hideturtle-to-turtle-isvisible.md)
