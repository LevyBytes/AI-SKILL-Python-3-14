# sys._getframemodulename

sys._getframemodulename([*depth*])

Hand back the name of a module taken from the call stack. When the optional integer *depth* is supplied, hand back the module that many calls beneath the top of the stack. Should that go beyond the depth of the call stack, or should the module be unidentifiable, `None` comes back instead. *depth* defaults to zero, which yields the module sitting at the top of the call stack.

Raises an auditing event `sys._getframemodulename` with argument `depth`.

**CPython implementation detail:** Keep this function for internal, specialized work alone. Not every Python implementation is guaranteed to ship it.

Added in version 3.12.

[API family](INDEX.md) · [sys context index](../INDEX.md).
