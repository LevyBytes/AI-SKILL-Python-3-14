# What’s New In Python 3.12 / tkinter

### tkinter

- Arguments handed to `tkinter.Canvas.coords()` are now flattened. Coordinates may still arrive as standalone arguments (`x1, y1, x2, y2, ...`) or bundled into one sequence (`[x1, y1, x2, y2, ...]`), yet pair-grouped forms (`(x1, y1), (x2, y2), ...` and `[(x1, y1), (x2, y2), ...]`) are accepted too, mirroring the `create_*()` methods. (Contributed by Serhiy Storchaka in [gh-94473](https://github.com/python/cpython/issues/94473).)

[Subject index](INDEX.md) · [Previous source section](threading.md) · [Next source section](tokenize.md) · [Release/subject declaration](summary-release-highlights.md)
