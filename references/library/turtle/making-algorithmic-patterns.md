# Making algorithmic patterns

### Making algorithmic patterns

With loops at your disposal, you can assemble geometric patterns:

```python
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

```

- bounded, naturally, by nothing more than your own imagination!

Now let's render the star shape shown near the top of this page. The plan calls for red outlines with a yellow fill:

```python
color('red')
fillcolor('yellow')

```

In the same way that `up()` and `down()` govern whether lines appear, the fill feature can likewise be switched on and off:

```python
begin_fill()

```

After that we set up a loop:

```python
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

```

`abs(pos()) < 1` serves nicely as a test for whether the turtle has returned to where home sits.

To wrap up, finish off the fill:

```python
end_fill()

```

(Keep in mind that the actual fill is only rendered once the `end_fill()` command runs.)

[Subject index](INDEX.md) · [Previous](the-turtle-s-position.md) · [Continue](how-to.md)
