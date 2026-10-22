# Build DTrace/SystemTap markers and inspect macOS probes

### Enabling the static markers

DTrace ships natively on macOS. Under Linux, compiling CPython so it carries the embedded SystemTap markers first requires that you install the SystemTap development tooling.

From a Linux box, you can install it with:

```shell
$ yum install systemtap-sdt-devel

```

or:

```shell
$ sudo apt-get install systemtap-sdt-dev

```

You then have to set up CPython by [`configured with the --with-dtrace option`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-dtrace):

```none
checking for --with-dtrace... yes

```

Under macOS, you can enumerate the DTrace probes that exist by launching a Python process in the background and then asking for every probe exposed by the Python provider:

```shell
$ python3.6 -q &
$ sudo dtrace -l -P python$!  # or: dtrace -l -m python3.6

   ID   PROVIDER            MODULE                          FUNCTION NAME
29564 python18035        python3.6          _PyEval_EvalFrameDefault function-entry
29565 python18035        python3.6             dtrace_function_entry function-entry
29566 python18035        python3.6          _PyEval_EvalFrameDefault function-return
29567 python18035        python3.6            dtrace_function_return function-return
29568 python18035        python3.6                           collect gc-done
29569 python18035        python3.6                           collect gc-start
29570 python18035        python3.6          _PyEval_EvalFrameDefault line
29571 python18035        python3.6                 maybe_dtrace_line line

```

[Subject index](INDEX.md) · [Inspect Linux static-marker sections and metadata](inspect-linux-static-marker-sections-and-metadata.md) · [Previous source context](instrumenting-cpython-with-dtrace-and-systemtap.md) · [Following source context](inspect-linux-static-marker-sections-and-metadata.md)
