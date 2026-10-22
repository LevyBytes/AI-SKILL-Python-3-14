# Instrumenting CPython with DTrace and SystemTap

## Instrumenting CPython with DTrace and SystemTap

### Instrumenting CPython with DTrace and SystemTap

author:

David Malcolm

author:

Łukasz Langa

Both DTrace and SystemTap serve as observability tools, each giving you a means to examine the activity of processes running on a machine. Each one relies on its own domain-specific language in which you author scripts that:

- select the processes that will be watched

- collect measurements from those targeted processes

- produce summaries from what was collected

Beginning with Python 3.6, you can compile CPython so that it carries built-in “markers” (the same things called “probes”), which a DTrace or SystemTap script is able to watch, simplifying the job of keeping track of what CPython processes are up to on a host.

**CPython implementation detail:** The DTrace markers belong to the inner workings of the CPython interpreter. There is no promise that probes will stay compatible from one CPython release to the next. A DTrace script may quietly break or behave wrongly with no notice once you move to a different CPython version.

[Subject index](INDEX.md) · [Previous source context](../python-howtos/advanced-development-debugging-and-profiling-index.md) · [Following source context](build-dtrace-systemtap-markers-and-inspect-macos-probes.md)
