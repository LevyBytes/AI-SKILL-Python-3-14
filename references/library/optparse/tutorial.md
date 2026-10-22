# optparse — Tutorial

### Tutorial

For all that `optparse` is flexible and powerful, it's also easy to use in most cases. This section walks through the code patterns shared by any `optparse`-based program.

To begin, you import the OptionParser class; then, early on in the main program, you build an OptionParser instance:

```python
from optparse import OptionParser
...
parser = OptionParser()

```

Next you can begin declaring options. The basic syntax runs:

```python
parser.add_option(opt_str, ...,
                  attr=value, ...)

```

Every option carries one or more option strings, such as `-f` or `--file`, plus several option attributes telling `optparse` what to expect and what to do once it meets that option on the command line.

As a rule, an option carries one short option string alongside one long option string, for example:

```python
parser.add_option("-f", "--file", ...)

```

Nothing stops you from declaring however many short option strings and long option strings you please (zero included), so long as one option string exists in total.

The option strings handed to `OptionParser.add_option()` act, in effect, as labels for the option that call defines. For brevity, we'll often speak of *encountering an option* on the command line; in truth, `optparse` encounters *option strings* and looks options up from them.

After every one of your options is declared, tell `optparse` to parse your program's command line:

```python
(options, args) = parser.parse_args()

```

(If you wish, you can hand a custom argument list to `parse_args()`, but that's rarely needed: by default it draws on `sys.argv[1:]`.)

`parse_args()` returns two values:

- `options`, an object holding values for every one of your options—for instance, if `--file` takes a lone string argument, then `options.file` ends up as the filename the user gave, or `None` when the user left that option out

- `args`, the list of positional arguments leftover after parsing options

This tutorial section limits itself to the four key option attributes: `action`, `type`, `dest` (destination), and `help`. Among them, `action` stands as the most fundamental.

[Subject index](INDEX.md) · [Previous](what-are-positional-arguments-for.md) · [Continue](understanding-option-actions.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
