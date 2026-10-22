# Python-function perf report with profiling support

If, on the other hand, we repeat the experiment with `perf` support turned on, the result becomes:

```shell
$ perf report --stdio -n -g

# Children      Self       Samples  Command     Shared Object       Symbol
# ........  ........  ............  ..........  ..................  .....................................................................
#
    90.58%     0.36%             1  python.exe  python.exe          [.] _start
            |
            ---_start
            |
                --89.86%--__libc_start_main
                        Py_BytesMain
                        |
                        |--55.43%--pymain_run_python.constprop.0
                        |          |
                        |          |--54.71%--_PyRun_AnyFileObject
                        |          |          _PyRun_SimpleFileObject
                        |          |          |
                        |          |          |--53.62%--run_mod
                        |          |          |          |
                        |          |          |           --53.26%--PyEval_EvalCode
                        |          |          |                     py::<module>:/src/script.py
                        |          |          |                     _PyEval_EvalFrameDefault
                        |          |          |                     PyObject_Vectorcall
                        |          |          |                     _PyEval_Vector
                        |          |          |                     py::baz:/src/script.py
                        |          |          |                     _PyEval_EvalFrameDefault
                        |          |          |                     PyObject_Vectorcall
                        |          |          |                     _PyEval_Vector
                        |          |          |                     py::bar:/src/script.py
                        |          |          |                     _PyEval_EvalFrameDefault
                        |          |          |                     PyObject_Vectorcall
                        |          |          |                     _PyEval_Vector
                        |          |          |                     py::foo:/src/script.py
                        |          |          |                     |
                        |          |          |                     |--51.81%--_PyEval_EvalFrameDefault
                        |          |          |                     |          |
                        |          |          |                     |          |--13.77%--_PyLong_Add
                        |          |          |                     |          |          |
                        |          |          |                     |          |          |--3.26%--_PyObject_Malloc

```

[Subject index](INDEX.md) · [Linux perf support, architecture conditions and sample workload](linux-perf-architecture-and-sample-workload.md) · [Native-only perf report without Python support](native-only-perf-report-without-python-support.md) · [Previous source context](native-only-perf-report-without-python-support.md) · [Following source context](how-to-enable-perf-profiling-support.md)
