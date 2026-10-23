# What's New In Python 3.9 / Porting to Python 3.9 / Changes in the C API / CPython bytecode changes - dis

### CPython bytecode changes

- A `LOAD_ASSERTION_ERROR` opcode was added to support the [`assert`](https://docs.python.org/3.14/reference/simple_stmts.html#assert) statement. Earlier, the assert statement misbehaved whenever the [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) exception happened to be shadowed. (Contributed by Zackery Spytz in [bpo-34880](https://bugs.python.org/issue?@action=redirect&bpo=34880).)

- The [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP) opcode was divided into four separate instructions:

  - `COMPARE_OP` for rich comparisons

  - `IS_OP` for ?is? and ?is not? tests

  - `CONTAINS_OP` for ?in? and ?not in? tests

  - `JUMP_IF_NOT_EXC_MATCH` for checking exceptions in ?try-except? statements.

(Contributed by Mark Shannon in [bpo-39156](https://bugs.python.org/issue?@action=redirect&bpo=39156).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-9-changes-in-the-c-api.md) · [Next source section](build-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-9.md) · [Release/subject declaration](porting-to-python-3-9-changes-in-the-c-api.md)
