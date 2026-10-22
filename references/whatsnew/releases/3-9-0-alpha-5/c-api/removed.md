# Python 3.9.0 alpha 5 / c api / removed

[bpo-39946](https://bugs.python.org/issue?@action=redirect&bpo=39946): Take away the `_PyRuntime.getframe` hook and drop the `_PyThreadState_GetFrame` macro, which aliased `_PyRuntime.getframe`. Only the internal C API exposed them. The `PyThreadFrameGetter` type is removed as well.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
