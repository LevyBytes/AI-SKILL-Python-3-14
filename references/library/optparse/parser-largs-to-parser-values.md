# optparse — How callbacks are called

### How callbacks are called

All callbacks are called as follows:

```python
func(option, opt_str, value, parser, *args, **kwargs)

```

where

`option`

is the Option instance that's calling the callback

`opt_str`

is the option string spotted on the command-line that sets off the callback. (When an abbreviated long option was given, `opt_str` will hold the full, canonical option string—for example, if the user types `--foo` on the command-line as shorthand for `--foobar`, then `opt_str` becomes `"--foobar"`.)

`value`

is the argument for this option spotted on the command-line. `optparse` only looks for an argument when `type` is set; the type of `value` follows from the option's type. When this option's `type` is `None` (no argument expected), `value` comes out `None`. When `nargs` > 1, `value` becomes a tuple of values of the fitting type.

`parser`

is the OptionParser instance steering everything, valuable chiefly because its instance attributes give you a way into some other interesting data:

`parser.largs`

the present list of leftover arguments, that is, arguments already consumed yet being neither options nor option arguments. Go ahead and modify `parser.largs`, say by tacking more arguments onto it. (This list turns into `args`, the second return value from `parse_args()`.)

`parser.rargs`

the present list of remaining arguments, that is, with `opt_str` and `value` (where applicable) stripped out, leaving only the arguments that came after them. Go ahead and modify `parser.rargs`, say by consuming more arguments.

`parser.values`

the object that by default holds option values (an instance of optparse.OptionValues). Through it, callbacks can store option values by the same mechanism the rest of `optparse` uses; there's no need to fiddle with globals or closures. You can likewise read or change the value(s) of any options already met along the command-line.

`args`

is a tuple holding whatever positional arguments you provided through the `callback_args` option attribute.

`kwargs`

is a dictionary holding whatever keyword arguments you provided through `callback_kwargs`.

[Subject index](INDEX.md) · [Previous](defining-a-callback-option.md) · [Continue](raising-errors-in-a-callback.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
