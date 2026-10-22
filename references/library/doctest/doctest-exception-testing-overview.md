# doctest — What About Exceptions? — Section introduction and initial examples

### What About Exceptions?

That's fine, as long as the traceback is the sole output the example yields: simply paste the traceback straight in. [1] Because tracebacks carry particulars apt to shift quickly (think exact file paths and line numbers), here is one situation where doctest goes out of its way to stay lenient about what it will accept.

Simple example:

```python
>>> [1, 2, 3].remove(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

```

That doctest passes provided [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised, carrying the `list.remove(x): x not in list` detail just as displayed.

An exception's expected output has to open with a traceback header, which may take either of these two forms, indented to line up with the example's first line:

```python
Traceback (most recent call last):
Traceback (innermost last):

```

After the traceback header comes an optional traceback stack, whose contents doctest disregards. The traceback stack is normally left out, or pasted in verbatim from an interactive session.

Following the traceback stack is the juiciest piece: the line(s) bearing the exception type and detail. Ordinarily that is a traceback's final line, though it may run over several lines when the exception carries a multi-line detail:

```python
>>> raise ValueError('multi\n    line\ndetail')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: multi
    line
detail

```

The closing three lines (which begin with [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError)) get matched against the exception's type and detail, and everything else is disregarded.

The recommended approach is to drop the traceback stack, unless including it lends real documentation value to the example. So a stronger rendering of that last example would probably be:

```python
>>> raise ValueError('multi\n    line\ndetail')
Traceback (most recent call last):
    ...
ValueError: multi
    line
detail

```

Be aware that tracebacks receive very special treatment. Specifically, in the reworked example, employing `...` has nothing to do with doctest's `ELLIPSIS` option. The ellipsis there could be dropped entirely, or swapped for three (or three hundred) commas or digits, or even an indented transcript of a Monty Python skit.

A few particulars worth reading through once, though not memorizing:

- Doctest has no way of telling whether your expected output originated in an exception traceback or in plain printing. Thus, for instance, an example anticipating `ValueError: 42 is prime` will pass regardless of whether [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) really gets raised or the example simply prints that traceback text. As a practical matter, everyday output seldom opens with a traceback header line, so this poses no real trouble.

- Each traceback stack line (when one is present) has to be indented more deeply than the example's first line, *or else* lead off with a non-alphanumeric character. The first line after the traceback header that matches the indentation and opens with an alphanumeric is read as where the exception detail begins. Naturally this behaves correctly for authentic tracebacks.

- With the `IGNORE_EXCEPTION_DETAIL` doctest option in force, everything past the leftmost colon plus any module qualification in the exception name gets disregarded.

- For certain [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError)s the interactive shell drops the traceback header line. But doctest leans on that traceback header line to tell exceptions apart from non-exceptions. So in the uncommon event that you must test a `SyntaxError` lacking the traceback header, you'll have to insert the traceback header line into your test example by hand.

- For some exceptions, Python marks where the error sits using `^` carets and tildes:

[Subject index](INDEX.md) · [Previous](what-s-the-execution-context.md) · [Continue](what-about-exceptions-code-example-1-none.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
