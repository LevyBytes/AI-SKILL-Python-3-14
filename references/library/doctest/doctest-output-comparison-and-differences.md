# doctest.OutputChecker: `check_output()`, `output_difference()`

check_output(*want*, *got*, *optionflags*)

Hand back `True` exactly when an example's actual output (*got*) agrees with the expected output (*want*). Identical strings always count as agreeing; beyond that, the option flags the test runner has in force can enable several looser kinds of matching. The Option Flags section says more about those flags.

 output_difference(*example*, *got*, *optionflags*)

Hand back a string laying out how a given example's expected output (*example*) departs from its actual output (*got*). The *optionflags* value is the collection of option flags applied when comparing *want* with *got*.

[Subject index](INDEX.md) · [Previous](doctest-outputchecker-class.md) · [Continue](debugging.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: doctest.OutputChecker](doctest-outputchecker-class.md) · [Owning module, declaration or section: OutputChecker objects](doctest-outputchecker-class.md)
