# Python 3.9.0 alpha 1 / library / faulthandler

[bpo-37851](https://bugs.python.org/issue?@action=redirect&bpo=37851): The [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) module no longer reserves its alternative stack during Python startup. The stack is now reserved only when faulthandler is first used.

[bpo-21131](https://bugs.python.org/issue?@action=redirect&bpo=21131): Fixed the `faulthandler.register(chain=True)` stack. faulthandler now reserves a dedicated stack of `SIGSTKSZ*2` bytes in place of merely `SIGSTKSZ` bytes. On certain platforms, invoking the prior signal handler from within the faulthandler signal handler consumes more than `SIGSTKSZ` bytes of stack memory.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
