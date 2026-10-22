# Python 3.14.0 alpha 1 / library / argparse

[gh-65865](https://github.com/python/cpython/issues/65865): [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) will now fail fast with an error on invalid `help` arguments handed to [`add_argument()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument), [`add_subparsers()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_subparsers) and `add_parser()`.

[gh-85935](https://github.com/python/cpython/issues/85935): [`argparse.ArgumentParser.add_argument()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument) will now throw an exception whenever an [action](https://docs.python.org/3.14/library/argparse.html#action) that takes no arguments (such as "store_const" or "store_true"), or an explicit `nargs=0`, is given for positional arguments.

[gh-124693](https://github.com/python/cpython/issues/124693): Fixes a defect where [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) fails to recognise negative complex numbers, or negatives written in scientific notation.

[gh-66436](https://github.com/python/cpython/issues/66436): Better default for [prog](https://docs.python.org/3.14/library/argparse.html#prog) in [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser). Its value now folds in the Python executable's name together with whatever was used to launch: a module name, a package name, a directory path, a ZIP file, or even a directory nested within a ZIP file when the code started up that way.

[gh-72795](https://github.com/python/cpython/issues/72795): Positional arguments whose [nargs](https://docs.python.org/3.14/library/argparse.html#nargs) is `'*'` or `argparse.REMAINDER` stop being required. That permits a positional argument with `nargs='*'` and no `default` inside a mutually exclusive group, and it sharpens the error text about required arguments.

[gh-59317](https://github.com/python/cpython/issues/59317): Repairs parsing of a positional argument whose [nargs](https://docs.python.org/3.14/library/argparse.html#nargs) is `'?'` or `'*'` when an option plus another positional argument come ahead of it.

[gh-53780](https://github.com/python/cpython/issues/53780): [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) will now skip the initial `"--"` (double dash) placed between an option and a command.

[gh-81691](https://github.com/python/cpython/issues/81691): Repairs treatment of several `"--"` (double dashes) inside [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse). Just the first is dropped now; everything after it is read literally.

[gh-87041](https://github.com/python/cpython/issues/87041): Repaired an [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) defect that indented long subparser argument help wrongly.

[gh-123945](https://github.com/python/cpython/issues/123945): Repairs a defect where [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) misses negative numbers written with underscores

[gh-117766](https://github.com/python/cpython/issues/117766): When printing `choices` inside [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse), [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) is now applied unconditionally.

[gh-113008](https://github.com/python/cpython/issues/113008): The argparse usage line is corrected for required, mutually exclusive groups that hold a positional argument

[bpo-44864](https://bugs.python.org/issue?@action=redirect&bpo=44864): Strings supplied by the user are no longer translated inside [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser).

[bpo-14074](https://bugs.python.org/issue?@action=redirect&bpo=14074): The [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) metavar handling is fixed so a positional argument may take a tuple metavar.

[gh-121151](https://github.com/python/cpython/issues/121151): Correct the wrapping of lengthy usage text for arguments placed inside a mutually exclusive group in [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse).

[gh-125254](https://github.com/python/cpython/issues/125254): Repair a defect where ArgumentError reports the wrong ambiguous option inside [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse).

[gh-61011](https://github.com/python/cpython/issues/61011): Repair how nested mutually exclusive groups are inherited from the parent parser within [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser). Formerly, every nested mutually exclusive group dropped its link to the enclosing group and instead appeared to sit directly on the parser.

[gh-116850](https://github.com/python/cpython/issues/116850): Corrects [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) for namespaces whose dict isn't directly writable (classes, for example).

[gh-58573](https://github.com/python/cpython/issues/58573): Resolves clashes between abbreviated long options defined on the parent parser versus subparsers in [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse).

[gh-61181](https://github.com/python/cpython/issues/61181): Repairs [choices](https://docs.python.org/3.14/library/argparse.html#choices) support for string values in [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse). Any substring of the given string is no longer treated as a valid value.

[gh-80259](https://github.com/python/cpython/issues/80259): Repairs how [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) handles positional arguments declared with `nargs='?'`, `default=argparse.SUPPRESS` plus a specified `type`.

[gh-53834](https://github.com/python/cpython/issues/53834): Repairs handling of arguments carrying [choices](https://docs.python.org/3.14/library/argparse.html#choices) in [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse). For positional arguments whose [nargs](https://docs.python.org/3.14/library/argparse.html#nargs) is `'?'` or `'*'`, the [default](https://docs.python.org/3.14/library/argparse.html#default) is no longer checked against `choices`. For optional arguments whose `nargs` is `'?'`, the [const](https://docs.python.org/3.14/library/argparse.html#const) is no longer checked against `choices`.

[gh-124345](https://github.com/python/cpython/issues/124345): [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) now handles abbreviated single-dash long options when they are split from the value by `=`.

[gh-104860](https://github.com/python/cpython/issues/104860): Repairs the prohibition on abbreviating single-dash long options in [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) when `allow_abbrev=False`.

[gh-63143](https://github.com/python/cpython/issues/63143): Repairs how mutually exclusive arguments parse in [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse). Arguments whose value equals the default (booleans, small integers, empty or single-character strings, say) are no longer counted as "not present".

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
