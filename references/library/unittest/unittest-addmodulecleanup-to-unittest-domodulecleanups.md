# setUpModule and tearDownModule

### setUpModule and tearDownModule

You ought to write these as plain functions:

```python
def setUpModule():
    createConnection()

def tearDownModule():
    closeConnection()

```

Should an exception arise within a `setUpModule`, not one of that module's tests will run, and `tearDownModule` is left unrun as well. Where that exception is a `SkipTest`, the module is logged as skipped in place of being marked an error.

For cleanup code that has to run even when an exception strikes, turn to `addModuleCleanup`:

 unittest.addModuleCleanup(*function*, */*, **args*, ***kwargs*)

Register a function to fire after `tearDownModule()`, releasing resources the test class made use of. These functions fire in the opposite order from how they were registered (LIFO), and they receive whatever positional and keyword arguments you handed to `addModuleCleanup()` at registration time.

Even when `setUpModule()` fails - which means `tearDownModule()` never runs - any cleanup functions you registered still get called.

Added in version 3.8.

 unittest.enterModuleContext(*cm*)

Step into the given [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager). On success, it also registers that manager's [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method as a cleanup function through `addModuleCleanup()`, and hands back whatever the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method produced.

Added in version 3.11.

 unittest.doModuleCleanups()

No matter what, this function runs once `tearDownModule()` has, or right after `setUpModule()` whenever `setUpModule()` throws an exception.

Its job is to invoke every cleanup function that `addModuleCleanup()` registered. Should you want those cleanup functions invoked *prior* to `tearDownModule()`, you are free to call `doModuleCleanups()` on your own.

Working through the cleanup-function stack one method at a time, `doModuleCleanups()` can be called whenever you like.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](setupclass-and-teardownclass.md) · [Continue](unittest-installhandler-to-unittest-removehandler.md)
