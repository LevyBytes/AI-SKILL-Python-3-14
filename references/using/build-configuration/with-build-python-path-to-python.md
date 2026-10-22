# --with-build-python=path/to/python

--with-build-python=path/to/python

path to the build `python` binary used for cross compiling

Added in version 3.11.

 CONFIG_SITE=file

An environment variable naming a file that holds configure overrides.

A sample *config.site* file:

```ini
# config.site-aarch64
ac_cv_buggy_getaddrinfo=no
ac_cv_file__dev_ptmx=yes
ac_cv_file__dev_ptc=no

```

[Subject index](INDEX.md) · [Previous source section](host-host.md) · [Following source section](hostrunner.md)
