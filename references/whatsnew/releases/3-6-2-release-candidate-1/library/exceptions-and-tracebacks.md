# Python 3.6.2 release candidate 1 / library / exceptions and tracebacks

[bpo-30185](https://bugs.python.org/issue?@action=redirect&bpo=30185): Prevent KeyboardInterrupt tracebacks from appearing in the forkserver helper process whenever Ctrl-C arrives.

[bpo-29692](https://bugs.python.org/issue?@action=redirect&bpo=29692): Stopped the arbitrary unchaining of RuntimeError exceptions within contextlib.contextmanager. Siddharth Velankar wrote the patch.

[bpo-28699](https://bugs.python.org/issue?@action=redirect&bpo=28699): Repaired a defect within the pools of multiprocessing.pool whereby raising an exception right at the start of an iterable could either swallow that exception or leave the program hanging. Davin Potts and Xiang Zhang contributed the patch.

[bpo-29615](https://bugs.python.org/issue?@action=redirect&bpo=29615): Whenever exception(s) are raised within the dispatched methods, SimpleXMLRPCDispatcher no longer chains a KeyError (nor any other exception) onto them. Petr Motejlek wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
