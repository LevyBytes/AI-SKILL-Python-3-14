# turtle: `turtle.pencolor()`, `pencolor()`, `turtle.fillcolor()`

#### Color control

 turtle.pencolor()

 turtle.pencolor(*color*, */*)

 turtle.pencolor(*r*, *g*, *b*, */*)

Read back or assign the pencolor.

Four input formats are accepted:

`pencolor()`

Give back the present pencolor either as a color specification string or as a tuple (refer to the example). It can feed into a further color/pencolor/fillcolor/bgcolor call.

`pencolor(colorstring)`

Assign the pencolor to *colorstring*, a Tk color specification string like `"red"`, `"yellow"`, or `"#33cc8c"`.

`pencolor((r, g, b))`

Assign the pencolor to the RGB color held in the tuple of *r*, *g*, and *b*. Every one of *r*, *g*, and *b* has to fall within 0..colormode, where colormode equals either 1.0 or 255 (see `colormode()`).

`pencolor(r, g, b)`

Assign the pencolor to the RGB color built from *r*, *g*, and *b*. Every one of *r*, *g*, and *b* has to fall within 0..colormode.

Where the turtleshape is a polygon, that polygon's outline is drawn using the freshly assigned pencolor.

```pycon
>>> colormode()
1.0
>>> turtle.pencolor()
'red'
>>> turtle.pencolor("brown")
>>> turtle.pencolor()
'brown'
>>> tup = (0.2, 0.8, 0.55)
>>> turtle.pencolor(tup)
>>> turtle.pencolor()
(0.2, 0.8, 0.5490196078431373)
>>> colormode(255)
>>> turtle.pencolor()
(51.0, 204.0, 140.0)
>>> turtle.pencolor('#32c18f')
>>> turtle.pencolor()
(50.0, 193.0, 143.0)

```

 turtle.fillcolor()

 turtle.fillcolor(*color*, */*)

[Subject index](INDEX.md) · [Previous](turtle-isdown.md)
