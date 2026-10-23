# optparse - Raising errors in a callback

### Raising errors in a callback

Your callback function ought to raise `OptionValueError` whenever something is wrong with the option or its argument(s). `optparse` catches that and stops the program, writing the error message you provide to stderr. Make your message clear, concise, accurate, and sure to name the offending option. Otherwise the user will struggle to work out what went wrong.

[Subject index](INDEX.md) · [Previous](parser-largs-to-parser-values.md) · [Continue](callback-example-1-trivial-callback.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)
