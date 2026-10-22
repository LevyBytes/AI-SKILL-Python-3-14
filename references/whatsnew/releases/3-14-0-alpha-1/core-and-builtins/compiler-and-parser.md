# Python 3.14.0 alpha 1 / core and builtins / compiler and parser

[gh-122245](https://github.com/python/cpython/issues/122245): Spotting writes to `__debug__` shifts out of the compiler's codegen stage and into the symtable. As a result these errors get caught even within code optimized away ahead of codegen (for instance assertions under the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) command line option).

[gh-119666](https://github.com/python/cpython/issues/119666): Stop a compiler crash in the situation where a pair of comprehensions in class scope each reference `__class__`.

[gh-120225](https://github.com/python/cpython/issues/120225): Stop a compiler crash on an empty block sitting at the end of an exception handler.

[gh-119724](https://github.com/python/cpython/issues/119724): Rolled back the error-message improvements for `elif`/`else` statements that match no valid statement, since they made the syntax errors inside those `elif`/`else` blocks hard to pinpoint.

[gh-120722](https://github.com/python/cpython/issues/120722): Set the bytecode position correctly on return instructions located within lambdas. Jelle Zijlstra contributed the fix.

[gh-120367](https://github.com/python/cpython/issues/120367): Fix a defect where the compiler builds a redundant jump while replacing pseudo-ops. It can surface only with a synthetic AST that puts a try on the same line as the instruction right after the exception handler.

[gh-120367](https://github.com/python/cpython/issues/120367): Stop the compiler from crashing on code carrying redundant NOPs and JUMPs that emerge once exception handlers move to the end of the code.

[gh-123344](https://github.com/python/cpython/issues/123344): Introduce AST optimizations covering type parameter defaults.

[gh-124871](https://github.com/python/cpython/issues/124871): A compiler bug present in some 3.13 versions, where an assertion failed while reachability analysis ran, is fixed.

[gh-118093](https://github.com/python/cpython/issues/118093): The experimental JIT compiler is now better at remaining “on trace” when it meets highly-biased branches.

[gh-124442](https://github.com/python/cpython/issues/124442): Nondeterminism during compilation is fixed by sorting the value of [`__static_attributes__`](https://docs.python.org/3.14/reference/datamodel.html#type.__static_attributes__). kp2pml30 contributed the patch.

[gh-123958](https://github.com/python/cpython/issues/123958): At optimization level 2, docstrings are now dropped from the optimized AST.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
