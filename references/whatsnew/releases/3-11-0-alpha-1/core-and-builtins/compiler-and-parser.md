# Python 3.11.0 alpha 1 / core and builtins / compiler and parser

[bpo-44878](https://bugs.python.org/issue?@action=redirect&bpo=44878): Dropped the loop from the bytecode interpreter. Because every instruction terminates with a DISPATCH macro, the loop had become unnecessary.

[bpo-43693](https://bugs.python.org/issue?@action=redirect&bpo=43693): Cell offsets are now computed relative to locals within the compiler. This lets the interpreter handle locals and cells as one array, which is marginally more efficient. The LOAD_CLOSURE opcode also becomes an alias for LOAD_FAST. Retaining LOAD_CLOSURE keeps the bytecode somewhat more readable.

[bpo-44335](https://bugs.python.org/issue?@action=redirect&bpo=44335): Corrected a regression when pinpointing incorrect characters in syntax errors. Pablo Galindo wrote the patch.

[bpo-43693](https://bugs.python.org/issue?@action=redirect&bpo=43693): The compiler, instead of the runtime, now computes the offsets of cell variables. This cuts the cost of handling cell and free variables, particularly when a variable serves as both an argument and a cell variable.

[bpo-43693](https://bugs.python.org/issue?@action=redirect&bpo=43693): A fresh opcode, MAKE_CELL, was introduced; it shifts part of the function-entry work into the compiler and the eval loop. Besides creating the necessary cell objects, this opcode turns the relevant arguments (and other locals) into cell variables when a function is entered.

[bpo-44201](https://bugs.python.org/issue?@action=redirect&bpo=44201): Avoided side effects from the REPL's check for specialized syntax errors, which had been prompting it to request extra tokens even after a syntax error was already detected. Pablo Galindo authored the patch.

[bpo-44180](https://bugs.python.org/issue?@action=redirect&bpo=44180): The parser will not surface generic syntax errors occurring at a position beyond the point it reached on its first pass. Pablo Galindo wrote the patch.

[bpo-44168](https://bugs.python.org/issue?@action=redirect&bpo=44168): Corrected the parser's error message for keyword arguments that carry invalid expressions. Pablo Galindo authored the patch.

[bpo-44143](https://bugs.python.org/issue?@action=redirect&bpo=44143): Corrected a parser crash that surfaced while raising tokenizer errors when an exception already existed. Pablo Galindo wrote the patch.

[bpo-26110](https://bugs.python.org/issue?@action=redirect&bpo=26110): Introduced the `CALL_METHOD_KW` opcode to accelerate method calls that include keyword arguments. The idea came from PyPy. One side effect: executing `CALL_METHOD` is now branchless within the evaluation loop.

[bpo-43149](https://bugs.python.org/issue?@action=redirect&bpo=43149): Adjusted the syntax error message about multiple exception types so it no longer mentions "exception groups". Pablo Galindo wrote the patch.

[bpo-43822](https://bugs.python.org/issue?@action=redirect&bpo=43822): When raising exceptions, the parser will give tokenizer errors priority over custom syntax errors. Pablo Galindo authored the patch.

[bpo-44456](https://bugs.python.org/issue?@action=redirect&bpo=44456): Better syntax error when positional and keyword patterns are mixed. Pablo Galindo authored the patch.

[bpo-44368](https://bugs.python.org/issue?@action=redirect&bpo=44368): Better syntax errors for invalid "as" targets. Pablo Galindo wrote the patch.

[bpo-44947](https://bugs.python.org/issue?@action=redirect&bpo=44947): Sharpen the syntax error reported for trailing commas within import statements. Pablo Galindo contributed the patch.

[bpo-44792](https://bugs.python.org/issue?@action=redirect&bpo=44792): Better syntax errors for if expressions. Miguel Brito wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
