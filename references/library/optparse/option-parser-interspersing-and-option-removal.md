# optparse - Querying and manipulating your option parser

### Querying and manipulating your option parser

You can tweak the option parser's default behavior somewhat, and you can also dig around inside your option parser to inspect its contents. OptionParser offers a number of methods to assist:

 OptionParser.disable_interspersed_args()

Make parsing halt at the first non-option. For instance, when `-a` and `-b` are both plain options taking no arguments, `optparse` ordinarily allows this syntax:

```python
prog -a arg1 -b arg2

```

and treats it as equivalent to

```python
prog -a -b arg1 arg2

```

Calling `disable_interspersed_args()` switches this feature off. Doing so brings back the traditional Unix syntax, where option parsing ends at the first non-option argument.

Reach for this when you have a command processor that launches another command carrying its own options, and you want to be sure those options stay unconfused. Each command, for instance, might have its own distinct option set.

 OptionParser.enable_interspersed_args()

Make parsing not halt at the first non-option, so switches can be mixed in among command arguments. This is the default behavior.

 OptionParser.get_option(*opt_str*)

Hands back the Option instance bearing the option string *opt_str*, or `None` when no option carries that option string.

 OptionParser.has_option(*opt_str*)

Yields `True` when the OptionParser owns an option whose option string is *opt_str* (for instance, `-q` or `--verbose`).

 OptionParser.remove_option(*opt_str*)

When the `OptionParser` holds an option matching *opt_str*, that option is removed. Should that option have supplied any other option strings, all of those become invalid. When *opt_str* belongs to no option in this `OptionParser`, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

[Subject index](INDEX.md) · [Previous](optionparser-parse-args.md) · [Continue](conflicts-between-options.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
