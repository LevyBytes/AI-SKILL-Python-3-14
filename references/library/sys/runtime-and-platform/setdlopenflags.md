# sys.setdlopenflags

sys.setdlopenflags(*n*)

Set the flags the interpreter applies for `dlopen()` calls, for instance when the interpreter loads extension modules. Among other effects, this enables lazy resolution of symbols while importing a module if it is called as `sys.setdlopenflags(0)`. To share symbols across extension modules, call it as `sys.setdlopenflags(os.RTLD_GLOBAL)`. Symbolic names for the flag values live in the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module (`RTLD_*xxx*` constants, e.g. [`os.RTLD_LAZY`](https://docs.python.org/3.14/library/os.html#os.RTLD_LAZY)).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

[API family](INDEX.md) · [sys context index](../INDEX.md).
