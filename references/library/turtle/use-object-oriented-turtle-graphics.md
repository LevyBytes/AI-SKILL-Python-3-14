# Use object-oriented turtle graphics

### Use object-oriented turtle graphics

See also

Explanation of the object-oriented interface

Apart from the most elementary introductions, or for quick experimentation, the object-oriented style of turtle graphics is the more customary and far more capable choice. It lets you, for one, place several turtles on the screen simultaneously.

Under this style, the assorted turtle commands act as methods on objects (chiefly `Turtle` objects). You *can* reach for the object-oriented style inside the shell, yet it tends to suit a Python script better.

Reworked into that form, the earlier example reads:

```python
from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()

```

Pay attention to that closing line. `t.screen` refers to the `Screen` instance hosting a given Turtle; it springs into being automatically alongside the turtle.

The screen belonging to the turtle accepts customization, such as:

```python
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("orange")

```

[Subject index](INDEX.md) · [Previous](use-turtle-graphics-in-a-script.md) · [Continue](turtle-graphics-reference.md)
