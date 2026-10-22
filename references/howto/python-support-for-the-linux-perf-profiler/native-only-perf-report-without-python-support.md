# Native-only perf report without Python support

Then we can use `perf report` to analyze the data:

```shell
$ perf report --stdio -n -g

# Children      Self       Samples  Command     Shared Object       Symbol
# ........  ........  ............  ..........  ..................  ..........................................
#
    91.08%     0.00%             0  python.exe  python.exe          [.] _start
            |
            ---_start
            |
                --90.71%--__libc_start_main
                        Py_BytesMain
                        |
                        |--56.88%--pymain_run_python.constprop.0
                        |          |
                        |          |--56.13%--_PyRun_AnyFileObject
                        |          |          _PyRun_SimpleFileObject
                        |          |          |
                        |          |          |--55.02%--run_mod
                        |          |          |          |
                        |          |          |           --54.65%--PyEval_EvalCode
                        |          |          |                     _PyEval_EvalFrameDefault
                        |          |          |                     PyObject_Vectorcall
                        |          |          |                     _PyEval_Vector
                        |          |          |                     _PyEval_EvalFrameDefault
                        |          |          |                     PyObject_Vectorcall
                        |          |          |                     _PyEval_Vector
                        |          |          |                     _PyEval_EvalFrameDefault
                        |          |          |                     PyObject_Vectorcall
                        |          |          |                     _PyEval_Vector
                        |          |          |                     |
                        |          |          |                     |--51.67%--_PyEval_EvalFrameDefault
                        |          |          |                     |          |
                        |          |          |                     |          |--11.52%--_PyLong_Add
                        |          |          |                     |          |          |
                        |          |          |                     |          |          |--2.97%--_PyObject_Malloc
...

```

Notice that none of the Python functions appear here — the only thing listed is `_PyEval_EvalFrameDefault`, which is the function that evaluates the Python bytecode. That isn't much help, since every Python function relies on the very same C function for bytecode evaluation, leaving us no way to tell which Python function goes with which bytecode-evaluating call.

[Subject index](INDEX.md) · [Linux perf support, architecture conditions and sample workload](linux-perf-architecture-and-sample-workload.md) · [Python-function perf report with profiling support](python-function-perf-report-with-profiling-support.md) · [Previous source context](linux-perf-architecture-and-sample-workload.md) · [Following source context](python-function-perf-report-with-profiling-support.md)
