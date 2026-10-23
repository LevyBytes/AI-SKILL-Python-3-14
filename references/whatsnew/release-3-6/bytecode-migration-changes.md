# What's New In Python 3.6 / Porting to Python 3.6 / Changes in the C API / CPython bytecode changes - dis

### CPython bytecode changes

Python 3.6 brought a number of significant revisions to the [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode).

- In place of bytecode, the Python interpreter now runs on 16-bit wordcode. (Contributed by Demur Rumed, who had input plus reviews coming from Serhiy Storchaka as well as Victor Stinner, in [bpo-26647](https://bugs.python.org/issue?@action=redirect&bpo=26647) and [bpo-28050](https://bugs.python.org/issue?@action=redirect&bpo=28050).)

- Powering the formatted string literal feature are the fresh `FORMAT_VALUE` and [`BUILD_STRING`](https://docs.python.org/3.14/library/dis.html#opcode-BUILD_STRING) opcodes. (Contributed by Eric Smith in [bpo-25483](https://bugs.python.org/issue?@action=redirect&bpo=25483) and Serhiy Storchaka in [bpo-27078](https://bugs.python.org/issue?@action=redirect&bpo=27078).)

- To streamline building dictionaries whose keys are constant, the fresh `BUILD_CONST_KEY_MAP` opcode arrived. (Contributed by Serhiy Storchaka in [bpo-27140](https://bugs.python.org/issue?@action=redirect&bpo=27140).)

- For faster performance and a cleaner implementation, the function call opcodes saw a major overhaul. The [`MAKE_FUNCTION`](https://docs.python.org/3.14/library/dis.html#opcode-MAKE_FUNCTION), `CALL_FUNCTION`, `CALL_FUNCTION_KW` and `BUILD_MAP_UNPACK_WITH_CALL` opcodes were revised, the fresh [`CALL_FUNCTION_EX`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_FUNCTION_EX) and `BUILD_TUPLE_UNPACK_WITH_CALL` arrived, while the `CALL_FUNCTION_VAR`, `CALL_FUNCTION_VAR_KW` and `MAKE_CLOSURE` opcodes were dropped. (Contributed by Demur Rumed in [bpo-27095](https://bugs.python.org/issue?@action=redirect&bpo=27095), and Serhiy Storchaka in [bpo-27213](https://bugs.python.org/issue?@action=redirect&bpo=27213), [bpo-28257](https://bugs.python.org/issue?@action=redirect&bpo=28257).)

- Backing the new [variable annotation](https://docs.python.org/3.14/glossary.html#term-variable-annotation) syntax are the fresh [`SETUP_ANNOTATIONS`](https://docs.python.org/3.14/library/dis.html#opcode-SETUP_ANNOTATIONS) and `STORE_ANNOTATION` opcodes. (Contributed by Ivan Levkivskyi in [bpo-27985](https://bugs.python.org/issue?@action=redirect&bpo=27985).)

### Notable changes in Python 3.6.2

### New `make regen-all` build target

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-6-changes-in-the-c-api.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-6.md) · [Release/subject declaration](porting-to-python-3-6-changes-in-the-c-api.md) · [Following release/subject continuation](new-make-regen-all-build-target.md)
