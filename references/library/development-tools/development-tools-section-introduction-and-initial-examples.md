# Development Tools - Section introduction and initial examples

# Development

### Development Tools

This chapter's modules assist you in writing software. The [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) module, for instance, accepts a module and produces documentation from that module's contents. Frameworks for authoring unit tests that automatically run code and confirm it yields the expected output live in the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) and [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) modules.

Here are the modules this chapter covers:

- [`typing` - Support for type hints](https://docs.python.org/3.14/library/typing.html)
  - [Specification for the Python Type System](https://docs.python.org/3.14/library/typing.html#specification-for-the-python-type-system)
  - [Type aliases](https://docs.python.org/3.14/library/typing.html#type-aliases)
  - [NewType](https://docs.python.org/3.14/library/typing.html#newtype)
  - [Annotating callable objects](https://docs.python.org/3.14/library/typing.html#annotating-callable-objects)
  - [Generics](https://docs.python.org/3.14/library/typing.html#generics)
  - [Annotating tuples](https://docs.python.org/3.14/library/typing.html#annotating-tuples)
  - [The type of class objects](https://docs.python.org/3.14/library/typing.html#the-type-of-class-objects)
  - [Annotating generators and coroutines](https://docs.python.org/3.14/library/typing.html#annotating-generators-and-coroutines)
  - [User-defined generic types](https://docs.python.org/3.14/library/typing.html#user-defined-generic-types)
  - [The `Any` type](https://docs.python.org/3.14/library/typing.html#the-any-type)
  - [Nominal vs structural subtyping](https://docs.python.org/3.14/library/typing.html#nominal-vs-structural-subtyping)
  - [Module contents](https://docs.python.org/3.14/library/typing.html#module-contents)
    - [Special typing primitives](https://docs.python.org/3.14/library/typing.html#special-typing-primitives)
      - [Special types](https://docs.python.org/3.14/library/typing.html#special-types)
      - [Special forms](https://docs.python.org/3.14/library/typing.html#special-forms)
      - [Building generic types and type aliases](https://docs.python.org/3.14/library/typing.html#building-generic-types-and-type-aliases)
      - [Other special directives](https://docs.python.org/3.14/library/typing.html#other-special-directives)

    - [Protocols](https://docs.python.org/3.14/library/typing.html#protocols)
    - [ABCs and Protocols for working with I/O](https://docs.python.org/3.14/library/typing.html#abcs-and-protocols-for-working-with-i-o)
    - [Functions and decorators](https://docs.python.org/3.14/library/typing.html#functions-and-decorators)
    - [Introspection helpers](https://docs.python.org/3.14/library/typing.html#introspection-helpers)
    - [Constant](https://docs.python.org/3.14/library/typing.html#constant)
    - [Deprecated aliases](https://docs.python.org/3.14/library/typing.html#deprecated-aliases)
      - [Aliases to built-in types](https://docs.python.org/3.14/library/typing.html#aliases-to-built-in-types)
      - [Aliases to types in `collections`](https://docs.python.org/3.14/library/typing.html#aliases-to-types-in-collections)
      - [Aliases to other concrete types](https://docs.python.org/3.14/library/typing.html#aliases-to-other-concrete-types)
      - [Aliases to container ABCs in `collections.abc`](https://docs.python.org/3.14/library/typing.html#aliases-to-container-abcs-in-collections-abc)
      - [Aliases to asynchronous ABCs in `collections.abc`](https://docs.python.org/3.14/library/typing.html#aliases-to-asynchronous-abcs-in-collections-abc)
      - [Aliases to other ABCs in `collections.abc`](https://docs.python.org/3.14/library/typing.html#aliases-to-other-abcs-in-collections-abc)
      - [Aliases to `contextlib` ABCs](https://docs.python.org/3.14/library/typing.html#aliases-to-contextlib-abcs)

  - [Deprecation Timeline of Major Features](https://docs.python.org/3.14/library/typing.html#deprecation-timeline-of-major-features)

- [`pydoc` - Documentation generator and online help system](https://docs.python.org/3.14/library/pydoc.html)
- [Python Development Mode](https://docs.python.org/3.14/library/devmode.html)
  - [Effects of the Python Development Mode](https://docs.python.org/3.14/library/devmode.html#effects-of-the-python-development-mode)
  - [ResourceWarning Example](https://docs.python.org/3.14/library/devmode.html#resourcewarning-example)
  - [Bad file descriptor error example](https://docs.python.org/3.14/library/devmode.html#bad-file-descriptor-error-example)

- [`doctest` - Test interactive Python examples](https://docs.python.org/3.14/library/doctest.html)
  - [Simple Usage: Checking Examples in Docstrings](https://docs.python.org/3.14/library/doctest.html#simple-usage-checking-examples-in-docstrings)
  - [Simple Usage: Checking Examples in a Text File](https://docs.python.org/3.14/library/doctest.html#simple-usage-checking-examples-in-a-text-file)
  - [Command-line Usage](https://docs.python.org/3.14/library/doctest.html#command-line-usage)
  - [How It Works](https://docs.python.org/3.14/library/doctest.html#how-it-works)
    - [Which Docstrings Are Examined?](https://docs.python.org/3.14/library/doctest.html#which-docstrings-are-examined)
    - [How are Docstring Examples Recognized?](https://docs.python.org/3.14/library/doctest.html#how-are-docstring-examples-recognized)
    - [What’s the Execution Context?](https://docs.python.org/3.14/library/doctest.html#what-s-the-execution-context)
    - [What About Exceptions?](https://docs.python.org/3.14/library/doctest.html#what-about-exceptions)
    - [Option Flags](https://docs.python.org/3.14/library/doctest.html#option-flags)
    - [Directives](https://docs.python.org/3.14/library/doctest.html#directives)
    - [Warnings](https://docs.python.org/3.14/library/doctest.html#warnings)

  - [Basic API](https://docs.python.org/3.14/library/doctest.html#basic-api)
  - [Unittest API](https://docs.python.org/3.14/library/doctest.html#unittest-api)
  - [Advanced API](https://docs.python.org/3.14/library/doctest.html#advanced-api)
    - [DocTest Objects](https://docs.python.org/3.14/library/doctest.html#doctest-objects)
    - [Example Objects](https://docs.python.org/3.14/library/doctest.html#example-objects)
    - [DocTestFinder objects](https://docs.python.org/3.14/library/doctest.html#doctestfinder-objects)
    - [DocTestParser objects](https://docs.python.org/3.14/library/doctest.html#doctestparser-objects)
    - [TestResults objects](https://docs.python.org/3.14/library/doctest.html#testresults-objects)
    - [DocTestRunner objects](https://docs.python.org/3.14/library/doctest.html#doctestrunner-objects)
    - [OutputChecker objects](https://docs.python.org/3.14/library/doctest.html#outputchecker-objects)

  - [Debugging](https://docs.python.org/3.14/library/doctest.html#debugging)
  - [Soapbox](https://docs.python.org/3.14/library/doctest.html#soapbox)

[Subject index](INDEX.md) · [Continue](development-tools.md)
