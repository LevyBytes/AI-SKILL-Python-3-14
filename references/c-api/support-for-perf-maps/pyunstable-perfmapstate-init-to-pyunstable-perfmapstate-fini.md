# Support for Perf Maps

## Support for Perf Maps

### Support for Perf Maps

Where the platform allows it (which, at the time of writing, means Linux only), the runtime can lean on *perf map files* so that an outside profiling tool — [perf](https://perf.wiki.kernel.org/index.php/Main_Page), for instance — can see Python functions. A live process is free to drop a file into the `/tmp` directory whose entries tie a stretch of executable code to a name. The shape of this interface appears in the [documentation of the Linux Perf tool](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/perf/Documentation/jit-interface.txt).

Within Python, libraries and features that depend on emitting machine code at runtime can put these helper APIs to use.

Bear in mind that no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) has to be held when calling these APIs.

 int PyUnstable_PerfMapState_Init(void)

 *Counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); it can shift without notice across minor releases.*

Unless it is open already, open the `/tmp/perf-$pid.map` file and set up a lock guaranteeing thread-safe writes to it (so long as those writes go through `PyUnstable_WritePerfMapEntry()`). As a rule you needn't invoke this directly; simply call `PyUnstable_WritePerfMapEntry()`, which sets the state up the first time around.

A `0` comes back on success, `-1` when the perf map file can't be created or opened, and `-2` when the lock can't be made. Consult `errno` to learn more about what went wrong.

 int PyUnstable_WritePerfMapEntry(const void *code_addr, unsigned int code_size, const char *entry_name)

 *Counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); minor releases may alter it with no warning given.*

Commit a single lone entry to the `/tmp/perf-$pid.map` file. The call is thread safe. A sample entry takes this form:

```c
# address      size  name
7f3529fcf759 b     py::bar:/run/t.py

```

Should the perf map file not yet be open, it invokes `PyUnstable_PerfMapState_Init()` ahead of writing the entry. On success it gives back `0`; on failure it returns the very error codes that `PyUnstable_PerfMapState_Init()` would.

 void PyUnstable_PerfMapState_Fini(void)

 *Counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); it is liable to change with no warning between minor releases.*

Shut the perf map file that `PyUnstable_PerfMapState_Init()` opened. The runtime fires this itself as the interpreter winds down. By and large you'll have no cause to call it directly, save for particular situations like forking.

[Subject index](INDEX.md) · [Previous source contract](../object-implementation-support/object-implementation-support.md) · [Following source contract](../pickle-buffer-objects/pypicklebuffer-type-to-pypicklebuffer-release.md)
