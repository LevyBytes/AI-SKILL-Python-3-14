# Visibility

### Turtle state

#### Visibility

 turtle.hideturtle()

 turtle.ht()

Render the turtle invisible. Doing so partway through an elaborate drawing is wise, since a hidden turtle makes the drawing run noticeably faster.

```pycon
>>> turtle.hideturtle()

```

 turtle.showturtle()

 turtle.st()

Render the turtle visible.

```pycon
>>> turtle.showturtle()

```

 turtle.isvisible()

Hand back `True` when the Turtle is shown and `False` when it's hidden.

```python
>>> turtle.hideturtle()
>>> turtle.isvisible()
False
>>> turtle.showturtle()
>>> turtle.isvisible()
True

```

[Subject index](INDEX.md) · [Continue](turtle-shape-to-turtle-turtlesize.md)
