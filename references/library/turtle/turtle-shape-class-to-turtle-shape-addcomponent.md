# turtle: `turtle.Shape`, `addcomponent()`

*class *turtle.Shape(*type_*, *data*)

Parameters:

**type_** – one of the strings “polygon”, “image”, “compound”

A data structure that models shapes. The pair `(type_, data)` is required to conform to this specification:

| *type_* | *data* |
| --- | --- |
| “polygon” | a polygon-tuple, i.e. a tuple of pairs of coordinates |
| “image” | an image (in this form only used internally!) |
| “compound” | `None` (a compound shape has to be constructed using the `addcomponent()` method) |

 addcomponent(*poly*, *fill*, *outline=None*)

Parameters:

- **poly** – a polygon, i.e. a tuple of pairs of numbers

- **fill** – a color the *poly* will be filled with

- **outline** – a color for the poly’s outline (if given)

Example:

```pycon
>>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
>>> s = Shape("compound")
>>> s.addcomponent(poly, "red", "blue")
>>> # ... add more components and then use register_shape()

```

See Compound shapes.

[Subject index](INDEX.md) · [Previous](turtle-scrolledcanvas-class.md) · [Continue](turtle-vec2d-class.md) · [Owning module, declaration or section: Public classes](turtle-rawturtle-class-to-turtle-rawpen-class.md)
