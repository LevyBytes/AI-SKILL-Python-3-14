# pickletools - Programmatic interface

### Programmatic interface

 pickletools.dis(*pickle*, *out=None*, *memo=None*, *indentlevel=4*, *annotate=0*)

Writes a symbolic disassembly of the pickle into the file-like object *out*, which falls back to `sys.stdout`. The *pickle* may be supplied as either a string or a file-like object. You can pass a Python dictionary as *memo* to serve as the pickle's memo; doing so lets you disassemble several pickles produced by one pickler in sequence. Deeper levels, which the stream marks with `MARK` opcodes, get indented by *indentlevel* spaces apiece. When *annotate* receives a nonzero value, every opcode in the output gains a brief note, and that value acts as a hint for which column the note begins in.

Changed in version 3.2: The *annotate* parameter was introduced.

 pickletools.genops(*pickle*)

Hands you an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) across every opcode within a pickle, yielding a run of `(opcode, arg, pos)` triples. Here *opcode* is an instance of the `OpcodeInfo` class; *arg* holds the opcode argument's decoded value as a Python object; and *pos* tells you where the opcode sits. The *pickle* may be supplied as either a string or a file-like object.

 pickletools.optimize(*picklestring*)

Strips out the `PUT` opcodes that go unused and gives back a fresh, equivalent pickle string. That trimmed pickle is shorter, moves across the wire faster, occupies less storage, and unpickles with greater efficiency.

[Subject index](INDEX.md) · [Previous](command-line-options.md) · [Continue](../pipes/pipes-interface-to-shell-pipelines.md) · [Owning module, declaration or section: pickletools](pickletools-tools-for-pickle-developers.md)
