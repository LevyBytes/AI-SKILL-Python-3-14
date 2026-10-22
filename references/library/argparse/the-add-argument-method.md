# argparse — The add_argument() method

### The add_argument() method

```text
ArgumentParser.add_argument(name or flags..., *[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest][, deprecated])
```

Specify the way a single command-line argument ought to be parsed. A fuller account of each parameter follows below, but here is the quick version:

- name or flags - Supply either a single name or several option strings, for instance `'foo'` or `'-f', '--foo'`.

- action - The fundamental kind of action that fires once the command line presents this argument.

- nargs - The number of command-line arguments that should be consumed.

- const - A constant value required by some action and nargs selections.

- default - The value yielded when the argument shows up neither on the command line nor within the namespace object.

- type - The type to which the command-line argument should be converted.

- choices - A sequence of the allowable values for the argument.

- required - Whether the option on the command line is allowed to be left out (applies to optionals only).

- help - A brief description of what the argument does.

- metavar - A name for the argument in usage messages.

- dest - The attribute name that gets attached to whatever object `parse_args()` hands back.

- deprecated - Whether or not use of the argument is deprecated.

An `Action` object that stands in for the argument is what the method hands back.

[Subject index](INDEX.md) · [Previous](color.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Required continuation of the source contract](name-or-flags.md)
