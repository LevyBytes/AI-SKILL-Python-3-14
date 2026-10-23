# optparse - Choosing an argument parsing library - Contract: handing in `-o=foo` yields `output="=foo"` under `optparse`, but yields `output="foo"` under `argparse` (because `=` is special cased as an alternate separator for option parameter values)

- handing in `-o=foo` yields `output="=foo"` under `optparse`, but yields `output="foo"` under `argparse` (because `=` is special cased as an alternate separator for option parameter values)

Whether these diverging behaviors in the `argparse` version count as desirable or as a problem hinges on the particular command line application use case.

See also

[click](https://pypi.org/project/click/) is a third party argument processing library (its roots lie in `optparse`) that lets command line applications take shape as a collection of decorated command implementation functions.

Further third party libraries, [typer](https://pypi.org/project/typer/) or [msgspec-click](https://pypi.org/project/msgspec-click/) among them, let command line interfaces be described in ways that mesh better with static checking of Python type annotations.

[Subject index](INDEX.md) · [Previous](argument-parser-library-selection-overview.md) · [Continue](introduction.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: Choosing an argument parsing library](argument-parser-library-selection-overview.md)
