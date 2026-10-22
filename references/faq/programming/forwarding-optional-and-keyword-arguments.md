# How can I pass optional or keyword parameters from one function to another?

### How can I pass optional or keyword parameters from one function to another?

Gather the arguments by using the `*` and `**` specifiers within the function's parameter list; this delivers the positional ones to you in tuple form and the keyword ones in dictionary form. From there you can forward those arguments into another function call with `*` and `**`:

```python
def f(x, *args, **kwargs):
    ...
    kwargs['width'] = '14.3c'
    ...
    g(x, *args, **kwargs)

```

[Subject index](INDEX.md)
