# Python 3.5.0 alpha 1 / core and builtins / compiler and parser

[bpo-21669](https://bugs.python.org/issue?@action=redirect&bpo=21669): Leaning on heuristics inside SyntaxError.__init__, the parser now tries to produce error messages that are more meaningful (or at minimum friendlier to search engines) whenever "exec" and "print" show up as statements.

[bpo-21642](https://bugs.python.org/issue?@action=redirect&bpo=21642): Inside the conditional if-else expression, treat an integer butted right up against the `else` keyword with no space (for example `True if 42else False`) as valid syntax.

[bpo-21523](https://bugs.python.org/issue?@action=redirect&bpo=21523): Corrected the compiler's overly pessimistic estimate of the stack effect for certain opcodes. That also clears a quadratic compilation time problem that showed up when compiling code carrying lots of "and" and "or" operators.

[bpo-21209](https://bugs.python.org/issue?@action=redirect&bpo=21209): Repaired the sending of tuples into custom generator objects via the yield from syntax.

[bpo-19655](https://bugs.python.org/issue?@action=redirect&bpo=19655): A rewrite landed for the ASDL parser — which the build process relies on to generate the C code that manages the Python AST. The replacement parser stands on its own and no longer drags along the spark.py parser-generator library; spark.py left the source base.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
