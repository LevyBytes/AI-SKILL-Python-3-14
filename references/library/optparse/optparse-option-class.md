# optparse: `optparse.Option`

### Option attributes

 *class *optparse.Option

One command line argument whose assorted attributes are handed by keyword to the constructor. You normally make it through `OptionParser.add_option()` rather than directly, and a custom class supplied via the *option_class* argument to `OptionParser` can override it.

You may hand the following option attributes as keyword arguments to `OptionParser.add_option()`. Passing an option attribute irrelevant to a given option, or skipping a required one, makes `optparse` raise `OptionError`.

[Subject index](INDEX.md) · [Previous](optparse-values-class.md) · [Continue](option-action-to-option-metavar.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
