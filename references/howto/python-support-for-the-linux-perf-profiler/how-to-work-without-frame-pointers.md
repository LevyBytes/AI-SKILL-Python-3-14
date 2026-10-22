# How to work without frame pointers

### How to work without frame pointers

Even with a Python interpreter built without frame pointers, the `perf` profiler remains usable; the catch is somewhat greater overhead, because Python has to produce unwinding information for each Python function call as it happens. Processing the data also takes `perf` longer, since it has to fall back on the DWARF debugging information to unwind the stack, which is a slow undertaking.

You switch this mode on through the [`PYTHON_PERF_JIT_SUPPORT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT) environment variable or the [`-X perf_jit`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option, both of which turn on JIT mode for the `perf` profiler.

Note

Owing to a defect in the `perf` tool, JIT mode functions only with `perf` releases above v6.8. That fix was additionally backported into the v6.7.2 build of the tool.

Bear in mind that when you inspect the `perf` tool's version — which you can do by running `perf version` — some distributions tack on their own custom version numbers, including a `-` character. So `perf 6.7-3` does not automatically equal `perf 6.7.3`.

Working in perf JIT mode requires one more step ahead of running `perf report`: you must run the `perf inject` command so the JIT information is injected into the `perf.data` file.:

```shell
$ perf record -F 9999 -g -k 1 --call-graph dwarf -o perf.data python -Xperf_jit my_script.py
$ perf inject -i perf.data --jit --output perf.jit.data
$ perf report -g -i perf.jit.data

```

or using the environment variable:

```shell
$ PYTHON_PERF_JIT_SUPPORT=1 perf record -F 9999 -g --call-graph dwarf -o perf.data python my_script.py
$ perf inject -i perf.data --jit --output perf.jit.data
$ perf report -g -i perf.jit.data

```

The `perf inject --jit` command reads `perf.data`, locates on its own the perf dump file Python writes (at `/tmp/perf-$PID.dump`), and produces `perf.jit.data`, into which it folds all of the JIT information. Expect it to drop a slew of `jitted-XXXX-N.so` files into the working directory as well; these are ELF images covering every JIT trampoline Python generated.

Warning

With `--call-graph dwarf` in play, the `perf` tool grabs snapshots of the profiled process's stack and records them in the `perf.data` file. The stack dump defaults to 8192 bytes, though you can adjust it by appending the value after a comma, as in `--call-graph dwarf,16384`.

That stack-dump size matters: set it too small and `perf` can't unwind the stack, leaving the output incomplete; set it too large and `perf` can no longer sample the process as often as it would prefer, because overhead climbs.

The stack size becomes especially relevant when you profile Python code built at low optimization levels such as `-O0`, since those builds tend to produce bigger stack frames. If you've compiled Python with `-O0` and your profiling output shows no Python functions, bump the stack dump size up to its ceiling of 65528 bytes:

```shell
$ perf record -F 9999 -g -k 1 --call-graph dwarf,65528 -o perf.data python -Xperf_jit my_script.py

```

Your choice of compilation flags can sway stack sizes a great deal:

- A `-O0` build usually carries far bigger stack frames than one done at `-O1` or above

- Turning on optimizations (`-O1`, `-O2`, and so on) tends to shrink the stack size

- Frame pointers (`-fno-omit-frame-pointer`) as a rule make stack unwinding more dependable

[Subject index](INDEX.md) · [Previous source context](how-to-obtain-the-best-results.md) · [Following source context](../how-to-port-python-2-code-to-python-3/how-to-port-python-2-code-to-python-3.md)
