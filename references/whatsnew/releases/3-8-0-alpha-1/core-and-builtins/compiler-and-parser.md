# Python 3.8.0 alpha 1 / core and builtins / compiler and parser

[bpo-34876](https://bugs.python.org/issue?@action=redirect&bpo=34876): For decorated functions and classes, the *lineno* and *col_offset* attributes on the AST now point to where the matching `def`, `async def` and `class` sit rather than to where the first decorator sits. The result is more accurate line reporting during tracing. This is the lone situation in which a child AST node's position can come before its parent AST node's position.

[bpo-33041](https://bugs.python.org/issue?@action=redirect&bpo=33041): Corrected bytecode generation for ?async for? when it has a complex target. A StopAsyncIteration raised during assignment or unpacking will now propagate rather than halting the iteration.

[bpo-33305](https://bugs.python.org/issue?@action=redirect&bpo=33305): Made the syntax error messages for invalid numerical literals clearer.

[bpo-33306](https://bugs.python.org/issue?@action=redirect&bpo=33306): Made the syntax error messages for unbalanced parentheses clearer.

[bpo-33499](https://bugs.python.org/issue?@action=redirect&bpo=33499): Introduce the [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX) environment variable along with the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `pycache_prefix` command-line option, which designate a different root directory under which module bytecode cache files get written.

[bpo-17611](https://bugs.python.org/issue?@action=redirect&bpo=17611): Streamlined the interpreter loop by relocating the block-stack unrolling logic into the compiler. The compiler now produces explicit instructions that adjust the value stack and invoke the clean-up code for [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) and [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return).

Dropped the opcodes `BREAK_LOOP`, `CONTINUE_LOOP`, `SETUP_LOOP` and `SETUP_EXCEPT`. Introduced fresh opcodes `ROT_FOUR`, `BEGIN_FINALLY` and `CALL_FINALLY` and `POP_FINALLY`. Adjusted how `END_FINALLY` and `WITH_CLEANUP_START` operate.

[bpo-31241](https://bugs.python.org/issue?@action=redirect&bpo=31241): The *lineno* and *col_offset* attributes on AST nodes for list comprehensions, generator expressions and tuples now point at the opening parenthesis or square brace. With tuples lacking parenthesis they point at the position of the first item.

[bpo-35193](https://bugs.python.org/issue?@action=redirect&bpo=35193): Repair an off by one error inside the bytecode peephole optimizer where, while stripping unreachable code, it could read bytes past the end bounds of an array. Every release of Python 3.6 and 3.7 carried this bug until now.

[bpo-33416](https://bugs.python.org/issue?@action=redirect&bpo=33416): Attach end line and end column position information onto the Python AST nodes. This constitutes a C-level backwards incompatible change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
