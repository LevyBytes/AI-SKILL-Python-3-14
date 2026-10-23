# What's New in Python 2.5 / PEP 308: Conditional Expressions - ctypes

### What's New in Python 2.5

Author:

A.M. Kuchling

The features introduced with Python 2.5 are covered in this document. Python 2.5 was originally targeted for a final release in August 2006, with the projected schedule laid out in [**PEP 356**](https://peps.python.org/pep-0356/); the actual release landed on September 19, 2006.

Python 2.5 blends together both language refinements and library upgrades in a noteworthy way. To my mind, the library work carries more weight for Python's userbase, since a handful of broadly handy packages joined the standard distribution. Among the fresh modules are ElementTree, which handles XML (`xml.etree`), the SQLite-backed database module (`sqlite`), and the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module that lets you invoke C functions.

On the language side the changes carry moderate weight. A number of agreeable additions appeared, though most of them won't be things you reach for daily. After much delay, conditional expressions joined the language with a fresh syntax; consult the PEP 308: Conditional Expressions section. Writing teardown code grows simpler thanks to the new ?[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)? statement (see PEP 343: The ?with? statement). Generators can now receive values pushed into them (see PEP 342: New Generator Features). Imports may be declared explicitly as absolute or relative (see PEP 328: Absolute and Relative Imports). A handful of awkward exception-handling edge cases now behave better (see PEP 341: Unified try/except/finally). Each of these is a genuine gain, yet each touches a single language feature in isolation; none of them sweep across Python's overall semantics.

Beyond the language and library work, additional refinements and fixes were spread across the entire codebase. Scanning the SVN change logs turns up 353 patches that were applied along with 458 bugs that were resolved between Python 2.4 and 2.5. (It's probable that both numbers undercount the real total.)

Rather than serving as an exhaustive specification of everything new, this document gives each change a quick introduction backed by useful examples. When you need the whole story, always consult the Python 2.5 documentation hosted at [https://docs.python.org](https://docs.python.org). And to dig into the full implementation along with the reasoning behind a design, turn to the PEP covering that particular new feature.

I welcome comments, suggestions, and reports of mistakes about this document; kindly e-mail them to the author or file a bug in the Python bug tracker.

### PEP 308: Conditional Expressions

People had asked for ages for a means of writing conditional expressions ? expressions that yield value A or value B according to whether some Boolean is true or false. With a conditional expression you can collapse into one assignment statement something that does the same job as this:

```python
if condition:
    x = true_value
else:
    x = false_value

```

Both python-dev and comp.lang.python hosted countless wearisome debates over the syntax. There was even a vote, which revealed that most participants wanted conditional expressions in one shape or another, yet no single syntax won a clear majority. Among the contenders were C's `cond ? true_v : false_v`, `if cond then true_v else false_v`, plus 16 further variants.

In the end Guido van Rossum settled on an unexpected syntax:

```python
x = true_value if condition else false_value

```

Just like the Boolean expressions already in the language, evaluation stays lazy, which makes the order of evaluation hop around somewhat. First to run is the *condition* expression sitting in the middle, and the *true_value* expression runs only when that condition turned out true. In the same way, the *false_value* expression runs only in the case where the condition is false.

The syntax can feel odd and inverted at first ? why should the condition sit in the *middle* of the expression instead of up front the way it does in C's `c ? x : y`? To validate the choice, the new syntax was applied across the standard library's modules to observe how the resulting code looked. Frequently, wherever a conditional expression appears, one value reads like the ?common case? while the other is an ?exceptional case? that surfaces only on the rarer occasions when the condition fails. This pattern shows through a little more plainly with the conditional syntax:

```python
contents = ((doc + '\n') if doc else '')

```

I parse the statement above as saying ?here *contents* normally takes on the value `doc+'\n'`; on occasion *doc* is empty, and in that particular situation an empty string comes back.? I suspect I won't reach for conditional expressions much in places lacking an obvious common and uncommon case.

Whether the language ought to insist on wrapping conditional expressions in parentheses got some discussion. The grammar of the Python language was ultimately set to *not* demand parentheses, but on stylistic grounds I'd argue you should add them every time. Look at these two statements:

```python
# First version -- no parens
level = 1 if logging else 0

# Second version -- with parens
level = (1 if logging else 0)

```

With the first version, I suspect a reader's gaze might split the line into ?level = 1?, ?if logging?, ?else 0?, leaving the impression that the condition governs whether *level* gets assigned at all. The second version, to my eye, reads more cleanly, since it signals that the assignment always happens and that the selection is between two values.

One more argument for the brackets: a couple of strange mixtures of list comprehensions and lambdas might resemble malformed conditional expressions. [**PEP 308**](https://peps.python.org/pep-0308/) offers a few such examples. Wrapping your conditional expressions in parentheses keeps you clear of that situation.

See also

[**PEP 308**](https://peps.python.org/pep-0308/) - Conditional Expressions

PEP authored by Guido van Rossum together with Raymond D. Hettinger; the implementation came from Thomas Wouters.

[Subject index](INDEX.md) · [Next source section](pep-309-partial-function-application.md)
