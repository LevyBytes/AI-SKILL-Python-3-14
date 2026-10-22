# Full grammar scope, notation and omitted parser actions

# Grammar

### 10. Full Grammar specification

What follows is the complete Python grammar, taken straight from the grammar that produces the CPython parser (refer to [Grammar/python.gram](https://github.com/python/cpython/tree/3.14/Grammar/python.gram)). This rendition leaves out the parts concerning code generation and error recovery.

The same notation as in the earlier docs applies here, and the [notation](https://docs.python.org/3.14/reference/introduction.html#notation) section explains it, apart from one added wrinkle:

- `~` (“cut”): lock in the current alternative, and should that alternative not parse, let the whole rule fail

For the most part Python relies on cuts to optimize or to sharpen error messages. In the listing that follows they frequently look pointless.

At the moment cuts are absent from parentheses, brackets, lookaheads, and the like. How they behave in such places is intentionally left unspecified.

[Subject index](INDEX.md) · [Following source section](peg-notation-parser-passes-cuts-and-starting-rules.md)
