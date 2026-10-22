# 4.9.7. Documentation Strings

### 4.9.7. Documentation Strings

Below are a handful of conventions covering what documentation strings contain and how they are laid out.

Make the opening line a brief, tight summary of what the object is for. To keep it short, skip naming the object or its type outright, because those facts come from elsewhere (unless the name itself is a verb that describes what the function does). Begin that line with a capital letter and finish it with a period.

Whenever the docstring runs longer, leave the second line empty so the summary stands apart from the remainder of the text. After that, write one or more paragraphs laying out how the object is called, what side effects it has, and so on.

When a multi-line string literal acts as a module, class, or function docstring, Python's parser removes its indentation.

What follows is a sample of a docstring spanning several lines:

```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything:
...
...         >>> my_function()
...         >>>
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

No, really, it doesn't do anything:

    >>> my_function()
    >>>

```

[Subject index](INDEX.md) · [Previous source section](lambda-expressions.md) · [Following source section](function-annotations.md)
