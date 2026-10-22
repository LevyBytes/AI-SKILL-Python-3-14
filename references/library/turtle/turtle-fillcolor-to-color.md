# turtle: `turtle.fillcolor()`, `fillcolor()`, `turtle.color()`, `color()`

turtle.fillcolor(*r*, *g*, *b*, */*)

Read or assign the fillcolor.

The call accepts four distinct argument styles:

`fillcolor()`

Hand back the present fillcolor as a color specification string, which may take tuple form (see the example). The result is suitable as an argument to a later color/pencolor/fillcolor/bgcolor call.

`fillcolor(colorstring)`

Assign fillcolor from *colorstring*, a Tk color specification string — for instance `"red"`, `"yellow"`, or `"#33cc8c"`.

`fillcolor((r, g, b))`

Assign fillcolor from the RGB color carried in the tuple of *r*, *g*, and *b*. Every one of *r*, *g*, and *b* has to fall within 0..colormode, where colormode equals either 1.0 or 255 (see `colormode()`).

`fillcolor(r, g, b)`

Assign fillcolor from the RGB color built out of *r*, *g*, and *b*. Every one of *r*, *g*, and *b* has to fall within 0..colormode.

When turtleshape is a polygon, that polygon's interior gets painted using the freshly assigned fillcolor.

```pycon
>>> turtle.fillcolor("violet")
>>> turtle.fillcolor()
'violet'
>>> turtle.pencolor()
(50.0, 193.0, 143.0)
>>> turtle.fillcolor((50, 193, 143))  # Integers, not floats
>>> turtle.fillcolor()
(50.0, 193.0, 143.0)
>>> turtle.fillcolor('#ffffff')
>>> turtle.fillcolor()
(255.0, 255.0, 255.0)

```

 turtle.color()

 turtle.color(*color*, */*)

 turtle.color(*r*, *g*, *b*, */*)

 turtle.color(*pencolor*, *fillcolor*, */*)

Read or assign both pencolor and fillcolor.

A number of argument styles work here. They take between 0 and 3 arguments, as shown:

`color()`

Hand back the present pencolor together with the present fillcolor, as a pair of color specification strings or tuples in the form yielded by `pencolor()` and `fillcolor()`.

`color(colorstring)`, `color((r,g,b))`, `color(r,g,b)`

Arguments work as in `pencolor()`; both fillcolor and pencolor are set to the supplied value.

`color(colorstring1, colorstring2)`, `color((r1,g1,b1), (r2,g2,b2))`

Same as a `pencolor(colorstring1)` followed by `fillcolor(colorstring2)`, and likewise when the alternate argument style is supplied.

When turtleshape is a polygon, the outline plus the interior of that polygon get painted using the freshly assigned colors.

```pycon
>>> turtle.color("red", "green")
>>> turtle.color()
('red', 'green')
>>> color("#285078", "#a0c8f0")
>>> color()
((40.0, 80.0, 120.0), (160.0, 200.0, 240.0))

```

See also: Screen method `colormode()`.

[Subject index](INDEX.md) · [Continue](turtle-filling-to-turtle-end-fill.md) · [Owning module, declaration or section: Color control](turtle-pencolor-to-turtle-fillcolor.md) · [Owning module, declaration or section: turtle.fillcolor; turtle.fillcolor](turtle-pencolor-to-turtle-fillcolor.md)
