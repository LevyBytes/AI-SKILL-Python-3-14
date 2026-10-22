# Can't you emulate threads in the interpreter instead of relying on an OS-specific thread implementation?

### Can't you emulate threads in the interpreter instead of relying on an OS-specific thread implementation?

Answer 1: Sadly, the interpreter pushes a minimum of one C stack frame per Python stack frame. On top of that, extensions can call back into Python at nearly any moment. A full threads implementation therefore demands thread support from C.

Answer 2: Happily, [Stackless Python](https://github.com/stackless-dev/stackless/wiki) exists, featuring a thoroughly reworked interpreter loop that sidesteps the C stack.

[Subject index](INDEX.md)
