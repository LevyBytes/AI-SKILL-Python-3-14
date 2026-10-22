# Creating extensions without third party tools

### Creating extensions without third party tools

The material in this part walks through building C and C++ extensions by hand, with no third party tools lending a hand. Its audience is mainly the people who write those very tools; for your own C extensions it is not the path we'd suggest taking.

See also

[**PEP 489**](https://peps.python.org/pep-0489/) – Multi-phase extension module initialization

- [1. Extending Python with C or C++](https://docs.python.org/3.14/extending/extending.html)
  - [1.1. A Simple Example](https://docs.python.org/3.14/extending/extending.html#a-simple-example)
  - [1.2. Intermezzo: Errors and Exceptions](https://docs.python.org/3.14/extending/extending.html#intermezzo-errors-and-exceptions)
  - [1.3. Back to the Example](https://docs.python.org/3.14/extending/extending.html#back-to-the-example)
  - [1.4. The Module’s Method Table and Initialization Function](https://docs.python.org/3.14/extending/extending.html#the-module-s-method-table-and-initialization-function)
  - [1.5. Compilation and Linkage](https://docs.python.org/3.14/extending/extending.html#compilation-and-linkage)
  - [1.6. Calling Python Functions from C](https://docs.python.org/3.14/extending/extending.html#calling-python-functions-from-c)
  - [1.7. Extracting Parameters in Extension Functions](https://docs.python.org/3.14/extending/extending.html#extracting-parameters-in-extension-functions)
  - [1.8. Keyword Parameters for Extension Functions](https://docs.python.org/3.14/extending/extending.html#keyword-parameters-for-extension-functions)
  - [1.9. Building Arbitrary Values](https://docs.python.org/3.14/extending/extending.html#building-arbitrary-values)
  - [1.10. Reference Counts](https://docs.python.org/3.14/extending/extending.html#reference-counts)
  - [1.11. Writing Extensions in C++](https://docs.python.org/3.14/extending/extending.html#writing-extensions-in-c)
  - [1.12. Providing a C API for an Extension Module](https://docs.python.org/3.14/extending/extending.html#providing-a-c-api-for-an-extension-module)

- [2. Defining Extension Types: Tutorial](https://docs.python.org/3.14/extending/newtypes_tutorial.html)
  - [2.1. The Basics](https://docs.python.org/3.14/extending/newtypes_tutorial.html#the-basics)
  - [2.2. Adding data and methods to the Basic example](https://docs.python.org/3.14/extending/newtypes_tutorial.html#adding-data-and-methods-to-the-basic-example)
  - [2.3. Providing finer control over data attributes](https://docs.python.org/3.14/extending/newtypes_tutorial.html#providing-finer-control-over-data-attributes)
  - [2.4. Supporting cyclic garbage collection](https://docs.python.org/3.14/extending/newtypes_tutorial.html#supporting-cyclic-garbage-collection)
  - [2.5. Subclassing other types](https://docs.python.org/3.14/extending/newtypes_tutorial.html#subclassing-other-types)

- [3. Defining Extension Types: Assorted Topics](https://docs.python.org/3.14/extending/newtypes.html)
  - [3.1. Finalization and De-allocation](https://docs.python.org/3.14/extending/newtypes.html#finalization-and-de-allocation)
  - [3.2. Object Presentation](https://docs.python.org/3.14/extending/newtypes.html#object-presentation)
  - [3.3. Attribute Management](https://docs.python.org/3.14/extending/newtypes.html#attribute-management)
  - [3.4. Object Comparison](https://docs.python.org/3.14/extending/newtypes.html#object-comparison)
  - [3.5. Abstract Protocol Support](https://docs.python.org/3.14/extending/newtypes.html#abstract-protocol-support)
  - [3.6. Weak Reference Support](https://docs.python.org/3.14/extending/newtypes.html#weak-reference-support)
  - [3.7. More Suggestions](https://docs.python.org/3.14/extending/newtypes.html#more-suggestions)

- [4. Building C and C++ Extensions](https://docs.python.org/3.14/extending/building.html)
  - [4.1. Building C and C++ Extensions with setuptools](https://docs.python.org/3.14/extending/building.html#building-c-and-c-extensions-with-setuptools)

- [5. Building C and C++ Extensions on Windows](https://docs.python.org/3.14/extending/windows.html)
  - [5.1. A Cookbook Approach](https://docs.python.org/3.14/extending/windows.html#a-cookbook-approach)
  - [5.2. Differences Between Unix and Windows](https://docs.python.org/3.14/extending/windows.html#differences-between-unix-and-windows)
  - [5.3. Using DLLs in Practice](https://docs.python.org/3.14/extending/windows.html#using-dlls-in-practice)

[Subject index](INDEX.md) · [Previous source section](recommended-third-party-tools.md) · [Next source section](embedding-the-cpython-runtime-in-a-larger-application.md)
