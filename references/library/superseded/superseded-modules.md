# sunau — Superseded Modules

## Superseded Modules

### Superseded Modules

For the bulk of tasks, the modules gathered in this chapter have been overtaken by newer ones; they linger mainly so that older code keeps working.

A module can land here because it tackles only a narrow corner of some problem while a broader answer already lives elsewhere in the standard library. Take [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt): it handles the narrow job of “mimic the C `getopt()` API in Python”, whereas the fuller command-line option and argument parsing is what [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) and [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) provide.

A module can also turn up here because it is plainly deprecated and headed for removal in some later release, or because it is [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) so that new projects are steered away from it. Now that [**PEP 594**](https://peps.python.org/pep-0594/) has stripped out a range of outdated modules, nothing remains in that second group at present.

- [`getopt` — C-style parser for command line options](https://docs.python.org/3.14/library/getopt.html)

[Subject index](INDEX.md) · [Continue](../symtable/symtable-access-to-the-compiler-s-symbol-tables.md)
