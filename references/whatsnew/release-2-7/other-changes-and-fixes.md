# What’s New in Python 2.7 / Other Changes and Fixes

### Other Changes and Fixes

- A pair of benchmark scripts, `iobench` and `ccbench`, joined the `Tools` directory. The first, `iobench`, gauges how fast the built-in file I/O objects handed back by [`open()`](https://docs.python.org/3.14/library/functions.html#open) run across assorted operations, whereas `ccbench` is a concurrency benchmark aiming to gauge computing throughput, thread switching latency, and IO processing bandwidth as it carries out several tasks with a varying thread count.

- Plural forms inside `.po` files are now understood by the `Tools/i18n/msgfmt.py` script. (Fixed by Martin von Löwis; [bpo-5464](https://bugs.python.org/issue?@action=redirect&bpo=5464).)

- While importing a module out of a `.pyc` or `.pyo` file that has a matching `.py` alongside it, the [`co_filename`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_filename) attributes on the resulting code objects get rewritten whenever the original filename is stale. That situation arises after a file is renamed, relocated, or reached by way of differing paths. (Patch by Ziga Seilnacht and Jean-Paul Calderone; [bpo-1180193](https://bugs.python.org/issue?@action=redirect&bpo=1180193).)

- The `regrtest.py` script now accepts a `--randseed=` switch whose integer becomes the random seed for the `-r` option, which runs tests in random order. That `-r` option additionally prints the seed it picked (Added by Collin Winter.)

- One more `regrtest.py` switch is `-j`, accepting an integer that says how many tests should run concurrently. On multi-core machines this cuts the overall runtime. The option plays well with several others, among them the `-R` switch that's notorious for lengthy runtimes. (Added by Antoine Pitrou, [bpo-6152](https://bugs.python.org/issue?@action=redirect&bpo=6152).) It pairs too with a fresh `-F` switch that keeps rerunning the chosen tests in a loop until one fails. (Added by Antoine Pitrou; [bpo-7312](https://bugs.python.org/issue?@action=redirect&bpo=7312).)

- Run as a script, the `py_compile.py` module now treats `'-'` as a valid argument, prompting it to read the roster of filenames to compile from standard input. (Contributed by Piotr Ożarowski; [bpo-8233](https://bugs.python.org/issue?@action=redirect&bpo=8233).)

[Subject index](INDEX.md) · [Previous source section](port-specific-changes-freebsd.md) · [Next source section](porting-to-python-2-7.md) · [Release/subject declaration](the-future-for-python-2-x.md)
