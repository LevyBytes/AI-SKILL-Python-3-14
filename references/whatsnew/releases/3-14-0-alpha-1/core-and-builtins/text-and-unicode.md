# Python 3.14.0 alpha 1 / core and builtins / text and unicode

[gh-122026](https://github.com/python/cpython/issues/122026): Repair a defect that left the tokenizer unable to spot mismatched parentheses within f-strings in certain situations. Pablo Galindo authored this.

[gh-122300](https://github.com/python/cpython/issues/122300): Keep the AST nodes for an f-string whose format specifiers hold a single element. Pablo Galindo authored this.

[gh-119879](https://github.com/python/cpython/issues/119879): String search now runs a bit quicker in some cases. It now applies the last character gap (good suffix rule) for two-way periodic needles.

[gh-119310](https://github.com/python/cpython/issues/119310): The new interactive shell can now read history files, written via the editline library, that use unicode-escaped entries. aorcajo and Łukasz Langa supplied the patch.

[gh-123229](https://github.com/python/cpython/issues/123229): Quiet a valgrind warning by zero-initializing the tokenizer's f-string buffers. Pablo Galindo authored this.

[gh-121609](https://github.com/python/cpython/issues/121609): Repair the pasting of characters that contain unicode character joiners within the new REPL. Marta Gomez Macias authored this.

[gh-116510](https://github.com/python/cpython/issues/116510): A crash brought on by immortal interned strings being shared across sub-interpreters that rely on basic single-phase init is fixed. Under that setup, a string could be used by an interpreter that lives longer than the one which created and interned it. For interpreters that share obmalloc state, the interned dict is now shared with the main interpreter as well.

[gh-124188](https://github.com/python/cpython/issues/124188): For syntax errors raised by the compiler, reading and decoding a line from a source file in a non-UTF-8 encoding is fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
