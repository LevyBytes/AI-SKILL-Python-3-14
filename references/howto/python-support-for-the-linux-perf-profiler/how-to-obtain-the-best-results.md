# How to obtain the best results

### How to obtain the best results

To get the best outcome, build Python with `CFLAGS="-fno-omit-frame-pointer -mno-omit-leaf-frame-pointer"`, since that lets profilers walk the stack using the frame pointer alone rather than leaning on DWARF debug information. The reason is that the on-the-fly generated code inserted to enable `perf` support carries no DWARF debugging information of its own.

To confirm whether your system was built with that flag, run:

```shell
$ python -m sysconfig | grep 'no-omit-frame-pointer'

```

Should nothing print, that tells you the interpreter was built without frame pointers, and as a consequence it may be unable to display Python functions within the `perf` output.

[Subject index](INDEX.md) · [Previous source context](how-to-enable-perf-profiling-support.md) · [Following source context](how-to-work-without-frame-pointers.md)
