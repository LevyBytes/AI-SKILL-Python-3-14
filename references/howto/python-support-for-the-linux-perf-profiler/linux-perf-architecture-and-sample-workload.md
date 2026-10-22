# Linux perf support, architecture conditions and sample workload

## Python support for the Linux perf profiler

### Python support for the Linux `perf` profiler

author:

Pablo Galindo

[The Linux perf profiler](https://perf.wiki.kernel.org) is an extremely capable utility for measuring and gathering data on how well your application performs. On top of that, `perf` comes with a thriving collection of companion tools for digging into the data it generates.

Where things get tricky when you point the `perf` profiler at Python applications is that `perf` only sees native symbols — the names of functions and procedures authored in C. As a result, neither the names nor the source files of the Python functions you wrote turn up in the output of `perf`.

From Python 3.12 onward, the interpreter offers a dedicated mode that surfaces Python functions in the `perf` profiler's output. With that mode switched on, before each Python function runs the interpreter slots in a tiny chunk of code generated on the fly, and through that chunk it shows `perf` how the code relates to its corresponding Python function by means of [perf map files](https://docs.python.org/3.14/c-api/perfmaps.html).

Note

At present the `perf` profiler is supported solely on Linux and only on certain architectures. To find out whether yours qualifies, inspect what the `configure` build step prints or look at the result of `python -m sysconfig | grep HAVE_PERF_TRAMPOLINE`.

For example, consider the following script:

```python
def foo(n):
    result = 0
    for _ in range(n):
        result += 1
    return result

def bar(n):
    foo(n)

def baz(n):
    bar(n)

if __name__ == "__main__":
    baz(1000000)

```

We can run `perf` to sample CPU stack traces at 9999 hertz:

```shell
$ perf record -F 9999 -g -o perf.data python my_script.py

```

[Subject index](INDEX.md) · [Native-only perf report without Python support](native-only-perf-report-without-python-support.md) · [Python-function perf report with profiling support](python-function-perf-report-with-profiling-support.md) · [Previous source context](../orientation/overview.md) · [Following source context](native-only-perf-report-without-python-support.md)
