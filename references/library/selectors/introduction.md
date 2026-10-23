# selectors - Introduction

### Introduction

Resting on top of the primitives from the [`select`](https://docs.python.org/3.14/library/select.html#module-select) module, this module delivers efficient I/O multiplexing at a higher level. Unless you genuinely need fine-grained command over the underlying OS-level primitives, reaching for this module instead is the recommended path.

What it supplies is the `BaseSelector` abstract base class, paired with a handful of concrete builds (`KqueueSelector`, `EpollSelector`…), letting you await I/O readiness signals across several file objects at once. Throughout the text that follows, the phrase “file object” covers any object carrying a [`fileno()`](https://docs.python.org/3.14/library/io.html#io.IOBase.fileno) method, or alternatively a bare file descriptor. See [file object](https://docs.python.org/3.14/glossary.html#term-file-object).

`DefaultSelector` stands as an alias pointing at whichever build runs most efficiently on the platform in use; for the majority of people this is what they ought to pick by default.

Note

Exactly which kinds of file objects work varies by platform: under Windows you get sockets but no pipes, while under Unix the two alike are handled (and a handful of further kinds, fifos or special file devices among them, can work too).

See also

[`select`](https://docs.python.org/3.14/library/select.html#module-select)

Low-level I/O multiplexing module.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module either fails to function or is absent altogether. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) to read more.

[Subject index](INDEX.md) · [Previous](selectors-high-level-i-o-multiplexing.md) · [Continue](selectors-selectorkey-class.md) · [Owning module, declaration or section: selectors](selectors-high-level-i-o-multiplexing.md)
