# Python 3.5.2 release candidate 1 / library / functions and types

[bpo-25447](https://bugs.python.org/issue?@action=redirect&bpo=25447): Copying the lru_cache() wrapper object now succeeds in every case, regardless of the wrapped object's type, since the original object is returned unchanged.

[bpo-25691](https://bugs.python.org/issue?@action=redirect&bpo=25691): Stopped a crash triggered when removing ElementTree.Element attributes.

[bpo-26050](https://bugs.python.org/issue?@action=redirect&bpo=26050): A fresh asyncio.StreamReader.readuntil() method was added. Марк Коренберг wrote the patch.

[bpo-27040](https://bugs.python.org/issue?@action=redirect&bpo=27040): Introduced a loop.get_exception_handler method

[bpo-26977](https://bugs.python.org/issue?@action=redirect&bpo=26977): Eliminated an unneeded and ignored call to the sum-of-squares helper inside statistics.pvariance.

[bpo-26711](https://bugs.python.org/issue?@action=redirect&bpo=26711): The comparison of plistlib.Data against other types has been fixed.

[bpo-26733](https://bugs.python.org/issue?@action=redirect&bpo=26733): Disassembling a class now also disassembles its class and static methods. Xiang Zhang contributed the patch.

[bpo-26457](https://bugs.python.org/issue?@action=redirect&bpo=26457): Correct the subnets() methods of the IP network classes for the situation where the resulting prefix length matches the maximal prefix length. Xiang Zhang's patch served as the basis.

[bpo-26186](https://bugs.python.org/issue?@action=redirect&bpo=26186): Remove an invalid type check from importlib.util.LazyLoader.

[bpo-26202](https://bugs.python.org/issue?@action=redirect&bpo=26202): copy.deepcopy() now correctly duplicates range() objects whose attributes are non-atomic.

[bpo-23804](https://bugs.python.org/issue?@action=redirect&bpo=23804): Correct the SSL recv(0) and read(0) methods so they yield zero bytes rather than as many as 1024.

[bpo-26616](https://bugs.python.org/issue?@action=redirect&bpo=26616): A bug inside the datetime.astimezone() method has been fixed.

[bpo-26177](https://bugs.python.org/issue?@action=redirect&bpo=26177): The keys() method on Canvas and Scrollbar widgets has been fixed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
