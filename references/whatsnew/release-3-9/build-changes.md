# What's New In Python 3.9 / Build Changes - sys

### Build Changes

- A `--with-platlibdir` option was added to the `configure` script: it sets the name of the platform-specific library directory, kept in the new [`sys.platlibdir`](https://docs.python.org/3.14/library/sys.html#sys.platlibdir) attribute. Consult the `sys.platlibdir` attribute for further detail. (Contributed by Jan Matějek, Matěj Cepl, Charalampos Stratakis and Victor Stinner in [bpo-1294959](https://bugs.python.org/issue?@action=redirect&bpo=1294959).)

- The `COUNT_ALLOCS` special build macro is gone. (Contributed by Victor Stinner in [bpo-39489](https://bugs.python.org/issue?@action=redirect&bpo=39489).)

- Off Windows platforms, building Python now requires the `setenv()` and `unsetenv()` functions. (Contributed by Victor Stinner in [bpo-39395](https://bugs.python.org/issue?@action=redirect&bpo=39395).)

- Off Windows platforms, producing `bdist_wininst` installers is now officially unsupported. (Consult [bpo-10945](https://bugs.python.org/issue?@action=redirect&bpo=10945) for further detail.)

- When you build Python on macOS from source, `_tkinter` now links against non-system Tcl and Tk frameworks should they be installed under `/Library/Frameworks`, just as it did on earlier macOS releases. Where a macOS SDK is explicitly configured, through [`--enable-universalsdk`](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-universalsdk) or `-isysroot`, the search covers the SDK alone. You can still override the default behavior using `--with-tcltk-includes` and `--with-tcltk-libs`. (Contributed by Ned Deily in [bpo-34956](https://bugs.python.org/issue?@action=redirect&bpo=34956).)

- Python is now buildable for Windows 10 ARM64. (Contributed by Steve Dower in [bpo-33125](https://bugs.python.org/issue?@action=redirect&bpo=33125).)

-

A handful of particular tests now get bypassed whenever `--pgo` is in play. Those tests bloated the PGO task time by a lot while probably doing little to sharpen the optimization of the resulting executable. Dropping them cuts the task duration by roughly 15x. Executing the complete unit test suite takes a while. As a side effect, the build may come out marginally less optimized, since fewer code branches end up being exercised. Should you be content to sit through the far slower build, you can bring the prior behavior back with `./configure [..] PROFILE_TASK="-m test --pgo-extended"`. There is no promise from us about which PGO task set yields a quicker build. Anyone who cares ought to run benchmarks that matter to them, because outcomes can hinge on the environment, workload, and compiler tool chain. (Consult [bpo-36044](https://bugs.python.org/issue?@action=redirect&bpo=36044) and [bpo-37707](https://bugs.python.org/issue?@action=redirect&bpo=37707) for the particulars.)

[Subject index](INDEX.md) · [Previous source section](bytecode-migration-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](c-api-changes-new-features.md)
