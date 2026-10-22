# Python 3.12.0 alpha 4 / build / platform

[gh-100540](https://github.com/python/cpython/issues/100540): The `--with-system-ffi` `configure` option was removed; on every non-Windows platform the system must now always provide `libffi`. For several releases the option had no impact on non-Darwin platforms, and in 3.11 its only obscure behavior was to run `pkg-config` to locate `libffi` while never defining `-DUSING_APPLE_OS_LIBFFI`. On Darwin, `configure` will now look first for the OS `libffi` and otherwise fall back to the same handling as the other platforms.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
