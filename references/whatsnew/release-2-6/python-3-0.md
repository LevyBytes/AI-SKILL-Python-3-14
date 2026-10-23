# What’s New in Python 2.6 / Python 3.0 - functools, json, multiprocessing

### What’s New in Python 2.6

Author:

A.M. Kuchling (amk at amk.ca)

This document walks through the additions that arrived in Python 2.6, which shipped on October 1, 2008. You can find the timeline for the release in [**PEP 361**](https://peps.python.org/pep-0361/).

The overarching focus of Python 2.6 was to smooth the road toward Python 3.0, the substantial reworking of the language. Where feasible, Python 2.6 pulls in fresh syntax and capabilities from 3.0 yet keeps working with current programs by leaving the older syntax and features in place. Where that approach doesn’t fit, Python 2.6 does its best, supplying helper functions inside a `future_builtins` module along with a `-3` flag that flags constructs slated to disappear in 3.0.

A few notable new packages have joined the standard library, including the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) and [`json`](https://docs.python.org/3.14/library/json.html#module-json) modules, although the bulk of the new functionality ties back to Python 3.0 one way or another.

Throughout the codebase, Python 2.6 also brings numerous refinements and corrected defects. Counting entries in the change logs turns up 259 patches that landed and 612 bugs that were closed across the span from Python 2.5 to 2.6. Each of those totals probably runs low.

Rather than laying out a thorough specification of everything new, this document aims to give you a handy summary. The Python 2.6 documentation is where you should go for the complete picture. To dig into the reasoning behind a feature’s design and how it was built, consult the PEP that covers it. Where it can, “What’s New in Python” points to the bug/patch entry tied to each modification.

### Python 3.0

Releases of Python 2.6 and 3.0 marched in lockstep during development, so the alpha and beta builds for each appeared on matching dates. Work on 3.0 shaped a good deal of what landed in 2.6.

Python 3.0 represents a sweeping reworking of Python that abandons compatibility with the 2.x line. As a result, code you already have will require some adjustment before it can execute under Python 3.0. That said, not every alteration in 3.0 is guaranteed to break compatibility. Where new capabilities pose no risk of breaking older programs, they were brought back into 2.6 and appear throughout this document wherever they fit. Among the features carried over from 3.0 are:

- A `__complex__()` method for converting objects to a complex number.

- Alternate syntax for catching exceptions: `except TypeError as exc`.

- The addition of [`functools.reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) as a synonym for the built-in `reduce()` function.

Several brand-new built-in functions arrive with Python 3.0, and a handful of the existing builtins gain altered behavior. The 3.0 newcomers like [`bin()`](https://docs.python.org/3.14/library/functions.html#bin) were just dropped into Python 2.6 directly, while the current builtins were left untouched; in their place, the `future_builtins` module carries variants that follow the new 3.0 behavior. Programs that want to line up with 3.0 can issue `from future_builtins import hex, map` wherever they need to.

A fresh command-line flag, `-3`, switches on warnings for the features bound for removal in Python 3.0. Running your program under this flag shows you roughly how big a job porting it to 3.0 will be. Python code can read the flag’s state through the boolean variable `sys.py3kwarning`, while C extension code accesses it via `Py_Py3kWarningFlag`.

See also

The 3*xxx* family of PEPs, which holds the proposals for Python 3.0. [**PEP 3000**](https://peps.python.org/pep-3000/) lays out the development process behind Python 3.0. Begin with [**PEP 3100**](https://peps.python.org/pep-3100/), which covers the broad aims for Python 3.0, and from there read the higher-numbered PEPs that put forward individual features.

[Subject index](INDEX.md) · [Next source section](changes-to-the-development-process.md)
