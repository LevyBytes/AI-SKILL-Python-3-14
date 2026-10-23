# logging.config - Configuring QueueHandler and QueueListener

### Configuring QueueHandler and QueueListener

Should you wish to configure a [`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler) — bearing in mind that it usually goes hand in hand with a [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) — you are able to set up the two at once. Once configured, the `QueueListener` instance can be reached as the [`listener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler.listener) attribute on the handler that was created, and that handler in turn is reachable through [`getHandlerByName()`](https://docs.python.org/3.14/library/logging.html#logging.getHandlerByName) by handing it the name you assigned the `QueueHandler` in your configuration. The YAML snippet below presents the dictionary schema for configuring the pair.

```yaml
handlers:
  qhand:
    class: logging.handlers.QueueHandler
    queue: my.module.queue_factory
    listener: my.package.CustomListener
    handlers:
      - hand_name_1
      - hand_name_2
      ...

```

The `queue` and `listener` keys are optional.

When the `queue` key shows up, its accompanying value may take any of these forms:

- An object that provides the [`Queue.put_nowait`](https://docs.python.org/3.14/library/queue.html#queue.Queue.put_nowait) and [`Queue.get`](https://docs.python.org/3.14/library/queue.html#queue.Queue.get) public API. This might, for example, be a genuine instance of [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue), a subclass of it, or a proxy returned by [`multiprocessing.managers.SyncManager.Queue()`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.managers.SyncManager.Queue).

Naturally, this only works when you are building or altering the configuration dictionary in code.

- A string that resolves to a callable which hands back the queue instance to use when invoked with no arguments. Such a callable might be a [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) subclass or a function that yields a fitting queue instance, like `my.module.queue_factory()`.

- A dict carrying a `'()'` key, built in the customary manner covered under User-defined objects. Whatever that construction produces ought to be a [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) instance.

Where the `queue` key is missing, an ordinary unbounded [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) instance gets created and put to use.

Where the `listener` key appears, its value is allowed to be any one of the following:

- A subclass of [`logging.handlers.QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener). This too is feasible solely when you assemble or change the configuration dictionary in code.

- A string resolving to some class that subclasses `QueueListener` — for example `'my.package.CustomListener'`.

- A dict featuring a `'()'` key, assembled in the standard fashion described under User-defined objects. The outcome of that assembly should be a callable whose signature matches the `QueueListener` initializer.

When the `listener` key is missing, [`logging.handlers.QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener) is what gets used.

Whatever values sit beneath the `handlers` key are the names of further handlers in the configuration (not depicted in the snippet above) that will be forwarded to the queue listener.

Every custom queue handler and listener class has to be declared with the same initialization signatures as [`QueueHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueHandler) and [`QueueListener`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.QueueListener).

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](import-resolution-and-custom-importers.md) · [Continue](logging-file-configuration-overview.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md)
