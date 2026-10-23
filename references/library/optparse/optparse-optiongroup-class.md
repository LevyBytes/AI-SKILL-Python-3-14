# optparse - Grouping Options - Signature and initial contract

*class *optparse.OptionGroup(*parser*, *title*, *description=None*)

where

- parser is the `OptionParser` instance the group will be inserted in to

- title is the group title

- description, optional, is a long description of the group

Because `OptionGroup` derives from `OptionContainer` (just as `OptionParser` does), you can call its `add_option()` method to attach an option to the group.

After every option has been declared, the group is attached to the previously built parser through the `OptionParser` method `add_option_group()`.

Building on the parser from the previous section, attaching an `OptionGroup` to a parser is straightforward:

```python
group = OptionGroup(parser, "Dangerous Options",
                    "Caution: use these options at your own risk.  "
                    "It is believed that some of them bite.")
group.add_option("-g", action="store_true", help="Group option.")
parser.add_option_group(group)

```

The help output produced by this would be:

```text
Usage: <yourscript> [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -v, --verbose         make lots of noise [default]
  -q, --quiet           be vewwy quiet (I'm hunting wabbits)
  -f FILE, --filename=FILE
                        write output to FILE
  -m MODE, --mode=MODE  interaction mode: novice, intermediate, or
                        expert [default: intermediate]

  Dangerous Options:
    Caution: use these options at your own risk.  It is believed that some
    of them bite.

    -g                  Group option.

```

A somewhat fuller example might use more than a single group; continuing to extend the earlier example:

```python
group = OptionGroup(parser, "Dangerous Options",
                    "Caution: use these options at your own risk.  "
                    "It is believed that some of them bite.")
group.add_option("-g", action="store_true", help="Group option.")
parser.add_option_group(group)

group = OptionGroup(parser, "Debug Options")
group.add_option("-d", "--debug", action="store_true",
                 help="Print debug information")
group.add_option("-s", "--sql", action="store_true",
                 help="Print all SQL statements executed")
group.add_option("-e", action="store_true", help="Print every action done")
parser.add_option_group(group)

```

which yields the output below:

[Subject index](INDEX.md) · [Previous](grouping-options.md) · [Continue](option-group-help-example.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: Grouping Options](grouping-options.md)
