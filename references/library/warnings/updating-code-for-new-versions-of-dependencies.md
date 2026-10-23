# warnings - Updating Code For New Versions of Dependencies

### Updating Code For New Versions of Dependencies

Warning categories aimed mainly at Python developers (as opposed to the end users of applications written in Python) are ignored by default.

In particular, that “ignored by default” set includes [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) (for every module other than `__main__`), so developers ought to be sure they test their code with the normally ignored warnings turned on, in order to get early notice of upcoming breaking API changes (be it in the standard library or in third party packages).

Ideally, the code comes with a proper test suite, and the test runner handles switching on all warnings implicitly while the tests run (the test runner that the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module ships does exactly this).

When circumstances are less than ideal, you can check an application for any reliance on deprecated interfaces by handing [`-Wd`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) to the Python interpreter (a shorthand for `-W default`) or by putting `PYTHONWARNINGS=default` in the environment. Doing so switches on default handling for every warning, the default-ignored ones included. If you want to alter what happens to the warnings encountered, change the argument you give to `-W` (for instance, `-W error`). Consult the `-W` flag for fuller coverage of the options.

[Subject index](INDEX.md) · [Previous](testing-warnings.md) · [Continue](warnings-warn-to-warnings-resetwarnings.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)
