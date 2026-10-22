# optparse — Standard option types

Writes to stdout the version number handed to the OptionParser and then exits. The actual formatting and printing of that version number falls to OptionParser's `print_version()` method. It only matters, by and large, when the `version` argument was given to the OptionParser constructor. Just as with `help` options, you will seldom build `version` options yourself, because `optparse` adds them automatically whenever they are needed.

### Standard option types

`optparse` ships five built-in option types: `"string"`, `"int"`, `"choice"`, `"float"` and `"complex"`. Should you want to introduce new option types, consult section Extending optparse.

Arguments given to string options undergo no checking or conversion at all: the command line text lands in the destination (or reaches the callback) unchanged.

Integer arguments (type `"int"`) get parsed this way:

- if the number starts with `0x`, it is parsed as a hexadecimal number

- if the number starts with `0`, it is parsed as an octal number

- if the number starts with `0b`, it is parsed as a binary number

- otherwise, the number is parsed as a decimal number

That conversion happens by invoking [`int()`](https://docs.python.org/3.14/library/functions.html#int) with the proper base (2, 8, 10, or 16). Should that fail, `optparse` fails too, though with a more helpful error message.

`"float"` and `"complex"` option arguments are converted straight through with [`float()`](https://docs.python.org/3.14/library/functions.html#float) and [`complex()`](https://docs.python.org/3.14/library/functions.html#complex), under comparable error-handling.

`"choice"` options form a subtype of `"string"` options. The `choices` option attribute (a sequence of strings) lays out the set of permitted option arguments. `optparse.check_choice()` checks user-supplied option arguments against this master list and raises `OptionValueError` whenever an invalid string appears.

[Subject index](INDEX.md) · [Continue](optionparser-parse-args.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: Standard option actions](standard-option-actions-overview.md) · [Preceding source contract and version conditions](option-action-callback-contract.md)
