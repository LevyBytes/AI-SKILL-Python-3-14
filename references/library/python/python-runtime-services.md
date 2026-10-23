# Python Runtime Services??

# Python, Queue

## Overview

This page takes in two areas: Python Runtime Services??, then queue (A synchronized queue class??).

## Python Runtime Services??

- [`contextlib` - Utilities for `with`-statement contexts](https://docs.python.org/3.14/library/contextlib.html)
  - [Utilities](https://docs.python.org/3.14/library/contextlib.html#utilities)
  - [Examples and Recipes](https://docs.python.org/3.14/library/contextlib.html#examples-and-recipes)
    - [Supporting a variable number of context managers](https://docs.python.org/3.14/library/contextlib.html#supporting-a-variable-number-of-context-managers)
    - [Catching exceptions from `__enter__` methods](https://docs.python.org/3.14/library/contextlib.html#catching-exceptions-from-enter-methods)
    - [Cleaning up in an `__enter__` implementation](https://docs.python.org/3.14/library/contextlib.html#cleaning-up-in-an-enter-implementation)
    - [Replacing any use of `try-finally` and flag variables](https://docs.python.org/3.14/library/contextlib.html#replacing-any-use-of-try-finally-and-flag-variables)
    - [Using a context manager as a function decorator](https://docs.python.org/3.14/library/contextlib.html#using-a-context-manager-as-a-function-decorator)

  - [Single use, reusable and reentrant context managers](https://docs.python.org/3.14/library/contextlib.html#single-use-reusable-and-reentrant-context-managers)
    - [Reentrant context managers](https://docs.python.org/3.14/library/contextlib.html#reentrant-context-managers)
    - [Reusable context managers](https://docs.python.org/3.14/library/contextlib.html#reusable-context-managers)

- [`abc` - Abstract Base Classes](https://docs.python.org/3.14/library/abc.html)
- [`atexit` - Exit handlers](https://docs.python.org/3.14/library/atexit.html)
  - [`atexit` Example](https://docs.python.org/3.14/library/atexit.html#atexit-example)

- [`traceback` - Print or retrieve a stack traceback](https://docs.python.org/3.14/library/traceback.html)
  - [Module-Level Functions](https://docs.python.org/3.14/library/traceback.html#module-level-functions)
  - [`TracebackException` Objects](https://docs.python.org/3.14/library/traceback.html#tracebackexception-objects)
  - [`StackSummary` Objects](https://docs.python.org/3.14/library/traceback.html#stacksummary-objects)
  - [`FrameSummary` Objects](https://docs.python.org/3.14/library/traceback.html#framesummary-objects)
  - [Examples of Using the Module-Level Functions](https://docs.python.org/3.14/library/traceback.html#examples-of-using-the-module-level-functions)
  - [Examples of Using `TracebackException`](https://docs.python.org/3.14/library/traceback.html#examples-of-using-tracebackexception)

- [`__future__` - Future statement definitions](https://docs.python.org/3.14/library/__future__.html)
  - [Module Contents](https://docs.python.org/3.14/library/__future__.html#module-contents)

- [`gc` - Garbage Collector interface](https://docs.python.org/3.14/library/gc.html)
- [`inspect` - Inspect live objects](https://docs.python.org/3.14/library/inspect.html)
  - [Types and members](https://docs.python.org/3.14/library/inspect.html#types-and-members)
  - [Retrieving source code](https://docs.python.org/3.14/library/inspect.html#retrieving-source-code)
  - [Introspecting callables with the Signature object](https://docs.python.org/3.14/library/inspect.html#introspecting-callables-with-the-signature-object)
  - [Classes and functions](https://docs.python.org/3.14/library/inspect.html#classes-and-functions)
  - [The interpreter stack](https://docs.python.org/3.14/library/inspect.html#the-interpreter-stack)
  - [Fetching attributes statically](https://docs.python.org/3.14/library/inspect.html#fetching-attributes-statically)
  - [Current State of Generators, Coroutines, and Asynchronous Generators](https://docs.python.org/3.14/library/inspect.html#current-state-of-generators-coroutines-and-asynchronous-generators)
  - [Code Objects Bit Flags](https://docs.python.org/3.14/library/inspect.html#code-objects-bit-flags)
  - [Buffer flags](https://docs.python.org/3.14/library/inspect.html#buffer-flags)
  - [Command-line interface](https://docs.python.org/3.14/library/inspect.html#command-line-interface)

- [`annotationlib` - Functionality for introspecting annotations](https://docs.python.org/3.14/library/annotationlib.html)
  - [Annotation semantics](https://docs.python.org/3.14/library/annotationlib.html#annotation-semantics)
  - [Classes](https://docs.python.org/3.14/library/annotationlib.html#classes)
  - [Functions](https://docs.python.org/3.14/library/annotationlib.html#functions)
  - [Recipes](https://docs.python.org/3.14/library/annotationlib.html#recipes)
    - [Using annotations in a metaclass](https://docs.python.org/3.14/library/annotationlib.html#using-annotations-in-a-metaclass)
    - [Creating a custom callable annotate function](https://docs.python.org/3.14/library/annotationlib.html#creating-a-custom-callable-annotate-function)

  - [Limitations of the `STRING` format](https://docs.python.org/3.14/library/annotationlib.html#limitations-of-the-string-format)
  - [Limitations of the `FORWARDREF` format](https://docs.python.org/3.14/library/annotationlib.html#limitations-of-the-forwardref-format)
  - [Security implications of introspecting annotations](https://docs.python.org/3.14/library/annotationlib.html#security-implications-of-introspecting-annotations)

- [`site` - Site-specific configuration hook](https://docs.python.org/3.14/library/site.html)
  - [`sitecustomize`](https://docs.python.org/3.14/library/site.html#module-sitecustomize)
  - [`usercustomize`](https://docs.python.org/3.14/library/site.html#module-usercustomize)
  - [Readline configuration](https://docs.python.org/3.14/library/site.html#readline-configuration)
  - [Module contents](https://docs.python.org/3.14/library/site.html#module-contents)
  - [Command-line interface](https://docs.python.org/3.14/library/site.html#command-line-interface)

See also

- See the [`concurrent.interpreters`](https://docs.python.org/3.14/library/concurrent.interpreters.html#module-concurrent.interpreters) module, which likewise surfaces core runtime functionality.

[Subject index](INDEX.md) · [Continue](python-runtime-services-overview.md) · [Previous](python-runtime-services-overview.md) · [Continue](../queue/queue-queue-class.md) · [Owning module, declaration or section: Python Runtime Services](python-runtime-services-overview.md)
