# sys.flags

sys.flags

The [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) *flags* surfaces the state of the command line flags. Reach flags only by name and never by index. These attributes are read only.

| flags.debug | `-d` |
| --- | --- |
| flags.inspect | `-i` |
| flags.interactive | `-i` |
| flags.isolated | `-I` |
| flags.optimize | `-O` or `-OO` |
| flags.dont_write_bytecode | `-B` |
| flags.no_user_site | `-s` |
| flags.no_site | `-S` |
| flags.ignore_environment | `-E` |
| flags.verbose | `-v` |
| flags.bytes_warning | `-b` |
| flags.quiet | `-q` |
| flags.hash_randomization | `-R` |
| flags.dev_mode | `-X dev` (Python Development Mode) |
| flags.utf8_mode | `-X utf8` |
| flags.safe_path | `-P` |
| flags.int_max_str_digits | `-X int_max_str_digits` (integer string conversion length limitation) |
| flags.warn_default_encoding | `-X warn_default_encoding` |
| flags.gil | `-X gil` and `PYTHON_GIL` |
| flags.thread_inherit_context | `-X thread_inherit_context` and `PYTHON_THREAD_INHERIT_CONTEXT` |
| flags.context_aware_warnings | `-X context_aware_warnings` and `PYTHON_CONTEXT_AWARE_WARNINGS` |

Changed in version 3.2: Added `quiet` attribute for the new [`-q`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-q) flag.

Added in version 3.2.3: The `hash_randomization` attribute.

Changed in version 3.3: Removed obsolete `division_warning` attribute.

Changed in version 3.4: Added `isolated` attribute for [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) `isolated` flag.

Changed in version 3.7: Introduced the `dev_mode` attribute tied to the new [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode), along with the `utf8_mode` attribute tied to the new [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `utf8` flag.

Changed in version 3.10: Added `warn_default_encoding` attribute for the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `warn_default_encoding` flag.

Changed in version 3.11: Added the `safe_path` attribute for the [`-P`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-P) option.

Changed in version 3.11: Added the `int_max_str_digits` attribute.

Changed in version 3.13: Added the `gil` attribute.

Changed in version 3.14: Added the `thread_inherit_context` attribute.

Changed in version 3.14: Added the `context_aware_warnings` attribute.

[API family](INDEX.md) · [sys context index](../INDEX.md).
