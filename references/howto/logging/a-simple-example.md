# A simple example

### A simple example

Here is a very basic example:

```python
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

```

Enter these lines into a script and execute it, and the result you'll get is:

```none
WARNING:root:Watch out!

```

printed out on the console. Since the default level sits at `WARNING`, the `INFO` message is absent. The text that prints carries both the level indicator and the event description that the logging call supplied, namely ‘Watch out!’. Should you require it, the real output can be shaped quite flexibly; the formatting choices will be covered further on.

Observe that here we call functions on the `logging` module itself, such as `logging.debug`, instead of building a logger and invoking its methods. Such functions act on the root logger, yet they can be handy because they will invoke [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) on your behalf if it hasn't run yet, as happens here. That said, in bigger programs you'll typically prefer to manage the logging setup yourself - and for that reason among others, creating loggers and invoking their methods is the better path.

[Subject index](INDEX.md) · [Previous source context](when-to-use-logging.md) · [Following source context](logging-to-a-file.md)
