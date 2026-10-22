# Logging to a file

### Logging to a file

Recording logging events into a file is a very frequent scenario, so we'll examine that next. Make sure you attempt the following inside a freshly launched Python interpreter, rather than carrying on from the earlier session:

```python
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

```

Changed in version 3.9: The *encoding* argument was added. With older Python releases, or when it isn't given, the encoding applied is whatever [`open()`](https://docs.python.org/3.14/library/functions.html#open) defaults to. Although the example above omits it, an *errors* argument may now be supplied too, controlling how encoding errors get handled. To learn the permitted values and the default, consult the docs for `open()`.

Now, opening the file to inspect its contents, we ought to see the log messages:

```none
DEBUG:__main__:This message should go to the log file
INFO:__main__:So should this
WARNING:__main__:And this, too
ERROR:__main__:And non-ASCII stuff, too, like Øresund and Malmö

```

This example additionally demonstrates setting the logging level that serves as the cutoff for tracking. Here, since we put the cutoff at `DEBUG`, every one of the messages came through.

Suppose you'd like to read the logging level from a command-line option like:

```none
--log=INFO

```

and the value handed to `--log` lands in some variable *loglevel*; then you can apply:

```python
getattr(logging, loglevel.upper())

```

to obtain the value that you'll then feed into [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) through its *level* argument. It may be wise to validate whatever value the user supplied, perhaps along the lines of the following example:

```python
# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level, ...)

```

You should invoke [`basicConfig()`](https://docs.python.org/3.14/library/logging.html#logging.basicConfig) *before* you call any of a logger's methods, for instance [`debug()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.debug), [`info()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.info), and the rest. If you don't, that logging event might not be processed the way you intended.

When you launch the script above more than once, each run's messages get appended to the file *example.log*. To make every run begin fresh, with no recollection of messages from prior runs, supply the *filemode* argument by altering the call in the example above to:

```python
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

```

You'll get the same output as before, except the log file is no longer appended to, which means the messages from prior runs disappear.

[Subject index](INDEX.md) · [Previous source context](a-simple-example.md) · [Following source context](logging-variable-data.md)
