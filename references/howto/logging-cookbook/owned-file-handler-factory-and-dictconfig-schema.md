# Owned-file handler factory and dictConfig schema

### Customizing handlers with [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig)

Sometimes you'll want to tailor logging handlers in specific ways, and reaching for [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) can let you accomplish this without subclassing. For instance, suppose you'd like to assign the ownership of a log file. That's simple on POSIX via [`shutil.chown()`](https://docs.python.org/3.14/library/shutil.html#shutil.chown), yet the stdlib file handlers ship no built-in support for it. You can tailor how a handler gets created with an ordinary function such as:

```python
def owned_file_handler(filename, mode='a', encoding=None, owner=None):
    if owner:
        if not os.path.exists(filename):
            open(filename, 'a').close()
        shutil.chown(filename, *owner)
    return logging.FileHandler(filename, mode, encoding)

```

Then, within a logging configuration handed to [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig), you can declare that a logging handler should be built by invoking this function:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'file':{
            # The values below are popped from this dictionary and
            # used to create the handler, set the handler's level and
            # its formatter.
            '()': owned_file_handler,
            'level':'DEBUG',
            'formatter': 'default',
            # The values below are passed to the handler creator callable
            # as keyword arguments.
            'owner': ['pulse', 'pulse'],
            'filename': 'chowntest.log',
            'mode': 'w',
            'encoding': 'utf-8',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

```

[Subject index](INDEX.md) · [Complete owned-file handler script and output](complete-owned-file-handler-script-and-output.md) · [Handler factory version and external-name configuration](handler-factory-version-and-external-name-configuration.md) · [Previous source context](implementing-structured-logging.md) · [Following source context](complete-owned-file-handler-script-and-output.md)
