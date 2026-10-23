# Python Runtime Services - Section introduction and initial examples

### Python Runtime Services

The modules laid out in this chapter deliver a broad span of services tied to the Python interpreter and how it interacts with its environment. A quick rundown follows:

- [`sys` - System-specific parameters and functions](https://docs.python.org/3.14/library/sys.html)
- [`sys.monitoring` - Execution event monitoring](https://docs.python.org/3.14/library/sys.monitoring.html)
  - [Tool identifiers](https://docs.python.org/3.14/library/sys.monitoring.html#tool-identifiers)
    - [Registering and using tools](https://docs.python.org/3.14/library/sys.monitoring.html#registering-and-using-tools)

  - [Events](https://docs.python.org/3.14/library/sys.monitoring.html#events)
    - [Local events](https://docs.python.org/3.14/library/sys.monitoring.html#local-events)
    - [Deprecated event](https://docs.python.org/3.14/library/sys.monitoring.html#deprecated-event)
    - [Ancillary events](https://docs.python.org/3.14/library/sys.monitoring.html#ancillary-events)
    - [Other events](https://docs.python.org/3.14/library/sys.monitoring.html#other-events)
    - [The STOP_ITERATION event](https://docs.python.org/3.14/library/sys.monitoring.html#the-stop-iteration-event)

  - [Turning events on and off](https://docs.python.org/3.14/library/sys.monitoring.html#turning-events-on-and-off)
    - [Setting events globally](https://docs.python.org/3.14/library/sys.monitoring.html#setting-events-globally)
    - [Per code object events](https://docs.python.org/3.14/library/sys.monitoring.html#per-code-object-events)
    - [Disabling events](https://docs.python.org/3.14/library/sys.monitoring.html#disabling-events)

  - [Registering callback functions](https://docs.python.org/3.14/library/sys.monitoring.html#registering-callback-functions)
    - [Callback function arguments](https://docs.python.org/3.14/library/sys.monitoring.html#callback-function-arguments)

- [`sysconfig` - Provide access to Python's configuration information](https://docs.python.org/3.14/library/sysconfig.html)
  - [Configuration variables](https://docs.python.org/3.14/library/sysconfig.html#configuration-variables)
  - [Installation paths](https://docs.python.org/3.14/library/sysconfig.html#installation-paths)
  - [User scheme](https://docs.python.org/3.14/library/sysconfig.html#user-scheme)
    - [`posix_user`](https://docs.python.org/3.14/library/sysconfig.html#posix-user)
    - [`nt_user`](https://docs.python.org/3.14/library/sysconfig.html#nt-user)
    - [`osx_framework_user`](https://docs.python.org/3.14/library/sysconfig.html#osx-framework-user)

  - [Home scheme](https://docs.python.org/3.14/library/sysconfig.html#home-scheme)
    - [`posix_home`](https://docs.python.org/3.14/library/sysconfig.html#posix-home)

  - [Prefix scheme](https://docs.python.org/3.14/library/sysconfig.html#prefix-scheme)
    - [`posix_prefix`](https://docs.python.org/3.14/library/sysconfig.html#posix-prefix)
    - [`nt`](https://docs.python.org/3.14/library/sysconfig.html#nt)

  - [Installation path functions](https://docs.python.org/3.14/library/sysconfig.html#installation-path-functions)
  - [Other functions](https://docs.python.org/3.14/library/sysconfig.html#other-functions)
  - [Command-line usage](https://docs.python.org/3.14/library/sysconfig.html#command-line-usage)

- [`builtins` - Built-in objects](https://docs.python.org/3.14/library/builtins.html)
- [`__main__` - Top-level code environment](https://docs.python.org/3.14/library/__main__.html)
  - [`__name__ == '__main__'`](https://docs.python.org/3.14/library/__main__.html#name-main)
    - [What is the "top-level code environment"?](https://docs.python.org/3.14/library/__main__.html#what-is-the-top-level-code-environment)
    - [Idiomatic Usage](https://docs.python.org/3.14/library/__main__.html#idiomatic-usage)
    - [Packaging Considerations](https://docs.python.org/3.14/library/__main__.html#packaging-considerations)

  - [`__main__.py` in Python Packages](https://docs.python.org/3.14/library/__main__.html#main-py-in-python-packages)
    - [Idiomatic Usage](https://docs.python.org/3.14/library/__main__.html#id1)

  - [`import __main__`](https://docs.python.org/3.14/library/__main__.html#import-main)

- [`warnings` - Warning control](https://docs.python.org/3.14/library/warnings.html)
  - [Warning Categories](https://docs.python.org/3.14/library/warnings.html#warning-categories)
  - [The Warnings Filter](https://docs.python.org/3.14/library/warnings.html#the-warnings-filter)
    - [Repeated Warning Suppression Criteria](https://docs.python.org/3.14/library/warnings.html#repeated-warning-suppression-criteria)
    - [Describing Warning Filters](https://docs.python.org/3.14/library/warnings.html#describing-warning-filters)
    - [Default Warning Filter](https://docs.python.org/3.14/library/warnings.html#default-warning-filter)
    - [Overriding the default filter](https://docs.python.org/3.14/library/warnings.html#overriding-the-default-filter)

  - [Temporarily Suppressing Warnings](https://docs.python.org/3.14/library/warnings.html#temporarily-suppressing-warnings)
  - [Testing Warnings](https://docs.python.org/3.14/library/warnings.html#testing-warnings)
  - [Updating Code For New Versions of Dependencies](https://docs.python.org/3.14/library/warnings.html#updating-code-for-new-versions-of-dependencies)
  - [Available Functions](https://docs.python.org/3.14/library/warnings.html#available-functions)
  - [Available Context Managers](https://docs.python.org/3.14/library/warnings.html#available-context-managers)
  - [Concurrent safety of Context Managers](https://docs.python.org/3.14/library/warnings.html#concurrent-safety-of-context-managers)

- [`dataclasses` - Data Classes](https://docs.python.org/3.14/library/dataclasses.html)
  - [Module contents](https://docs.python.org/3.14/library/dataclasses.html#module-contents)
  - [Post-init processing](https://docs.python.org/3.14/library/dataclasses.html#post-init-processing)
  - [Class variables](https://docs.python.org/3.14/library/dataclasses.html#class-variables)
  - [Init-only variables](https://docs.python.org/3.14/library/dataclasses.html#init-only-variables)
  - [Frozen instances](https://docs.python.org/3.14/library/dataclasses.html#frozen-instances)
  - [Inheritance](https://docs.python.org/3.14/library/dataclasses.html#inheritance)
  - [Re-ordering of keyword-only parameters in `__init__()`](https://docs.python.org/3.14/library/dataclasses.html#re-ordering-of-keyword-only-parameters-in-init)
  - [Default factory functions](https://docs.python.org/3.14/library/dataclasses.html#default-factory-functions)
  - [Mutable default values](https://docs.python.org/3.14/library/dataclasses.html#mutable-default-values)
  - [Descriptor-typed fields](https://docs.python.org/3.14/library/dataclasses.html#descriptor-typed-fields)

[Subject index](INDEX.md) · [Previous](python-runtime-services.md) · [Continue](python-runtime-services.md)
