# What's New In Python 3.6 / DTrace and SystemTap probing support

### DTrace and SystemTap probing support

The interpreter now supports a `--with-dtrace` build option that turns on static markers covering these interpreter events:

- function call/return

- garbage collection started/finished

- line of code executed.

You can apply this to observe live interpreters in a production setting, sparing you from rebuilding dedicated [debug builds](https://docs.python.org/3.14/using/configure.html#debug-build) or writing your own application-specific profiling/debugging code.

Further coverage appears in [Instrumenting CPython with DTrace and SystemTap](https://docs.python.org/3.14/howto/instrumentation.html#instrumentation).

So far the implementation has been verified on Linux and macOS. More markers might land down the road.

(Contributed by Łukasz Langa in [bpo-21590](https://bugs.python.org/issue?@action=redirect&bpo=21590); his work drew from patches authored by Jesús Cea Avión, David Malcolm, and Nikhil Benesch.)

[Subject index](INDEX.md) · [Previous source section](pythonmalloc-environment-variable.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](summary-release-highlights.md)
