# Compound shapes

### Compound shapes

For compound turtle shapes — those made up of several polygons in differing colors — you have to invoke the helper class `Shape` directly, in the way laid out below:

1.

Build an empty Shape object whose type is “compound”.

2.

Attach however many components you want to that object, by way of the `addcomponent()` method.

For example:

```pycon
>>> s = Shape("compound")
>>> poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
>>> s.addcomponent(poly1, "red", "blue")
>>> poly2 = ((0,0),(10,-5),(-10,-5))
>>> s.addcomponent(poly2, "blue", "red")

```

3.

At this point attach the Shape to the Screen's shapelist and put it to use:

```pycon
>>> register_shape("myshape", s)
>>> shape("myshape")

```

Note

Internally the `register_shape()` method makes use of the `Shape` class in various ways. The application programmer needs to touch the Shape class *only* when working with compound shapes as demonstrated above!

[Subject index](INDEX.md) · [Previous](turtle-setundobuffer-to-turtle-undobufferentries.md) · [Continue](methods-of-turtlescreen-screen-and-corresponding-functions.md)
