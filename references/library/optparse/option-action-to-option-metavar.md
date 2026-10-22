# optparse: `Option.action`, `Option.type`, `Option.dest`, `Option.default`, `Option.nargs`, `Option.const`, `Option.choices`, `Option.callback`, `Option.callback_args`, `Option.callback_kwargs`, `Option.help`, `Option.metavar`

Option.action

(default: `"store"`)

Governs how `optparse` behaves once this option turns up on the command line; the choices available are documented here.

 Option.type

(default: `"string"`)

The kind of argument this option expects (for example `"string"` or `"int"`); the option types on offer are documented here.

 Option.dest

(default: derived from option strings)

When the option's action calls for writing or altering a value someplace, this points `optparse` to the destination: `dest` identifies an attribute on the `options` object that `optparse` constructs while parsing the command line.

 Option.default

The value assigned to this option's destination should the option never appear on the command line. See also `OptionParser.set_defaults()`.

 Option.nargs

(default: 1)

The count of `type`-typed arguments to consume each time this option appears. When greater than 1, `optparse` saves a tuple of values into `dest`.

 Option.const

For actions that store a constant value, the constant value to store.

 Option.choices

For `"choice"`-type options, the roster of strings the user is allowed to pick from.

 Option.callback

For options whose action is `"callback"`, the callable invoked once this option turns up. See section Option Callbacks for detail on the arguments handed to the callable.

 Option.callback_args

 Option.callback_kwargs

Extra positional and keyword arguments handed to `callback` following the four standard callback arguments.

 Option.help

Help text shown for this option while listing every available option once the user provides a `help` option (such as `--help`). When no help text is given, the option appears in the listing without any. To conceal this option, use the special value `optparse.SUPPRESS_HELP`.

 Option.metavar

(default: derived from option strings)

Placeholder used in place of the option argument(s) while printing help text. See section Tutorial for an example.

[Subject index](INDEX.md) · [Previous](optparse-option-class.md) · [Continue](standard-option-actions-overview.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: optparse.Option](optparse-option-class.md) · [Owning module, declaration or section: Option attributes](optparse-option-class.md)
