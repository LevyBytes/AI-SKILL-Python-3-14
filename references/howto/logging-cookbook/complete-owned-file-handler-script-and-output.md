# Complete owned-file handler script and output

Here I assign ownership to the `pulse` user and group, purely as an illustration. Combined into a runnable script, `chowntest.py`:

The complete program is in the [upstream source](https://docs.python.org/3.14/howto/logging-cookbook.html#customizing-handlers-with-dictconfig).

You'll most likely have to run this as `root`:

```shell
$ sudo python3.3 chowntest.py
$ cat chowntest.log
2013-11-05 09:34:51,128 DEBUG mylogger A debug message
$ ls -l chowntest.log
-rw-r--r-- 1 pulse pulse 55 2013-11-05 09:34 chowntest.log

```

[Subject index](INDEX.md) · [Owned-file handler factory and dictConfig schema](owned-file-handler-factory-and-dictconfig-schema.md) · [Handler factory version and external-name configuration](handler-factory-version-and-external-name-configuration.md) · [Previous source context](owned-file-handler-factory-and-dictconfig-schema.md) · [Following source context](handler-factory-version-and-external-name-configuration.md)
