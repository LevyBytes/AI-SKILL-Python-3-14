# Animation control

### Animation control

 turtle.no_animation()

Switch off turtle animation for a while. Whatever code sits inside the `no_animation` block goes unanimated; the drawing shows up once that code block finishes.

```pycon
>>> with screen.no_animation():
...     for dist in range(2, 400, 2):
...         fd(dist)
...         rt(90)

```

Added in version 3.14.

 turtle.delay(*delay=None*)

Parameters:

**delay** – positive integer

Assign or read the drawing *delay*, measured in milliseconds. (Roughly the gap in time between two successive canvas updates.) A larger drawing delay slows the animation down.

Optional argument:

```pycon
>>> screen.delay()
10
>>> screen.delay(5)
>>> screen.delay()
5

```

 turtle.tracer(*n=None*, *delay=None*)

Parameters:

- **n** – nonnegative integer

- **delay** – nonnegative integer

Switch turtle animation on or off and fix the delay for update drawings. When *n* is supplied, only every n-th routine screen update actually runs. (Handy for speeding up the drawing of intricate graphics.) Invoked with no arguments, it returns the value of n that is currently stored. The second argument fixes the delay value (see `delay()`).

```pycon
>>> screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

```

 turtle.update()

Carry out a TurtleScreen update. Meant for use while tracer is switched off.

Consult as well the RawTurtle/Turtle method `speed()`.

[Subject index](INDEX.md) · [Previous](turtle-screensize-to-turtle-setworldcoordinates.md) · [Continue](turtle-listen-to-turtle-onkeypress.md)
