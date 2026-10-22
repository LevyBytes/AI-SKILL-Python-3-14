# Python 3.13.0 beta 1 / core and builtins / build and platforms

[gh-118518](https://github.com/python/cpython/issues/118518): Permit Linux perf support to function without frame pointers by leaning on perf's advanced JIT support. You switch the feature on via the `PYTHON_PERF_JIT_SUPPORT` environment variable or by launching Python with `-Xperf_jit`. Pablo Galindo wrote the patch.

[gh-118335](https://github.com/python/cpython/issues/118335): Alter the way the tier 2 interpreter gets selected. Rather than launching Python with `-X uops` or assigning the environment variable `PYTHON_UOPS=1`, the decision now happens at build time by configuring through `--enable-experimental-jit=interpreter`.

**Beware!** This shifts the environment variable that enables or disables micro-ops to `PYTHON_JIT`. The former `PYTHON_UOPS` no longer has any effect.

[gh-116622](https://github.com/python/cpython/issues/116622): Forward stdout and stderr into the system log whenever embedded within an Android app.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
