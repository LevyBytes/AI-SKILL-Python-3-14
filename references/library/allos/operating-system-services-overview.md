# Generic Operating System Services — Section introduction and initial examples

# Allos

### Generic Operating System Services

This chapter's modules expose interfaces to operating system features present on (nearly) every operating system, such as files and a clock. While these interfaces largely follow the Unix or C interfaces, they remain available on most other systems too. The list below gives an overview:

- [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3.14/library/os.html)
  - [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3.14/library/os.html#file-names-command-line-arguments-and-environment-variables)
  - [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#python-utf-8-mode)
  - [Process Parameters](https://docs.python.org/3.14/library/os.html#process-parameters)
  - [File Object Creation](https://docs.python.org/3.14/library/os.html#file-object-creation)
  - [File Descriptor Operations](https://docs.python.org/3.14/library/os.html#file-descriptor-operations)
    - [Querying the size of a terminal](https://docs.python.org/3.14/library/os.html#querying-the-size-of-a-terminal)
    - [Inheritance of File Descriptors](https://docs.python.org/3.14/library/os.html#inheritance-of-file-descriptors)

  - [Files and Directories](https://docs.python.org/3.14/library/os.html#files-and-directories)
    - [Timer File Descriptors](https://docs.python.org/3.14/library/os.html#timer-file-descriptors)
    - [Linux extended attributes](https://docs.python.org/3.14/library/os.html#linux-extended-attributes)

  - [Process Management](https://docs.python.org/3.14/library/os.html#process-management)
  - [Interface to the scheduler](https://docs.python.org/3.14/library/os.html#interface-to-the-scheduler)
  - [Miscellaneous System Information](https://docs.python.org/3.14/library/os.html#miscellaneous-system-information)
  - [Random numbers](https://docs.python.org/3.14/library/os.html#random-numbers)

- [`io` — Core tools for working with streams](https://docs.python.org/3.14/library/io.html)
  - [Overview](https://docs.python.org/3.14/library/io.html#overview)
    - [Text I/O](https://docs.python.org/3.14/library/io.html#text-i-o)
    - [Binary I/O](https://docs.python.org/3.14/library/io.html#binary-i-o)
    - [Raw I/O](https://docs.python.org/3.14/library/io.html#raw-i-o)

  - [Text Encoding](https://docs.python.org/3.14/library/io.html#text-encoding)
    - [Opt-in EncodingWarning](https://docs.python.org/3.14/library/io.html#opt-in-encodingwarning)

  - [High-level Module Interface](https://docs.python.org/3.14/library/io.html#high-level-module-interface)
  - [Class hierarchy](https://docs.python.org/3.14/library/io.html#class-hierarchy)
    - [I/O Base Classes](https://docs.python.org/3.14/library/io.html#i-o-base-classes)
    - [Raw File I/O](https://docs.python.org/3.14/library/io.html#raw-file-i-o)
    - [Buffered Streams](https://docs.python.org/3.14/library/io.html#buffered-streams)
    - [Text I/O](https://docs.python.org/3.14/library/io.html#id1)

  - [Static Typing](https://docs.python.org/3.14/library/io.html#static-typing)
  - [Performance](https://docs.python.org/3.14/library/io.html#performance)
    - [Binary I/O](https://docs.python.org/3.14/library/io.html#id2)
    - [Text I/O](https://docs.python.org/3.14/library/io.html#id3)
    - [Multi-threading](https://docs.python.org/3.14/library/io.html#multi-threading)
    - [Reentrancy](https://docs.python.org/3.14/library/io.html#reentrancy)

- [`time` — Time access and conversions](https://docs.python.org/3.14/library/time.html)
  - [Functions](https://docs.python.org/3.14/library/time.html#functions)
  - [Clock ID Constants](https://docs.python.org/3.14/library/time.html#clock-id-constants)
  - [Timezone Constants](https://docs.python.org/3.14/library/time.html#timezone-constants)

- [`logging` — Logging facility for Python](https://docs.python.org/3.14/library/logging.html)
  - [Logger Objects](https://docs.python.org/3.14/library/logging.html#logger-objects)
  - [Logging Levels](https://docs.python.org/3.14/library/logging.html#logging-levels)
  - [Handler Objects](https://docs.python.org/3.14/library/logging.html#handler-objects)
  - [Formatter Objects](https://docs.python.org/3.14/library/logging.html#formatter-objects)
  - [Filter Objects](https://docs.python.org/3.14/library/logging.html#filter-objects)
  - [LogRecord Objects](https://docs.python.org/3.14/library/logging.html#logrecord-objects)
  - [LogRecord attributes](https://docs.python.org/3.14/library/logging.html#logrecord-attributes)
  - [LoggerAdapter Objects](https://docs.python.org/3.14/library/logging.html#loggeradapter-objects)
  - [Thread Safety](https://docs.python.org/3.14/library/logging.html#thread-safety)
  - [Module-Level Functions](https://docs.python.org/3.14/library/logging.html#module-level-functions)
  - [Module-Level Attributes](https://docs.python.org/3.14/library/logging.html#module-level-attributes)
  - [Integration with the warnings module](https://docs.python.org/3.14/library/logging.html#integration-with-the-warnings-module)

- [`logging.config` — Logging configuration](https://docs.python.org/3.14/library/logging.config.html)
  - [Configuration functions](https://docs.python.org/3.14/library/logging.config.html#configuration-functions)
  - [Security considerations](https://docs.python.org/3.14/library/logging.config.html#security-considerations)
  - [Configuration dictionary schema](https://docs.python.org/3.14/library/logging.config.html#configuration-dictionary-schema)
    - [Dictionary Schema Details](https://docs.python.org/3.14/library/logging.config.html#dictionary-schema-details)
    - [Incremental Configuration](https://docs.python.org/3.14/library/logging.config.html#incremental-configuration)
    - [Object connections](https://docs.python.org/3.14/library/logging.config.html#object-connections)
    - [User-defined objects](https://docs.python.org/3.14/library/logging.config.html#user-defined-objects)
    - [Handler configuration order](https://docs.python.org/3.14/library/logging.config.html#handler-configuration-order)
    - [Access to external objects](https://docs.python.org/3.14/library/logging.config.html#access-to-external-objects)
    - [Access to internal objects](https://docs.python.org/3.14/library/logging.config.html#access-to-internal-objects)
    - [Import resolution and custom importers](https://docs.python.org/3.14/library/logging.config.html#import-resolution-and-custom-importers)
    - [Configuring QueueHandler and QueueListener](https://docs.python.org/3.14/library/logging.config.html#configuring-queuehandler-and-queuelistener)

  - [Configuration file format](https://docs.python.org/3.14/library/logging.config.html#configuration-file-format)

[Subject index](INDEX.md) · [Continue](generic-operating-system-services.md)
