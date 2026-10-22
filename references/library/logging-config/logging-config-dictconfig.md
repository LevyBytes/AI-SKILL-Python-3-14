# logging.config: `logging.config.dictConfig()`

### Configuration functions

These functions, found in the `logging.config` module, set up the logging module. Using them is not required — logging can be set up either through these helpers or by issuing calls against the primary API (defined within [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) itself) and declaring handlers that live in either `logging` or [`logging.handlers`](https://docs.python.org/3.14/library/logging.handlers.html#module-logging.handlers).

 logging.config.dictConfig(*config*)

Pulls the logging configuration out of a dictionary. What this dictionary should contain is laid out in Configuration dictionary schema below.

Should something go wrong while configuring, the function raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError), [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) or [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) carrying a reasonably descriptive message. Here is a (perhaps not exhaustive) set of situations that trigger an error:

- A `level` that is not a string, or that is a string which doesn't map to a genuine logging level.

- A `propagate` value that is not a boolean.

- An id lacking a matching destination.

- A handler id that does not exist, encountered during an incremental call.

- A logger name that is invalid.

- A failure to resolve to either an internal or external object.

The `DictConfigurator` class handles parsing; its constructor receives the dictionary used for configuration and exposes a `configure()` method. The `logging.config` module carries a callable attribute named `dictConfigClass`, which starts out pointing at `DictConfigurator`. You're free to substitute your own suitable implementation for `dictConfigClass`.

`dictConfig()` invokes `dictConfigClass` with the supplied dictionary, and afterwards runs the `configure()` method on whatever object comes back, thereby applying the configuration:

```python
def dictConfig(config):
    dictConfigClass(config).configure()

```

As an illustration, a subclass of `DictConfigurator` might invoke `DictConfigurator.__init__()` from within its own `__init__()`, and then register custom prefixes for use during the later `configure()` call. You would then bind `dictConfigClass` to this new subclass, after which `dictConfig()` could be invoked precisely as it is in the default, uncustomized scenario.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](logging-config-logging-configuration.md) · [Continue](logging-config-fileconfig-to-logging-config-stoplistening.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
