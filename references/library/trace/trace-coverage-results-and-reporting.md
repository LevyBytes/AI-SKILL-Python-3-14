# trace / Programmatic Interface: `trace.CoverageResults`, `update()`, `write_results()`

*class *trace.CoverageResults

A holder for coverage results, produced by `Trace.results()`. Users are not meant to instantiate it themselves.

 update(*other*)

Fold in data drawn from a second `CoverageResults` object.

 write_results(*show_missing=True*, *summary=False*, *coverdir=None*, ***, *ignore_missing_files=False*)

Emit the coverage results. Turn on *show_missing* to surface lines that recorded no hits. Turn on *summary* to fold a per-module coverage summary into the output. *coverdir* names the directory where the coverage result files are written. When it is `None`, each source file's results land in that file's own directory.

Should *ignore_missing_files* be `True`, coverage counts tied to files that have since vanished are passed over without complaint. If not, a vanished file triggers a [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError).

Changed in version 3.13: Added *ignore_missing_files* parameter.

A short example showing the programmatic interface in action:

```python
import sys
import trace

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

# run the new command using the given tracer
tracer.run('main()')

# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")

```

[Subject index](INDEX.md) · [Previous](trace-trace-run-to-trace-trace-results.md) · [Owning module, declaration or section: trace](coverage-py.md) · [Owning module, declaration or section: Programmatic Interface](trace-trace-class.md)
