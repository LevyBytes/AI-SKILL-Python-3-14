# sys.modules

sys.modules

This is a dictionary mapping module names to the modules that have already been loaded. You can manipulate it to force modules to reload along with other tricks. That said, swapping out the dictionary will not necessarily behave the way you expect, and removing critical items from it may make Python fail. When you want to walk over this global dictionary, always reach for `sys.modules.copy()` or `tuple(sys.modules)` so you avoid exceptions, since its size can change mid-iteration as a side effect of code or activity running in other threads.

[API family](INDEX.md) · [sys context index](../INDEX.md).
