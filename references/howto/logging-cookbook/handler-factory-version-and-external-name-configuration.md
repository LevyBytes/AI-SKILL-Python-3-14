# Handler factory version and external-name configuration

Note that Python 3.3 is used in this example because that release introduced [`shutil.chown()`](https://docs.python.org/3.14/library/shutil.html#shutil.chown). The technique ought to function on any Python release providing [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) - that is, Python 2.7, 3.2 or later. On versions before 3.3, you'd have to carry out the actual ownership change yourself using, for example, [`os.chown()`](https://docs.python.org/3.14/library/os.html#os.chown).

Realistically, the function that builds the handler might sit in some utility module within your project. Rather than this line in the configuration:

```python
'()': owned_file_handler,

```

you might instead write, for example:

```python
'()': 'ext://project.util.owned_file_handler',

```

where you replace `project.util` with the real name of the package holding the function. In the runnable script above, `'ext://__main__.owned_file_handler'` ought to work. At this point [`dictConfig()`](https://docs.python.org/3.14/library/logging.config.html#logging.config.dictConfig) resolves the genuine callable from the `ext://` specification.

This example hopefully also suggests how you might carry out other kinds of file change - say, setting particular POSIX permission bits - in the same fashion, via [`os.chmod()`](https://docs.python.org/3.14/library/os.html#os.chmod).

Naturally, the same idea also stretches to handler types beyond a [`FileHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.FileHandler) - for instance, one of the rotating file handlers, or an entirely different kind of handler.

[Subject index](INDEX.md) · [Owned-file handler factory and dictConfig schema](owned-file-handler-factory-and-dictconfig-schema.md) · [Complete owned-file handler script and output](complete-owned-file-handler-script-and-output.md) · [Previous source context](complete-owned-file-handler-script-and-output.md) · [Following source context](application-wide-logging-format-styles.md)
