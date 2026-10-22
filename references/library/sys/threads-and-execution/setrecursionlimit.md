# sys.setrecursionlimit

sys.setrecursionlimit(*limit*)

Cap the Python interpreter stack at a maximum depth of *limit*. Such a cap keeps infinite recursion from overflowing the C stack and crashing Python.

The maximum allowable limit varies by platform. A user may have to raise the limit when running a program that calls for deep recursion on a platform that permits a higher limit. This warrants caution, since a limit set too high can produce a crash.

When the new limit sits too low for the current recursion depth, a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) exception is raised.

Changed in version 3.5.1: A [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) exception is now raised when the new limit is too low for the current recursion depth.

[API family](INDEX.md) · [sys context index](../INDEX.md).
