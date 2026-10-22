# sys._getframe

sys._getframe([*depth*])

Hand back a frame object taken from the call stack. When the optional integer *depth* is supplied, hand back the frame object that many calls beneath the top of the stack. Should that go beyond the depth of the call stack, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. *depth* defaults to zero, which yields the frame sitting at the top of the call stack.

Raises an auditing event `sys._getframe` with argument `frame`.

**CPython implementation detail:** Reserve this function for internal, specialized work alone. There is no guarantee that every Python implementation provides it.

[API family](INDEX.md) · [sys context index](../INDEX.md).
