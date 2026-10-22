# Python 3.11.0 beta 1 / core and builtins / functions and types

[bpo-47177](https://bugs.python.org/issue?@action=redirect&bpo=47177): Substitute a `prev_instr` pointer for the `f_lasti` member of the internal `_PyInterpreterFrame` structure, cutting overhead within the main interpreter loop. For backward-compatibility, the `f_lasti` attribute on Python-layer frame objects stays in place.

[bpo-46764](https://bugs.python.org/issue?@action=redirect&bpo=46764): Resolve wrapping of bound methods using @classmethod.

[gh-91266](https://github.com/python/cpython/issues/91266): Rework the `bytearray` strip methods `strip`, `lstrip` and `rstrip` so that they share one common implementation.

[gh-92063](https://github.com/python/cpython/issues/92063): The `PRECALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS` instruction will now confirm that methods get invoked solely against objects whose type matches.

[gh-91102](https://github.com/python/cpython/issues/91102): Convert `EncodingMap` to Argument Clinic. Oleg Iarygin authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
