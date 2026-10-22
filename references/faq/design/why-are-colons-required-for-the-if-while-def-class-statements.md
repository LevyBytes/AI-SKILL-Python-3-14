# Why are colons required for the if/while/def/class statements?

### Why are colons required for the if/while/def/class statements?

Chiefly, the colon exists to make code more readable — a lesson carried over from the experimental ABC language. Take a look at this:

```python
if a == b
    print(a)

```

versus

```python
if a == b:
    print(a)

```

See how the second version reads a touch more smoothly. Observe, too, that a colon introduces the example in this very FAQ answer; that is ordinary English punctuation at work.

A second, smaller justification is that the colon eases life for syntax-highlighting editors: they can watch for colons as the cue that indentation should grow, sparing them a more involved parse of the source text.

[Subject index](INDEX.md)
