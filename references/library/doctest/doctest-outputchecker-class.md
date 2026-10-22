# doctest: `doctest.OutputChecker`

### OutputChecker objects

 *class *doctest.OutputChecker

A class whose role is verifying whether a doctest example's actual output lines up with the expected output. `OutputChecker` provides two methods: `check_output()`, which weighs a supplied pair of outputs and returns `True` when they agree; and `output_difference()`, which returns a string spelling out how the two outputs differ.

`OutputChecker` defines the following methods:

[Subject index](INDEX.md) · [Previous](doctest-runner-reporting-and-summary.md) · [Continue](doctest-output-comparison-and-differences.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)
