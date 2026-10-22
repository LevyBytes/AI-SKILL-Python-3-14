# Python 3.13.0 alpha 2 / c api / modules

[gh-109587](https://github.com/python/cpython/issues/109587): Three new entry points arrived: `PyUnstable_PerfTrampoline_CompileCode()`, `PyUnstable_PerfTrampoline_SetPersistAfterFork()` and `PyUnstable_CopyPerfMapFile()`. With them, extension modules can build trampolines up front once the application has "warmed up", which lets perf-trampolines stay on in an always-enabled mode.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
