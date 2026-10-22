# What happens if no configuration is provided

### What happens if no configuration is provided

When logging has not been configured at all, you can end up in a state where a logging event must be emitted yet no handlers exist to emit it.

Under such circumstances the event goes out through a 'handler of last resort', held in [`lastResort`](https://docs.python.org/3.14/library/logging.html#logging.lastResort). This built-in handler belongs to no logger and behaves like a [`StreamHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.StreamHandler) that writes the event's description message to whatever `sys.stderr` currently points at (so it honors any redirections in force). The message receives no formatting - only the plain event description message gets printed. Since the handler's level is `WARNING`, every event at that severity or above will be emitted.

Changed in version 3.2: In Python releases before 3.2, the behaviour was the following:

- When [`raiseExceptions`](https://docs.python.org/3.14/library/logging.html#logging.raiseExceptions) is `False` (production mode), the event simply gets dropped without notice.

- When [`raiseExceptions`](https://docs.python.org/3.14/library/logging.html#logging.raiseExceptions) is `True` (development mode), this text - 'No handlers could be found for logger X.Y.Z' - appears just once.

To get back the pre-3.2 behaviour, set [`lastResort`](https://docs.python.org/3.14/library/logging.html#logging.lastResort) to `None`.

[Subject index](INDEX.md) · [Previous source context](existing-logger-caveats-and-dictconfig-yaml-schema.md) · [Following source context](configuring-logging-for-a-library.md)
