# Multiple handlers and formatters

### Multiple handlers and formatters

Loggers are ordinary Python objects. There is no floor or ceiling on how many handlers the [`addHandler()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.addHandler) method lets you attach. On occasion an application benefits from writing every message at every severity into a text file, while at the same time routing only errors and worse to the console. Achieving that is just a matter of wiring up the right handlers. None of the logging calls in your application code have to change. What follows is a small tweak to the earlier basic module-level configuration example:

```python
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

```

Observe that the 'application' code is indifferent to how many handlers exist. The only difference was wiring in and configuring one extra handler called *fh*.

Being able to spin up extra handlers with stricter or looser severity filters proves quite useful while you build and exercise an application. Rather than scattering `print` statements everywhere to debug, reach for `logger.debug`: those print statements eventually have to be removed or commented out, whereas logger.debug calls can stay put in the source, lying idle until you want them once more. When that moment arrives, the sole adjustment required is bumping the severity of the logger and/or the handler down to debug.

[Subject index](INDEX.md) · [Previous source context](logging-from-multiple-threads.md) · [Following source context](logging-to-multiple-destinations.md)
