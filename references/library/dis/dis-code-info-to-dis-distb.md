# dis: `dis.code_info()`, `dis.show_code()`, `dis.dis()`, `dis.distb()`

### Analysis functions

The `dis` module additionally provides the analysis functions listed here, each turning the input straight into the output you want. When you only need to run one operation, they come in handy, since the intermediate analysis object adds nothing useful:

 dis.code_info(*x*)

Hand back a formatted multi-line string holding thorough code object details for the given function, generator, asynchronous generator, coroutine, method, source code string or code object.

Be aware that the precise makeup of code info strings depends heavily on the implementation, and that it can shift unpredictably from one Python VM or Python release to another.

Added in version 3.2.

Changed in version 3.7: Coroutine and asynchronous generator objects are now handled by this.

 dis.show_code(*x*, ***, *file=None*)

Send thorough code object details for the given function, method, source code string or code object to *file* (or to `sys.stdout` when *file* goes unspecified).

Acting as a tidy shortcut for `print(code_info(x), file=file)`, this is meant for poking around interactively at the interpreter prompt.

Added in version 3.2.

Changed in version 3.4: Brought in the *file* parameter.

 dis.dis(*x=None*, ***, *file=None*, *depth=None*, *show_caches=False*, *adaptive=False*, *show_offsets=False*, *show_positions=False*)

Disassemble the *x* object. Acceptable forms for *x* include a code object, a coroutine, a function, a generator, an asynchronous generator, a method, a module, a class, plus a source code string or a raw bytecode byte sequence. With a module, every function gets disassembled. With a class, all methods get disassembled (class and static methods included). With a code object or raw bytecode sequence, a single line is printed per bytecode instruction. Nested code objects are also disassembled recursively. Things of that sort can encompass the bodies of nested classes, nested functions, generator expressions, plus the code objects backing [annotation scopes](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes). Before disassembly, strings get compiled into code objects via the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) built-in function. Should no object be supplied, this function disassembles the most recent traceback.

Text from the disassembly goes to the *file* argument you pass when one is given, and otherwise to `sys.stdout`.

Recursion's greatest depth is capped by *depth* except when that is `None`. A value of `depth=0` denotes no recursion.

When *show_caches* is `True`, this function renders the inline cache entries the interpreter relies on to specialize the bytecode.

When *adaptive* is `True`, this function renders specialized bytecode that can diverge from the original bytecode.

Changed in version 3.4: Brought in the *file* parameter.

Changed in version 3.7: Added recursive disassembling support along with the *depth* parameter.

Changed in version 3.7: Coroutine and asynchronous generator objects are now handled by this.

Changed in version 3.11: Brought in the *show_caches* together with the *adaptive* parameters.

Changed in version 3.13: Brought in the *show_offsets* parameter.

Changed in version 3.14: Brought in the *show_positions* parameter.

 dis.distb(*tb=None*, ***, *file=None*, *show_caches=False*, *adaptive=False*, *show_offset=False*, *show_positions=False*)

Disassemble a traceback's top-of-stack function, falling back to the most recent traceback when none is given. The instruction that caused the exception is flagged.

Text from the disassembly goes to the *file* argument you pass when one is given, and otherwise to `sys.stdout`.

Changed in version 3.4: Brought in the *file* parameter.

Changed in version 3.11: Brought in the *show_caches* together with the *adaptive* parameters.

Changed in version 3.13: Brought in the *show_offsets* parameter.

Changed in version 3.14: Brought in the *show_positions* parameter.

[Subject index](INDEX.md) · [Previous](dis-bytecode-dis-to-dis-bytecode-info.md) · [Continue](dis-disassemble-to-dis-findlabels.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md)
