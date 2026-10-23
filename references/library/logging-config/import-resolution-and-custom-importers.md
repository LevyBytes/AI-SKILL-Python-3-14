# logging.config - Import resolution and custom importers

### Import resolution and custom importers

By default, import resolution leans on the builtin [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function to carry out its imports. Perhaps you would rather swap in your own importing mechanism: in that case you can overwrite the `importer` attribute of the `DictConfigurator`, or of its parent, the `BaseConfigurator` class. Tread carefully, though, owing to how functions are reached from classes by way of descriptors. When you employ a Python callable for your imports and intend to define it at class level instead of instance level, you must wrap it in [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod). For instance:

```python
from importlib import import_module
from logging.config import BaseConfigurator

BaseConfigurator.importer = staticmethod(import_module)

```

Wrapping in [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) is unnecessary when you assign the import callable on a configurator *instance*.

[Subject index](INDEX.md) · [Previous](access-to-internal-objects.md) · [Continue](configuring-queuehandler-and-queuelistener.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
