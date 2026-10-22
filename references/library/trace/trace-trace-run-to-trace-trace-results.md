# trace.Trace: `run()`, `runctx()`, `runfunc()`, `results()`

run(*cmd*)

Run the command and collect statistics from that run using the tracing parameters currently in effect. *cmd* has to be a string or code object fit for handing to [`exec()`](https://docs.python.org/3.14/library/functions.html#exec).

 runctx(*cmd*, *globals=None*, *locals=None*)

Run the command and collect statistics from that run using the tracing parameters currently in effect, within the supplied global and local environments. When left unspecified, *globals* and *locals* each fall back to empty dictionaries.

 runfunc(*func*, */*, **args*, ***kwds*)

Invoke *func* with the arguments you supply, overseen by the `Trace` object and governed by the tracing parameters currently in effect.

 results()

Hand back a `CoverageResults` object holding the combined results of every earlier `run`, `runctx`, and `runfunc` call made on this `Trace` instance. The accumulated trace results are left intact.

[Subject index](INDEX.md) · [Previous](trace-trace-class.md) · [Continue](trace-coverage-results-and-reporting.md) · [Owning module, declaration or section: trace](coverage-py.md) · [Owning module, declaration or section: trace.Trace](trace-trace-class.md) · [Owning module, declaration or section: Programmatic Interface](trace-trace-class.md)
