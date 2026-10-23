# optparse - Creating the parser

### Reference Guide

### Creating the parser

To begin using `optparse`, your first step is to build an OptionParser instance.

 *class *optparse.OptionParser(*...*)

While the OptionParser constructor demands no positional arguments, it accepts a handful of optional keyword arguments. Always pass these as keyword arguments—do not depend on the sequence in which the arguments are declared.

`usage` (default: `"%prog [options]"`)

The usage summary shown whenever your program runs incorrectly or with a help option. As `optparse` writes the usage string, it turns `%prog` into `os.path.basename(sys.argv[0])` (or into `prog` when you handed in that keyword argument). To quash a usage message, hand in the special value `optparse.SUPPRESS_USAGE`.

`option_list` (default: `[]`)

A list of Option objects with which to fill the parser. Whatever options sit in `option_list` get inserted after anything in `standard_option_list` (a class attribute that OptionParser subclasses may set), yet ahead of any version or help options. Deprecated; instead call `add_option()` once the parser exists.

`option_class` (default: optparse.Option)

Class to use when adding options to the parser in `add_option()`.

`version` (default: `None`)

A version string printed once the user provides a version option. Give `version` a true value and `optparse` automatically tacks on a version option carrying the lone option string `--version`. The `%prog` substring expands exactly as it does for `usage`.

`conflict_handler` (default: `"error"`)

Dictates the response when options bearing clashing option strings get added to the parser; see section Conflicts between options.

`description` (default: `None`)

A paragraph of text offering a short summary of your program. `optparse` rewraps this paragraph to suit the present terminal width and shows it whenever the user asks for help (following `usage`, yet preceding the list of options).

`formatter` (default: a new `IndentedHelpFormatter`)

An optparse.HelpFormatter instance employed to render help text. For this job `optparse` ships two concrete classes: IndentedHelpFormatter and TitledHelpFormatter.

`add_help_option` (default: `True`)

When true, `optparse` attaches a help option (whose option strings are `-h` and `--help`) to the parser.

`prog`

The string used in place of `os.path.basename(sys.argv[0])` while expanding `%prog` within `usage` and `version`.

`epilog` (default: `None`)

A paragraph of help text shown following the option help.

[Subject index](INDEX.md) · [Continue](populating-the-parser.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
