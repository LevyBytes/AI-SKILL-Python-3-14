# doctest: `doctest.REPORTING_FLAGS`, `doctest.register_optionflag()`

doctest.REPORTING_FLAGS

A bitmask or'ing together every reporting flag listed above.

A facility also exists for registering brand-new option flag names, though it's of little use unless you mean to extend `doctest` internals through subclassing:

 doctest.register_optionflag(*name*)

Make a fresh option flag carrying a given name, and hand back the new flag's integer value. `register_optionflag()` is available when you subclass `OutputChecker` or `DocTestRunner` to mint new options that your subclasses understand. `register_optionflag()` ought always to be invoked using this idiom:

```python
MY_FLAG = register_optionflag('MY_FLAG')

```

[Subject index](INDEX.md) · [Previous](doctest-dont-accept-true-for-1-to-doctest-fail-fast.md) · [Continue](directives.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: Option Flags](doctest-dont-accept-true-for-1-to-doctest-fail-fast.md)
