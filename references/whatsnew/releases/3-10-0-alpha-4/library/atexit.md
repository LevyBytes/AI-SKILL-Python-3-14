# Python 3.10.0 alpha 4 / library / atexit

[bpo-42639](https://bugs.python.org/issue?@action=redirect&bpo=42639): During interpreter shutdown, when a callback that was registered via [`atexit.register()`](https://docs.python.org/3.14/library/atexit.html#atexit.register) fails, its exception is now recorded. Beforehand only certain exceptions got logged, and the final one was always dropped quietly.

[bpo-42639](https://bugs.python.org/issue?@action=redirect&bpo=42639): Moved the [`atexit`](https://docs.python.org/3.14/library/atexit.html#module-atexit) module state to a per-interpreter model. Keeping several `atexit` module instances around is now safe. Donghee Na and Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
