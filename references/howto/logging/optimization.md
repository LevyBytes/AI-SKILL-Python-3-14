# Optimization

### Optimization

The logging machinery holds off on formatting message arguments right up to the point where it has no choice. Even so, working out the arguments you feed to the logging call can itself be costly, and you might prefer to skip that work when the logger is only going to discard the event anyway. To make that call, invoke the [`isEnabledFor()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.isEnabledFor) method, which accepts a level argument and yields true whenever the Logger would in fact produce the event at that level. Code along these lines does the trick:

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Message with %s, %s', expensive_func1(),
                                        expensive_func2())

```

so that whenever the logger's threshold sits higher than `DEBUG`, neither `expensive_func1` nor `expensive_func2` ever gets called.

Note

Now and then, [`isEnabledFor()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.isEnabledFor) may cost more than you would like on its own — say, with deeply nested loggers whose explicit level is fixed only near the top of the logger hierarchy. When that happens (or if you simply want to keep method calls out of tight loops), stash the outcome of an `isEnabledFor()` call in a local or instance variable and consult that rather than re-invoking the method every pass. You would only have to recompute that stored value if the logging configuration shifts on the fly while the program runs, and that rarely happens.

Further tuning is available for particular programs that demand tighter say over which logging details get gathered. The list that follows covers steps you can take to skip the logging work you have no use for:

| What you don’t want to collect | How to avoid collecting it |
| --- | --- |
| Details on the location a call originated from. | Assign `None` to `logging._srcfile`. Doing so sidesteps any `sys._getframe()` call, which can accelerate your program under runtimes such as PyPy (it cannot optimize code relying on `sys._getframe()`). |
| Thread-related details. | Assign `False` to `logging.logThreads`. |
| The active process ID (`os.getpid()`) | Assign `False` to `logging.logProcesses`. |
| The active process name where `multiprocessing` is driving several processes. | Assign `False` to `logging.logMultiprocessing`. |
| The active `asyncio.Task` name where `asyncio` is in play. | Assign `False` to `logging.logAsyncioTasks`. |

Bear in mind too that the central logging module bundles only the basic handlers. As long as you never import [`logging.handlers`](https://docs.python.org/3.14/library/logging.handlers.html#module-logging.handlers) or [`logging.config`](https://docs.python.org/3.14/library/logging.config.html#module-logging.config), neither one consumes any memory.

[Subject index](INDEX.md) · [Logging arbitrary objects as messages](logging-arbitrary-objects-as-messages.md) · [Following source context](logging-arbitrary-objects-as-messages.md) · [Previous source context](logging-arbitrary-objects-as-messages.md) · [Following source context](other-resources.md)
