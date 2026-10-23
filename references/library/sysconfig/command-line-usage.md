# sysconfig - Command-line usage

### Command-line usage

`sysconfig` can be run as a script through Python's *-m* option:

```shell
$ python -m sysconfig
Platform: "macosx-10.4-i386"
Python version: "3.2"
Current installation scheme: "posix_prefix"

Paths:
        data = "/usr/local"
        include = "/Users/tarek/Dev/svn.python.org/py3k/Include"
        platinclude = "."
        platlib = "/usr/local/lib/python3.2/site-packages"
        platstdlib = "/usr/local/lib/python3.2"
        purelib = "/usr/local/lib/python3.2/site-packages"
        scripts = "/usr/local/bin"
        stdlib = "/usr/local/lib/python3.2"

Variables:
        AC_APPLE_UNIVERSAL_BUILD = "0"
        AIX_GENUINE_CPLUSPLUS = "0"
        AR = "ar"
        ARFLAGS = "rc"
        ...

```

Running it sends to standard output the information that `get_platform()`, `get_python_version()`, `get_path()` and `get_config_vars()` produce.

[Subject index](INDEX.md) · [Previous](python-version-platform-and-makefile-queries.md) · [Continue](../syslog/syslog-syslog-to-syslog-log-debug.md) · [Owning module, declaration or section: sysconfig](python-configuration-access-overview.md)
