# dis — Command-line interface

### Command-line interface

From the command line, the `dis` module is runnable as a script:

```sh
python -m dis [-h] [-C] [-O] [-P] [-S] [infile]

```

These are the options the script accepts:

 -h, --help

Display usage and exit.

 -C, --show-caches

Show inline caches.

Added in version 3.13.

 -O, --show-offsets

Show offsets of instructions.

Added in version 3.13.

 -P, --show-positions

Show positions of instructions in the source code.

Added in version 3.14.

 -S, --specialized

Show specialized bytecode.

Added in version 3.14.

When `infile` is given, its disassembled code goes to stdout. If it is not, the disassembly runs against compiled source code that arrives on stdin.

[Subject index](INDEX.md) · [Previous](dis-disassembler-for-python-bytecode.md) · [Continue](dis-bytecode-class.md) · [Owning module, declaration or section: dis](dis-disassembler-for-python-bytecode.md)
