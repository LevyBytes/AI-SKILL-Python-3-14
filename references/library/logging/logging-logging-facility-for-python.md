# logging — `logging` — Logging facility for Python

### `logging` — Logging facility for Python

**Source code:** [Lib/logging/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/logging/__init__.py)

---

Functions and classes that build a flexible event logging system for applications and libraries are defined in this module.

The chief advantage of the logging API living in a standard library module is that every Python module can take part in logging, so that your application log can carry your own messages woven together with messages coming from third-party modules.

Here’s a simple example of idiomatic usage:

```python
# myapp.py
import logging
import mylib
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()

```

```python
# mylib.py
import logging
logger = logging.getLogger(__name__)

def do_something():
    logger.info('Doing something')

```

Running *myapp.py* should leave you with this inside *myapp.log*:

```none
INFO:__main__:Started
INFO:mylib:Doing something
INFO:__main__:Finished

```

What makes this idiomatic usage stand out is that most of the code merely builds a module level logger via `getLogger(__name__)` and then uses that logger for whatever logging is required. It stays concise while still granting downstream code fine-grained control where that's wanted. Messages logged to the module-level logger are forwarded on to the handlers of loggers belonging to higher-level modules, right up to the topmost logger called the root logger; this scheme goes by the name hierarchical logging.

To be of any use, logging has to be configured: you set the levels and destinations for each logger, perhaps tweaking how particular modules log, frequently driven by command-line arguments or application configuration. As a rule, in cases like the one above, only the root logger has to be configured this way, since every lower-level logger at module level winds up forwarding its messages to that logger's handlers. `basicConfig()` offers a fast route to configuring the root logger, which covers a great many use cases.

There's plenty of functionality and flexibility on offer in the module. Should logging be new to you, the best path to getting comfortable with it is to read through the tutorials (**see the links above and on the right**).

The module's basic classes, alongside their attributes and methods, are enumerated in the sections that follow.

- Loggers present the interface that application code makes direct use of.

- Handlers route the log records (which loggers create) to the fitting destination.

- Filters supply a more fine-grained means of deciding which log records get output.

- Formatters dictate how log records are laid out in the final output.

[Subject index](INDEX.md) · [Continue](logging-logger-class.md)
