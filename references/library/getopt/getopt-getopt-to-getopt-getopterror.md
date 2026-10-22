# getopt — `getopt` — C-style parser for command line options

## getopt — C-style parser for command line options

### `getopt` — C-style parser for command line options

**Source code:** [Lib/getopt.py](https://github.com/python/cpython/tree/3.14/Lib/getopt.py)

Note

This module is regarded as feature complete. For an alternative to this API that is more declarative and extensible, turn to the [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module. Additional capabilities for handling command line parameters come either from third-party modules on PyPI or from features within the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module.

---

Scripts can lean on this module to parse the command line arguments held in `sys.argv`. It honors the same conventions the Unix `getopt()` function does (the special handling of arguments shaped like ‘`-`’ and ‘`--`‘ included). By way of an optional third argument, long options resembling those GNU software supports can be used too.

Anyone not already acquainted with the Unix `getopt()` function would be wise to reach for the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module instead. Those who do know the Unix `getopt()` function but want comparable behavior with less code to write plus better help and error messages would do well to look at the [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse) module. Consult [Choosing an argument parsing library](https://docs.python.org/3.14/library/optparse.html#choosing-an-argument-parser) for more details.

This module provides two functions and an exception:

 getopt.getopt(*args*, *shortopts*, *longopts=[]*)

Parses the command line options together with the parameter list. *args* is the list of arguments to parse, minus the leading reference to the program being run. Typically that means `sys.argv[1:]`. *shortopts* is the string holding the option letters the script wants to recognize; options needing an argument are trailed by a colon (`':'`) and options that take an optional argument are trailed by two colons (`'::'`) — that is, the very format Unix `getopt()` employs.

Note

In contrast to GNU `getopt()`, every argument following a non-option argument is treated as a non-option too. That mirrors how non-GNU Unix systems behave.

*longopts*, when given, has to be a list of strings naming the long options that ought to be supported. The leading `'--'` characters should be left out of the option name. A long option that requires an argument ought to be trailed by an equal sign (`'='`). A long option that takes an optional argument ought to be trailed by an equal sign and a question mark (`'=?'`). For only long options to be accepted, *shortopts* should be the empty string. Long options on the command line are recognized provided they give a prefix of the option name that matches exactly one accepted option. As an example, where *longopts* is `['foo', 'frob']`, the option `--fo` resolves to `--foo`, whereas `--f` lacks a unique match, so `GetoptError` gets raised.

Two elements make up the return value: first comes a list of `(option, value)` pairs; second comes the list of program arguments remaining once the option list was peeled away (a trailing slice of *args*). Every returned option-and-value pair holds the option as its first element — prefixed with one hyphen for short options (such as `'-x'`) or two hyphens for long options (such as `'--long-option'`) — and the option's argument as its second element, or an empty string when the option carries no argument. The options appear in the list following the same order in which they showed up, which permits multiple occurrences. Mixing long and short options is allowed.

Changed in version 3.14: Optional arguments are supported.

 getopt.gnu_getopt(*args*, *shortopts*, *longopts=[]*)

This function behaves like `getopt()`, save that GNU style scanning mode applies by default. That allows option and non-option arguments to be interspersed. The `getopt()` function quits processing options the moment a non-option argument shows up.

When the option string opens with the character `'+'`, or when the environment variable `POSIXLY_CORRECT` is set, option processing halts the moment a non-option argument shows up.

When the option string opens with the character `'-'`, any non-option arguments trailed by options get appended to the option-and-value pair list as a pair whose first slot holds `None` and whose second slot holds the list of those non-option arguments. The second element of what `gnu_getopt()` returns lists the program arguments that follow the last option.

Changed in version 3.14: Added the ability to return interspersed options and non-option arguments in their original order.

 *exception *getopt.GetoptError

This gets raised when the argument list contains an option that isn't recognized, or when an option that requires an argument receives none. The exception's argument is a string describing what caused the error. With long options, supplying an argument to an option that doesn't require one will likewise raise this exception. The attributes `msg` and `opt` carry the error message and the related option; when no specific option is tied to the exception, `opt` is the empty string.

[Subject index](INDEX.md) · [Continue](getopt-error.md)
