# What’s New In Python 3.5 / compileall - compileall

### compileall

A fresh [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) option, `-j *N*`, lets you spin up *N* workers at once to carry out parallel bytecode compilation. A matching `workers` parameter exists on the [`compile_dir()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_dir) function. (Contributed by Claudiu Popa in [bpo-16104](https://bugs.python.org/issue?@action=redirect&bpo=16104).)

One more fresh option, `-r`, governs the deepest recursion level reached across subdirectories. (Contributed by Claudiu Popa in [bpo-19628](https://bugs.python.org/issue?@action=redirect&bpo=19628).)

You can henceforth supply the `-q` command line option more than once, and when you do all output, errors included, gets suppressed. The matching `quiet` parameter on [`compile_dir()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_dir), [`compile_file()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_file), and [`compile_path()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_path) will henceforth take an integer value that signals the degree of output suppression. (Contributed by Thomas Kluyver in [bpo-21338](https://bugs.python.org/issue?@action=redirect&bpo=21338).)

[Subject index](INDEX.md) · [Previous source section](collections-abc.md) · [Next source section](concurrent-futures.md) · [Release/subject declaration](summary-release-highlights.md)
