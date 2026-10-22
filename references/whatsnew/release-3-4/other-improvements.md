# What's New In Python 3.4 / Other Improvements — argparse, bz2, gzip, lzma, readline, stat, sys, test

### Other Improvements

- The [python](https://docs.python.org/3.14/using/cmdline.html#using-on-cmdline) command picks up a new [option](https://docs.python.org/3.14/using/cmdline.html#using-on-misc-options), `-I`, that makes it run in "isolated mode", where [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) leaves out both the script's own directory and the user's `site-packages` directory, while every `PYTHON*` environment variable gets disregarded (it pulls in `-s` together with `-E`). Further constraints could land down the road, all aiming to wall off a script's execution from the user's environment. Such isolation suits cases like running a system script through Python. Across most POSIX systems it's well suited to (and belongs in) the `#!` line of system scripts. (Contributed by Christian Heimes in [bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499).)

- Tab-completion ships switched on by default within the interactive interpreter wherever [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) is available. History likewise comes on by default and is saved into (and reloaded from) the `~/.python-history` file. (Contributed by Antoine Pitrou and ?ric Araujo in [bpo-5845](https://bugs.python.org/issue?@action=redirect&bpo=5845).)

- Launching the Python interpreter with `--version` now sends the version to standard output rather than standard error ([bpo-18338](https://bugs.python.org/issue?@action=redirect&bpo=18338)). Comparable adjustments reached [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) ([bpo-18920](https://bugs.python.org/issue?@action=redirect&bpo=18920)) plus other modules offering script-like invocation ([bpo-18922](https://bugs.python.org/issue?@action=redirect&bpo=18922)).

- The CPython Windows installer appends `.py` onto the `PATHEXT` variable as extensions get registered, so users can fire off a python script at the windows command prompt simply by typing its name minus the `.py` extension. (Contributed by Paul Moore in [bpo-18569](https://bugs.python.org/issue?@action=redirect&bpo=18569).)

- A fresh `make` target [coverage-report](https://devguide.python.org/coverage/#measuring-coverage-of-c-code-with-gcov-and-lcov) will compile python, exercise the test suite, and emit an HTML coverage report covering the C codebase by way of `gcov` plus [lcov](https://github.com/linux-test-project/lcov).

- The `-R` flag passed to the [python regression test suite](https://docs.python.org/3.14/library/test.html#regrtest) now hunts for memory allocation leaks as well, leaning on [`sys.getallocatedblocks()`](https://docs.python.org/3.14/library/sys.html#sys.getallocatedblocks). (Contributed by Antoine Pitrou in [bpo-13390](https://bugs.python.org/issue?@action=redirect&bpo=13390).)

- `python -m` operates with namespace packages now.

- The [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) module has been rewritten in C, so it pulls its constant values straight from the C header files rather than carrying the values hard-coded inside the python module the way it used to.

- Pulling several python modules out of one OS module (`.so`, `.dll`) functions properly now (it formerly returned, without complaint, just the first python module within the file). (Contributed by Václav ?milauer in [bpo-16421](https://bugs.python.org/issue?@action=redirect&bpo=16421).)

- A fresh opcode, `LOAD_CLASSDEREF`, was introduced to patch a bug around loading free variables inside class bodies that certain uses of [__prepare__](https://docs.python.org/3.14/reference/datamodel.html#prepare) could set off. (Contributed by Benjamin Peterson in [bpo-17853](https://bugs.python.org/issue?@action=redirect&bpo=17853).)

- Victor Stinner spotted and repaired a batch of MemoryError-related crashes using his [**PEP 445**](https://peps.python.org/pep-0445/)-based `pyfailmalloc` tool ([bpo-18408](https://bugs.python.org/issue?@action=redirect&bpo=18408), [bpo-18520](https://bugs.python.org/issue?@action=redirect&bpo=18520)).

- The `pyvenv` command will now take a `--copies` option, switching to copies instead of symlinks even on systems that default to symlinks. (Contributed by Vinay Sajip in [bpo-18807](https://bugs.python.org/issue?@action=redirect&bpo=18807).)

- > The `pyvenv` command also accepts a `--without-pip` option to suppress the otherwise-automatic bootstrapping of pip into the virtual environment. (Contributed by Nick Coghlan in [bpo-19552](https://bugs.python.org/issue?@action=redirect&bpo=19552) as part of the [**PEP 453**](https://peps.python.org/pep-0453/) implementation.)

- The encoding name has become optional inside the value you set for the [`PYTHONIOENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONIOENCODING) environment variable. That lets you configure only the error handler while leaving the default encoding alone. (Contributed by Serhiy Storchaka in [bpo-18818](https://bugs.python.org/issue?@action=redirect&bpo=18818).)

- The [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma), and [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) module `open` functions have gained support for `x` (exclusive creation) mode. (Contributed by Tim Heaney and Vajrasky Kok in [bpo-19201](https://bugs.python.org/issue?@action=redirect&bpo=19201), [bpo-19222](https://bugs.python.org/issue?@action=redirect&bpo=19222), and [bpo-19223](https://bugs.python.org/issue?@action=redirect&bpo=19223).)

[Subject index](INDEX.md) · [Previous source section](other-build-and-c-api-changes.md) · [Next source section](significant-optimizations.md) · [Release/subject declaration](release-highlights.md)
