# 4.10. Intermezzo: Coding Style

### 4.10. Intermezzo: Coding Style

With longer and trickier Python programs now within reach, this is a fitting moment to discuss *coding style*. Nearly every language admits several styles of writing (or, put more briefly, *formatting*), and some read better than the rest. Keeping your code easy for others to follow is always worthwhile, and a tidy coding style does an enormous amount toward that end.

In the Python world, [**PEP 8**](https://peps.python.org/pep-0008/) has become the style guide that the bulk of projects follow; it encourages a highly readable and pleasant-looking coding style. At some stage every Python programmer ought to read it; the key takeaways are pulled out for you here:

- Indent with 4 spaces and steer clear of tabs.

A 4-space indent strikes a sensible balance: tighter indentation buys you deeper nesting, while wider indentation reads more easily. Tabs only breed confusion and are best avoided.

- Break lines so none of them go past 79 characters.

Doing so assists anyone on a small screen and lets you line up multiple code files alongside each other on bigger ones.

- Separate your functions and classes with blank lines, and do the same around sizable blocks of code within functions.

- Wherever you can, give comments a line to themselves.

- Make a habit of writing docstrings.

- Place spaces on either side of operators and following commas, yet not immediately within bracketing constructs: `a = f(1, 2) + g(3, 4)`.

- Keep your class and function naming uniform; by convention classes take `UpperCamelCase` while functions and methods take `lowercase_with_underscores`. For a method's first argument, invariably name it `self` (see [A First Look at Classes](https://docs.python.org/3.14/tutorial/classes.html#tut-firstclasses) for further coverage of classes and methods).

- Steer away from exotic encodings when your code is destined for international use. In every situation Python's default of UTF-8, or even plain ASCII, serves you best.

- In the same vein, keep non-ASCII characters out of identifiers whenever there is even a faint possibility that speakers of another language might read or maintain your code.

Footnotes

[Subject index](INDEX.md) · [Previous source section](function-annotations.md)
