# How to enable `perf` profiling support

### How to enable `perf` profiling support

There are two ways to switch on `perf` profiling support: right from launch, via the [`PYTHONPERFSUPPORT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPERFSUPPORT) environment variable or the [`-X perf`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option, or on the fly through [`sys.activate_stack_trampoline()`](https://docs.python.org/3.14/library/sys.html#sys.activate_stack_trampoline) paired with [`sys.deactivate_stack_trampoline()`](https://docs.python.org/3.14/library/sys.html#sys.deactivate_stack_trampoline).

In terms of precedence, the `sys` functions win out over the `-X` option, and the `-X` option itself outranks the environment variable.

Example, using the environment variable:

```shell
$ PYTHONPERFSUPPORT=1 perf record -F 9999 -g -o perf.data python my_script.py
$ perf report -g -i perf.data

```

Example, using the `-X` option:

```shell
$ perf record -F 9999 -g -o perf.data python -X perf my_script.py
$ perf report -g -i perf.data

```

Example, using the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) APIs in file `example.py`:

```python
import sys

sys.activate_stack_trampoline("perf")
do_profiled_stuff()
sys.deactivate_stack_trampoline()

non_profiled_stuff()

```

…then:

```shell
$ perf record -F 9999 -g -o perf.data python ./example.py
$ perf report -g -i perf.data

```

[Subject index](INDEX.md) · [Previous source context](python-function-perf-report-with-profiling-support.md) · [Following source context](how-to-obtain-the-best-results.md)
