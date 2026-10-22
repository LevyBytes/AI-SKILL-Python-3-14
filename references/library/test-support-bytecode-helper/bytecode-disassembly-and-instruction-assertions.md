# test.support.bytecode_helper: `BytecodeTestCase.get_disassembly_as_string()`, `BytecodeTestCase.assertInBytecode()`, `BytecodeTestCase.assertNotInBytecode()`

BytecodeTestCase.get_disassembly_as_string(*co*)

Returns the disassembly of *co* in string form.

 BytecodeTestCase.assertInBytecode(*x*, *opname*, *argval=_UNSPECIFIED*)

Returns instr when *opname* is present; otherwise it raises [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError).

 BytecodeTestCase.assertNotInBytecode(*x*, *opname*, *argval=_UNSPECIFIED*)

Raises [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) when *opname* is present.

[Subject index](INDEX.md) · [Previous](test-support-bytecode-helper-bytecodetestcase-class.md) · [Continue](../test-support-threading-helper/thread-test-joining-and-concurrent-execution.md) · [Owning module, declaration or section: test.support.bytecode_helper](test-support-bytecode-helper-bytecodetestcase-class.md) · [Owning module, declaration or section: test.support.bytecode_helper.BytecodeTestCase](test-support-bytecode-helper-bytecodetestcase-class.md)
