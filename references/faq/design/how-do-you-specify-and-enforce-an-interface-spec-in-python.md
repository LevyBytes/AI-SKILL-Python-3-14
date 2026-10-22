# How do you specify and enforce an interface spec in Python?

### How do you specify and enforce an interface spec in Python?

In languages like C++ and Java, a module’s interface specification spells out the prototypes of that module’s methods and functions. A common view holds that enforcing such specifications at compile time aids in putting together large programs.

Starting in Python 2.6, the [`abc`](https://docs.python.org/3.14/library/abc.html#module-abc) module lets you declare Abstract Base Classes (ABCs). From there, [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) let you verify whether a given object or class satisfies a specific ABC. Ready-made ABCs live in the [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) module, among them [`Iterable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Iterable), [`Container`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Container), and [`MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping).

In the Python world, a sound testing regimen applied to each component recovers much of what interface specifications would have given you.

A solid test suite for a module does triple duty: it catches regressions, it documents the module’s interface, and it offers a batch of examples. Plenty of Python modules can be invoked as a script to run a basic “self test.” Even those that talk to elaborate external interfaces can frequently be exercised on their own by swapping in throwaway “stub” stand-ins for that interface. Whether you lean on the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) and [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) modules or on third-party test frameworks, you can assemble thorough test suites that touch every line of a module’s code.

A disciplined approach to testing serves the construction of big, intricate Python applications every bit as well as interface specifications would — arguably better, since a specification cannot verify certain behaviors of a program. Take the [`list.append()`](https://docs.python.org/3.14/library/stdtypes.html#list.append) method, which ought to tack a new element onto the end of some internal list: a specification has no way to confirm that your `list.append()` implementation truly behaves that way, whereas confirming it inside a test suite is trivial.

Building test suites pays off handsomely, so it is worth shaping your code to be readily testable. A method that keeps gaining traction, test-driven development, has you author pieces of the test suite up front, ahead of the real code itself. Naturally, Python will also happily let you be careless and skip writing any tests whatsoever.

[Subject index](INDEX.md)
