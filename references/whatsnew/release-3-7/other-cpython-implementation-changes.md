# What's New In Python 3.7 / Other CPython Implementation Changes

### Other CPython Implementation Changes

- By assigning the new [`f_trace_lines`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_lines) and [`f_trace_opcodes`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_trace_opcodes) attributes on the frame under trace, trace hooks can now decline `line` events and request `opcode` events from the interpreter. (Contributed by Nick Coghlan in [bpo-31344](https://bugs.python.org/issue?@action=redirect&bpo=31344).)

- Several inconsistencies affecting namespace package module attributes were corrected. A namespace module object now carries an `__file__` equal to `None` (it had been unset before), and likewise its `__spec__.origin` is now `None` (previously the string `"namespace"`). See [bpo-32305](https://bugs.python.org/issue?@action=redirect&bpo=32305). Furthermore, the namespace module object's `__spec__.loader` now matches `__loader__` (formerly that field held `None`). See [bpo-32303](https://bugs.python.org/issue?@action=redirect&bpo=32303).

- Entries in the [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) dictionary are now shown following the lexical sequence in which the variables were declared. The ordering had previously been unspecified. (Contributed by Raymond Hettinger in [bpo-32690](https://bugs.python.org/issue?@action=redirect&bpo=32690).)

- The `distutils` `upload` command will no longer attempt to swap CR line endings for CRLF. That corrects a corruption bug affecting sdists whose final byte equaled CR. (Contributed by Bo Bayles in [bpo-32304](https://bugs.python.org/issue?@action=redirect&bpo=32304).)

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](deprecated-python-behavior.md) · [Release/subject declaration](summary-release-highlights.md)
