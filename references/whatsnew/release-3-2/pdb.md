# What's New In Python 3.2 / pdb — pdb

### pdb

Several usability refinements landed in the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) debugger module:

- `pdb.py` carries a fresh `-c` option which runs whatever commands a `.pdbrc` script file supplies.

- Within a `.pdbrc` script file you may place `continue` together with `next` commands that keep debugging going.

- A *nosigint* argument is now accepted by the [`Pdb`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb) class constructor.

- New commands: `l(list)`, `ll(long list)` and `source` for listing source code.

- Two fresh commands, `display` and `undisplay`, let you reveal or conceal an expression's value whenever that value has shifted.

- A fresh command, `interact`, launches an interactive interpreter populated with whatever global plus local names exist where execution currently sits.

- You can wipe out breakpoints by referencing their breakpoint number.

(Contributed by Georg Brandl, Antonio Cuni and Ilya Sandler.)

[Subject index](INDEX.md) · [Previous source section](sysconfig.md) · [Next source section](configparser.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
