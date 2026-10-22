# What's New In Python 3.11 / Faster Runtime / Inlined Python function calls — sys

> (Contributed by Mark Shannon in [bpo-44590](https://bugs.python.org/issue?@action=redirect&bpo=44590).)

#### Inlined Python function calls

Each Python function call has Python invoke an evaluating C function to interpret the code of that function. The practical effect is that pure Python recursion is bounded by whatever the C stack can safely handle.

Within 3.11, the moment CPython notices Python code invoking some other Python function, it builds a fresh frame and "jumps" straight into the new code inside that frame. The C interpreting function is thereby skipped entirely.

The majority of Python function calls now use up no C stack space, which speeds them along. With plain recursive functions such as fibonacci or factorial, we saw a 1.7x speedup. It also lets recursive functions descend much further (provided the user raises the recursion limit through [`sys.setrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.setrecursionlimit)). Our pyperformance figures showed a 1-3% improvement.

[Subject index](INDEX.md) · [Previous source section](faster-runtime-cheaper-lazy-python-frames.md) · [Next source section](faster-runtime-pep-659-specializing-adaptive-interpreter.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](faster-runtime-cheaper-lazy-python-frames.md)
