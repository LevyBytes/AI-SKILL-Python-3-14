# Python 3.12.0 alpha 1 / core and builtins / compiler and parser

[gh-94438](https://github.com/python/cpython/issues/94438): Repair a problem that left extended opcode arguments and certain conditional pops out of the calculation of valid jump targets for assignments to a frame object's `f_lineno` attribute. In certain cases this produced inconsistent internal state and a hard interpreter crash.

[gh-91409](https://github.com/python/cpython/issues/91409): Repair the incorrect source location info that certain optimizations in the bytecode compiler introduced.

[gh-93554](https://github.com/python/cpython/issues/93554): Rework the jump opcodes such that every conditional jump becomes a forward jump. The assembler rewrites backward jumps into a conditional forward jump whose target is the fallthrough block (with the condition flipped), trailed by an unconditional backward jump. As an example:

`POP_JUMP_IF_TRUE BACKWARD_TARGET` becomes `POP_JUMP_IF_FALSE NEXT_BLOCK; JUMP BACKWARD_TARGET`.

Every directed conditional jump opcode was dropped: `POP_JUMP_FORWARD_IF_TRUE`, `POP_JUMP_BACKWARD_IF_TRUE`, `POP_JUMP_FORWARD_IF_FALSE`, `POP_JUMP_BACKWARD_IF_FALSE`, `POP_JUMP_FORWARD_IF_NONE`, `POP_JUMP_BACKWARD_IF_NONE`, `POP_JUMP_FORWARD_IF_NOT_NONE`, `POP_JUMP_BACKWARD_IF_NOT_NONE`.

Their direction-free counterparts are no longer pseudo-instructions, and those are what now carry out the forward conditional jumps.

[gh-92619](https://github.com/python/cpython/issues/92619): Has the compiler duplicate an exit block solely when none of its instructions carry a lineno (formerly only the block's first instruction was inspected, which produced needlessly duplicated blocks).

[gh-96848](https://github.com/python/cpython/issues/96848): Repair command line parsing: the [`-X int_max_str_digits`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option given with no value (invalid) is now rejected even when the [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS) environment variable already holds a valid limit. Victor Stinner wrote the patch.

[gh-93621](https://github.com/python/cpython/issues/93621): Reorders the bytecode instructions produced for [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) and [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) so the exception table holds fewer entries.

[gh-93444](https://github.com/python/cpython/issues/93444): Dropped surplus fields from the compiler's basicblock struct: `b_nofallthrough`, `b_exit`, `b_return`. Each is readily derived from the opcode of the block's last instruction.

[gh-93356](https://github.com/python/cpython/issues/93356): Bytecode for exception handlers is now placed at the tail of the code unit's bytecode. That removes one jump in the case where no exception fires.

[gh-93223](https://github.com/python/cpython/issues/93223): Whenever one bytecode instruction jumps to an unconditional jump, the first can frequently be rewritten to aim straight at the unconditional jump's destination. Owing to tracing, this previously happened only where both instructions shared a line number. It now also happens when the unconditional jump is artificial — that is, carries no line number of its own.

[gh-93678](https://github.com/python/cpython/issues/93678): A test harness was added for direct unit testing of the compiler's optimization stage. The `_testinternalcapi.optimize_cfg()` function drives the optimiser across a sequence of instructions. Inside `test.support`, the `CfgOptimizationTestCase` class offers utilities for running the optimizer and inspecting the output.

[gh-95922](https://github.com/python/cpython/issues/95922): Repair a bug in which the compiler's `eliminate_empty_basic_blocks` function passed over the final block of the code unit.

[gh-95150](https://github.com/python/cpython/issues/95150): Update how code objects hash and compare so that every debugging and exception handling table is taken into account. This addresses a case where certain non-identical code objects might get "deduplicated" during compilation.

[gh-87092](https://github.com/python/cpython/issues/87092): Build a "jump target label" abstraction into the compiler so its codegen stage no longer operates directly on basic blocks. This sets the stage for changes to the underlying CFG generation mechanism.

[gh-93678](https://github.com/python/cpython/issues/93678): Introduce a cfg_builder struct and rework the surrounding code so a cfg can be assembled without any instance of the compiler struct.

[gh-90997](https://github.com/python/cpython/issues/90997): Speed up reading and writing of inline bytecode caches on certain platforms.

[gh-96751](https://github.com/python/cpython/issues/96751): Strip dead code out of the `CALL_FUNCTION_EX` opcode.

[gh-98461](https://github.com/python/cpython/issues/98461): Correct the bytecode source location for list, set and dict comprehensions, and likewise for generator expressions.

[gh-97997](https://github.com/python/cpython/issues/97997): A running column offset was added to the tokenizer state, sparing the AST column information from being derived via pointer arithmetic.

[gh-97973](https://github.com/python/cpython/issues/97973): The tokenizer was changed to hand back every piece of information the parser requires for placing location data on the AST nodes, freeing the parser from computing it through pointer arithmetic.

[gh-93678](https://github.com/python/cpython/issues/93678): Reworks the compiler optimisation code so `struct assembler` and `struct compiler` no longer need to be threaded through. Each function instead receives the CFG plus whatever data it genuinely requires. That opens the door to testing this code directly.

[gh-93678](https://github.com/python/cpython/issues/93678): Reworks the compiler to cut down on boilerplate and repetition.

[gh-94893](https://github.com/python/cpython/issues/94893): Resolves a case where manipulating frame objects could corrupt inline bytecode caches.

[gh-94694](https://github.com/python/cpython/issues/94694): Resolves a case that could leave multi-line method lookups carrying misleading or wrong column offset data. Occasionally (while compiling a hand-built AST) this had the potential to trigger a hard interpreter crash.

[gh-92228](https://github.com/python/cpython/issues/92228): Turns off the compiler's inline-small-exit-blocks optimization on exit blocks tied to source code lines. This corrects a bug that prevents the debugger from distinguishing where an exception handler stops and the following code block starts.

[gh-91719](https://github.com/python/cpython/issues/91719): Reloads `opcode` whenever the interpreter main loop raises `unknown opcode error`, letting C compilers emit dispatching code on their own.

[gh-94329](https://github.com/python/cpython/issues/94329): Compiles and executes code that unpacks very large sequences (thousands of elements). Such code used to fail compilation. It now both compiles and runs as expected.

[gh-92858](https://github.com/python/cpython/issues/92858): Sharpens the error message for certain suites carrying a syntax error ahead of ":"

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
