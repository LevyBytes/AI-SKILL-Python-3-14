# Python 3.5.4 release candidate 1 / library / exceptions and tracebacks

[bpo-29692](https://bugs.python.org/issue?@action=redirect&bpo=29692): Repaired the arbitrary unchaining of RuntimeError exceptions within contextlib.contextmanager. Siddharth Velankar contributed the patch.

[bpo-28699](https://bugs.python.org/issue?@action=redirect&bpo=28699): Repaired a defect in the pools of multiprocessing.pool whereby an exception thrown at the very start of an iterable might swallow that exception or leave the program hanging. Davin Potts and Xiang Zhang wrote the patch.

[bpo-29615](https://bugs.python.org/issue?@action=redirect&bpo=29615): SimpleXMLRPCDispatcher no longer chains KeyError (nor any other exception) onto the exception(s) thrown within the dispatched methods. Petr Motejlek contributed the patch.

[bpo-29960](https://bugs.python.org/issue?@action=redirect&bpo=29960): Keep generator state intact when _random.Random.setstate() throws an exception. Bryan Olson contributed the patch.

[bpo-30185](https://bugs.python.org/issue?@action=redirect&bpo=30185): Steer clear of KeyboardInterrupt tracebacks inside the forkserver helper process whenever Ctrl-C arrives.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
