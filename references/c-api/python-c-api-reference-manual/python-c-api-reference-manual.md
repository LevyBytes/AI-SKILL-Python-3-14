# python c api reference manual C API: C API scope for extensions and embedding

# Init

## Overview

Covers: Python/C API reference manual; Initialization, finalization, and threads.

## Python/C API reference manual

### Python/C API reference manual

Aimed at C and C++ developers building extension modules or embedding Python, this reference describes the available API. Treat it as a counterpart to [Extending and Embedding the Python Interpreter](https://docs.python.org/3.14/extending/index.html#extending-index), a guide that lays out the broad principles behind extensions yet leaves the individual API functions undocumented in depth.

- [Introduction](https://docs.python.org/3.14/c-api/intro.html)
  - [Language version compatibility](https://docs.python.org/3.14/c-api/intro.html#language-version-compatibility)
  - [Coding standards](https://docs.python.org/3.14/c-api/intro.html#coding-standards)
  - [Include Files](https://docs.python.org/3.14/c-api/intro.html#include-files)
  - [Useful macros](https://docs.python.org/3.14/c-api/intro.html#useful-macros)
  - [Objects, Types and Reference Counts](https://docs.python.org/3.14/c-api/intro.html#objects-types-and-reference-counts)
  - [Exceptions](https://docs.python.org/3.14/c-api/intro.html#exceptions)
  - [Embedding Python](https://docs.python.org/3.14/c-api/intro.html#embedding-python)
  - [Debugging Builds](https://docs.python.org/3.14/c-api/intro.html#debugging-builds)
  - [Recommended third party tools](https://docs.python.org/3.14/c-api/intro.html#recommended-third-party-tools)

- [C API Stability](https://docs.python.org/3.14/c-api/stable.html)
  - [Unstable C API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api)
  - [Stable Application Binary Interface](https://docs.python.org/3.14/c-api/stable.html#stable-application-binary-interface)
  - [Platform Considerations](https://docs.python.org/3.14/c-api/stable.html#platform-considerations)
  - [Contents of Limited API](https://docs.python.org/3.14/c-api/stable.html#contents-of-limited-api)

- [The Very High Level Layer](https://docs.python.org/3.14/c-api/veryhigh.html)
  - [Available start symbols](https://docs.python.org/3.14/c-api/veryhigh.html#available-start-symbols)
  - [Stack Effects](https://docs.python.org/3.14/c-api/veryhigh.html#stack-effects)

- [Reference Counting](https://docs.python.org/3.14/c-api/refcounting.html)
- [Exception Handling](https://docs.python.org/3.14/c-api/exceptions.html)
  - [Printing and clearing](https://docs.python.org/3.14/c-api/exceptions.html#printing-and-clearing)
  - [Raising exceptions](https://docs.python.org/3.14/c-api/exceptions.html#raising-exceptions)
  - [Issuing warnings](https://docs.python.org/3.14/c-api/exceptions.html#issuing-warnings)
  - [Querying the error indicator](https://docs.python.org/3.14/c-api/exceptions.html#querying-the-error-indicator)
  - [Signal Handling](https://docs.python.org/3.14/c-api/exceptions.html#signal-handling)
  - [Exception Classes](https://docs.python.org/3.14/c-api/exceptions.html#exception-classes)
  - [Exception Objects](https://docs.python.org/3.14/c-api/exceptions.html#exception-objects)
  - [Unicode Exception Objects](https://docs.python.org/3.14/c-api/exceptions.html#unicode-exception-objects)
  - [Recursion Control](https://docs.python.org/3.14/c-api/exceptions.html#recursion-control)
  - [Exception and warning types](https://docs.python.org/3.14/c-api/exceptions.html#exception-and-warning-types)
  - [Tracebacks](https://docs.python.org/3.14/c-api/exceptions.html#tracebacks)

- [Defining extension modules](https://docs.python.org/3.14/c-api/extension-modules.html)
  - [Multiple module instances](https://docs.python.org/3.14/c-api/extension-modules.html#multiple-module-instances)
  - [Initialization function](https://docs.python.org/3.14/c-api/extension-modules.html#initialization-function)
  - [Multi-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#multi-phase-initialization)
  - [Legacy single-phase initialization](https://docs.python.org/3.14/c-api/extension-modules.html#legacy-single-phase-initialization)

- [Utilities](https://docs.python.org/3.14/c-api/utilities.html)
  - [Operating System Utilities](https://docs.python.org/3.14/c-api/sys.html)
  - [System Functions](https://docs.python.org/3.14/c-api/sys.html#system-functions)
  - [Process Control](https://docs.python.org/3.14/c-api/sys.html#process-control)
  - [Importing Modules](https://docs.python.org/3.14/c-api/import.html)
  - [Data marshalling support](https://docs.python.org/3.14/c-api/marshal.html)
  - [Parsing arguments and building values](https://docs.python.org/3.14/c-api/arg.html)
  - [String conversion and formatting](https://docs.python.org/3.14/c-api/conversion.html)
  - [Character classification and conversion](https://docs.python.org/3.14/c-api/conversion.html#character-classification-and-conversion)
  - [PyHash API](https://docs.python.org/3.14/c-api/hash.html)
  - [Reflection](https://docs.python.org/3.14/c-api/reflection.html)
  - [Codec registry and support functions](https://docs.python.org/3.14/c-api/codec.html)
  - [PyTime C API](https://docs.python.org/3.14/c-api/time.html)
  - [Support for Perf Maps](https://docs.python.org/3.14/c-api/perfmaps.html)

- [Abstract Objects Layer](https://docs.python.org/3.14/c-api/abstract.html)
  - [Object Protocol](https://docs.python.org/3.14/c-api/object.html)
  - [Call Protocol](https://docs.python.org/3.14/c-api/call.html)
  - [Number Protocol](https://docs.python.org/3.14/c-api/number.html)
  - [Sequence Protocol](https://docs.python.org/3.14/c-api/sequence.html)
  - [Mapping Protocol](https://docs.python.org/3.14/c-api/mapping.html)
  - [Iterator Protocol](https://docs.python.org/3.14/c-api/iter.html)
  - [Buffer Protocol](https://docs.python.org/3.14/c-api/buffer.html)

[Subject index](INDEX.md) · [Following source contract](concrete-objects-and-extension-api-routes.md)
