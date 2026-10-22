# turtle: `turtle.speed()`

turtle.speed(*speed=None*)

Parameters:

**speed** ? a whole number from 0..10, or else a speedstring (described further down)

Fix the turtle's speed to a whole number from 0..10. Call it without an argument and the present speed comes back.

When the value passed exceeds 10 or drops below 0.5, the speed becomes 0. The mapping from speedstrings to speedvalues runs like this:

- ?fastest?: 0

- ?fast?: 10

- ?normal?: 6

- ?slow?: 3

- ?slowest?: 1

Across the 1 to 10 range, higher numbers drive progressively quicker animation of both line drawing and turtle turning.

Attention: a *speed* of 0 means *no* animation at all. forward/back causes the turtle to jump, and likewise left/right snap the turtle around instantly.

```pycon
>>> turtle.speed()
3
>>> turtle.speed('normal')
>>> turtle.speed()
6
>>> turtle.speed(9)
>>> turtle.speed()
9

```

[Subject index](INDEX.md) · [Previous](turtle-clearstamp-to-turtle-undo.md) · [Continue](turtle-position-to-turtle-heading.md) · [Owning module, declaration or section: Turtle motion](turtle-forward-to-turtle-lt.md)
