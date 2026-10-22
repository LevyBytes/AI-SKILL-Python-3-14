# What's New In Python 3.11 / Replaced opcodes

### Replaced opcodes

| Replaced Opcode(s) | New Opcode(s) | Notes |
| --- | --- | --- |
| `BINARY_*` `INPLACE_*` | `BINARY_OP` | Folded every numeric binary/in-place opcode into one opcode |
| `CALL_FUNCTION` `CALL_FUNCTION_KW` `CALL_METHOD` | `CALL` `KW_NAMES` `PRECALL` `PUSH_NULL` | Splits method argument shifting apart from keyword-argument handling; enables stronger specialization of calls |
| `DUP_TOP` `DUP_TOP_TWO` `ROT_TWO` `ROT_THREE` `ROT_FOUR` `ROT_N` | `COPY` `SWAP` | Instructions that manipulate the stack |
| `JUMP_IF_NOT_EXC_MATCH` | `CHECK_EXC_MATCH` | Runs the check yet no longer jumps |
| `JUMP_ABSOLUTE` `POP_JUMP_IF_FALSE` `POP_JUMP_IF_TRUE` | `JUMP_BACKWARD` `POP_JUMP_BACKWARD_IF_*` `POP_JUMP_FORWARD_IF_*` | Consult [3]; each direction gets `TRUE`, `FALSE`, `NONE` and `NOT_NONE` variants |
| `SETUP_WITH` `SETUP_ASYNC_WITH` | `BEFORE_WITH` | Setup for a `with` block |

[Subject index](INDEX.md) · [Previous source section](new-opcodes.md) · [Next source section](changed-removed-opcodes.md) · [Release/subject declaration](summary-release-highlights.md)
