# argparse - Printing help

### Printing help

For the bulk of programs, `parse_args()` handles laying out and emitting whatever usage or error text is needed on its own. Even so, a handful of formatting methods are at your disposal:

 ArgumentParser.print_usage(*file=None*)

Writes out a short note on the way the `ArgumentParser` is meant to be called at the command line. When *file* is `None`, [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) is taken as the target.

 ArgumentParser.print_help(*file=None*)

Writes out a help message that covers the program's usage along with details of the arguments registered on the `ArgumentParser`. When *file* is `None`, [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) is taken as the target.

Companion versions of these methods exist too, handing back a string rather than printing one:

 ArgumentParser.format_usage()

Hands back a string holding a short note on the way the `ArgumentParser` is meant to be called at the command line.

 ArgumentParser.format_help()

Hands back a string holding a help message that covers the program's usage along with details of the arguments registered on the `ArgumentParser`.

[Subject index](INDEX.md) · [Previous](argumentparser-set-defaults-to-argumentparser-get-default.md) · [Continue](argumentparser-parse-known-args.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)
