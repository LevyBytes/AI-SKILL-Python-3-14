# What’s New In Python 3.8 / Porting to Python 3.8 / Changes in the C API / CPython bytecode changes

### CPython bytecode changes

- Pushing the logic that unrolls the block stack down into the compiler has simplified the interpreter loop. The compiler now puts out explicit instructions for tidying the value stack and running the clean-up code tied to [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) and [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return).

Gone are the opcodes `BREAK_LOOP`, `CONTINUE_LOOP`, `SETUP_LOOP` and `SETUP_EXCEPT`. Fresh opcodes `ROT_FOUR`, `BEGIN_FINALLY`, `CALL_FINALLY` and `POP_FINALLY` have been added. The behavior of `END_FINALLY` and `WITH_CLEANUP_START` has changed.

(The work here came from Mark Shannon, Antoine Pitrou and Serhiy Storchaka under [bpo-17611](https://bugs.python.org/issue?@action=redirect&bpo=17611).)

- A fresh opcode, [`END_ASYNC_FOR`](https://docs.python.org/3.14/library/dis.html#opcode-END_ASYNC_FOR), was introduced to cope with exceptions thrown while awaiting the next element within an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) loop. (The work here came from Serhiy Storchaka under [bpo-33041](https://bugs.python.org/issue?@action=redirect&bpo=33041).)

- [`MAP_ADD`](https://docs.python.org/3.14/library/dis.html#opcode-MAP_ADD) has been reworked so that it looks for the value at the top of the stack and the key just beneath it. The reason for the swap is to guarantee that, within dictionary comprehensions, the key is evaluated ahead of the value — exactly what [**PEP 572**](https://peps.python.org/pep-0572/) called for. (The work here came from Jörn Heissler under [bpo-35224](https://bugs.python.org/issue?@action=redirect&bpo=35224).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-8-changes-in-the-c-api.md) · [Release/subject declaration](assignment-expressions.md) · [Release/subject declaration](porting-to-python-3-8.md) · [Release/subject declaration](porting-to-python-3-8-changes-in-the-c-api.md) · [Next source section](porting-to-python-3-8-changes-in-the-c-api-demos-and-tools.md)
