# dis - MATCH_CLASS bytecode instruction

Here `STACK[-1]` holds a tuple naming the keyword attributes, `STACK[-2]` names the class used for the comparison, and `STACK[-3]` carries the subject being matched. The *count* value records how many positional sub-patterns there are.

Discard `STACK[-1]`, `STACK[-2]`, and `STACK[-3]` from the stack. When `STACK[-3]` qualifies as an instance of `STACK[-2]` and supplies the positional plus keyword attributes demanded by *count* together with `STACK[-1]`, a tuple holding the pulled-out attributes is pushed. If not, `None` goes on instead.

Added in version 3.10.

Changed in version 3.11: Earlier releases also left a boolean on the stack to signal whether the match worked (`True`) or did not (`False`).

[Subject index](INDEX.md) · [Continue](dis-positions-resume-to-dis-positions-send.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md) · [Owning module, declaration or section: MATCH_CLASS bytecode instruction](dis-positions-convert-value-to-dis-positions-match-class.md) · [Preceding source contract and version conditions](dis-positions-convert-value-to-dis-positions-match-class.md)
