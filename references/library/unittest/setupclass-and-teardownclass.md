# setUpClass and tearDownClass

### setUpClass and tearDownClass

You have to write these as class methods:

```python
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()

```

Should you need the base classes' `setUpClass` and `tearDownClass` to run, it's on you to invoke them upward yourself; the versions defined in `TestCase` are empty.

Whenever an exception fires during a `setUpClass`, that class's tests stay unrun and its `tearDownClass` is skipped too. Classes that get skipped never have `setUpClass` or `tearDownClass` run at all. And if the exception happens to be a `SkipTest`, the class is logged as skipped rather than as an error.

[Subject index](INDEX.md) · [Previous](class-and-module-fixtures.md) · [Continue](unittest-addmodulecleanup-to-unittest-domodulecleanups.md)
