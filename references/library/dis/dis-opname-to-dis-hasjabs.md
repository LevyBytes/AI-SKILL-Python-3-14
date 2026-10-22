# dis — Opcode collections

### Opcode collections

To support automatic introspection of bytecode instructions, these collections exist:

Changed in version 3.12: Pseudo instructions plus instrumented instructions are now included in the collections too. Such opcodes carry values `>= MIN_PSEUDO_OPCODE` and `>= MIN_INSTRUMENTED_OPCODE`.

 dis.opname

A sequence of operation names that you index with the bytecode.

 dis.opmap

A dictionary that maps each operation name onto its bytecode.

 dis.cmp_op

A sequence containing every compare operation name.

 dis.hasarg

A sequence of the bytecodes that make use of their argument.

Added in version 3.12.

 dis.hasconst

A sequence of the bytecodes that read a constant.

 dis.hasfree

A sequence of the bytecodes that reach a [free (closure) variable](https://docs.python.org/3.14/glossary.html#term-closure-variable). Here ‘free’ covers two cases: names defined in this scope but used by nested scopes, and names from enclosing scopes that this scope reads. Names belonging to the global or builtin scopes are *not* counted.

 dis.hasname

A sequence of the bytecodes that reach an attribute through its name.

 dis.hasjump

A sequence of the bytecodes carrying a jump target. Every jump is relative.

Added in version 3.13.

 dis.haslocal

A sequence of the bytecodes that reach a local variable.

 dis.hascompare

A sequence of the bytecodes for Boolean operations.

 dis.hasexc

A sequence of the bytecodes that install an exception handler.

Added in version 3.12.

 dis.hasjrel

A sequence of the bytecodes carrying a relative jump target.

Deprecated since version 3.13: All jumps are now relative. Use `hasjump`.

 dis.hasjabs

A sequence of the bytecodes carrying an absolute jump target.

Deprecated since version 3.13: Since every jump is relative these days, nothing populates this list.

[Subject index](INDEX.md) · [Previous](dis-positions-setup-finally-to-dis-positions-load-closure.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md)
