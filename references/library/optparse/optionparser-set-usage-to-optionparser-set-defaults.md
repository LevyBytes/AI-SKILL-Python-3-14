# optparse - Other methods

### Other methods

OptionParser exposes several additional public methods:

 OptionParser.set_usage(*usage*)

Establish the usage string following the rules laid out earlier for the `usage` constructor keyword argument. Handing in `None` selects the default usage string; reach for `optparse.SUPPRESS_USAGE` to quash a usage message.

 OptionParser.print_usage(*file=None*)

Write the running program's usage message (`self.usage`) out to *file* (stdout by default). Each appearance of the string `%prog` within `self.usage` gets swapped for the running program's name. When `self.usage` is empty or undefined, this does nothing.

 OptionParser.get_usage()

Behaves like `print_usage()`, except it gives back the usage string rather than printing it.

 OptionParser.set_defaults(*dest=value*, *...*)

Assign default values to several option destinations in one call. Relying on `set_defaults()` is the recommended route for setting option defaults, since several options can share a single destination. For instance, when several "mode" options all target the same destination, whichever sets the default first matters less than the fact that the last one wins:

```python
parser.add_option("--advanced", action="store_const",
                  dest="mode", const="advanced",
                  default="novice")    # overridden below
parser.add_option("--novice", action="store_const",
                  dest="mode", const="novice",
                  default="advanced")  # overrides above setting

```

To steer clear of that muddle, lean on `set_defaults()`:

```python
parser.set_defaults(mode="advanced")
parser.add_option("--advanced", action="store_const",
                  dest="mode", const="advanced")
parser.add_option("--novice", action="store_const",
                  dest="mode", const="novice")

```

[Subject index](INDEX.md) · [Previous](cleanup.md) · [Continue](option-callbacks.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
