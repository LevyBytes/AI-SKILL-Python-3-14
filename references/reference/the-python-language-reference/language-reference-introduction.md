# language reference: Language reference introduction and core syntax topics

# Introduction

## Overview

Covers: The Python Language Reference; 1. Introduction.

## The Python Language Reference

### The Python Language Reference

This manual lays out the grammar and the central meaning of the language. The writing is compact, yet it aims for precision and full coverage. How the optional built-in object kinds behave, together with the behavior of the built-in routines and the bundled modules, is covered separately in [The Python Standard Library](https://docs.python.org/3.14/library/index.html#library-index). Anyone wanting a gentler walkthrough should turn to [The Python Tutorial](https://docs.python.org/3.14/tutorial/index.html#tutorial-index). Those coding in C or C++ have two further guides at their disposal: [Extending and Embedding the Python Interpreter](https://docs.python.org/3.14/extending/index.html#extending-index) sketches, at a broad level, the steps for authoring a Python extension module, while the [Python/C API reference manual](https://docs.python.org/3.14/c-api/index.html#c-api-index) spells out the interfaces open to C/C++ developers thoroughly.

- [1. Introduction](https://docs.python.org/3.14/reference/introduction.html)
  - [1.1. Alternate Implementations](https://docs.python.org/3.14/reference/introduction.html#alternate-implementations)
  - [1.2. Notation](https://docs.python.org/3.14/reference/introduction.html#notation)

- [2. Lexical analysis](https://docs.python.org/3.14/reference/lexical_analysis.html)
  - [2.1. Line structure](https://docs.python.org/3.14/reference/lexical_analysis.html#line-structure)
  - [2.2. Other tokens](https://docs.python.org/3.14/reference/lexical_analysis.html#other-tokens)
  - [2.3. Names (identifiers and keywords)](https://docs.python.org/3.14/reference/lexical_analysis.html#names-identifiers-and-keywords)
  - [2.4. Literals](https://docs.python.org/3.14/reference/lexical_analysis.html#literals)
  - [2.5. String and Bytes literals](https://docs.python.org/3.14/reference/lexical_analysis.html#string-and-bytes-literals)
  - [2.6. Numeric literals](https://docs.python.org/3.14/reference/lexical_analysis.html#numeric-literals)
  - [2.7. Operators and delimiters](https://docs.python.org/3.14/reference/lexical_analysis.html#operators-and-delimiters)

- [3. Data model](https://docs.python.org/3.14/reference/datamodel.html)
  - [3.1. Objects, values and types](https://docs.python.org/3.14/reference/datamodel.html#objects-values-and-types)
  - [3.2. The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#the-standard-type-hierarchy)
  - [3.3. Special method names](https://docs.python.org/3.14/reference/datamodel.html#special-method-names)
  - [3.4. Coroutines](https://docs.python.org/3.14/reference/datamodel.html#coroutines)

- [4. Execution model](https://docs.python.org/3.14/reference/executionmodel.html)
  - [4.1. Structure of a program](https://docs.python.org/3.14/reference/executionmodel.html#structure-of-a-program)
  - [4.2. Naming and binding](https://docs.python.org/3.14/reference/executionmodel.html#naming-and-binding)
  - [4.3. Exceptions](https://docs.python.org/3.14/reference/executionmodel.html#exceptions)
  - [4.4. Runtime Components](https://docs.python.org/3.14/reference/executionmodel.html#runtime-components)

- [5. The import system](https://docs.python.org/3.14/reference/import.html)
  - [5.1. `importlib`](https://docs.python.org/3.14/reference/import.html#importlib)
  - [5.2. Packages](https://docs.python.org/3.14/reference/import.html#packages)
  - [5.3. Searching](https://docs.python.org/3.14/reference/import.html#searching)
  - [5.4. Loading](https://docs.python.org/3.14/reference/import.html#loading)
  - [5.5. The Path Based Finder](https://docs.python.org/3.14/reference/import.html#the-path-based-finder)
  - [5.6. Replacing the standard import system](https://docs.python.org/3.14/reference/import.html#replacing-the-standard-import-system)
  - [5.7. Package Relative Imports](https://docs.python.org/3.14/reference/import.html#package-relative-imports)
  - [5.8. Special considerations for __main__](https://docs.python.org/3.14/reference/import.html#special-considerations-for-main)
  - [5.9. References](https://docs.python.org/3.14/reference/import.html#references)

- [6. Expressions](https://docs.python.org/3.14/reference/expressions.html)
  - [6.1. Arithmetic conversions](https://docs.python.org/3.14/reference/expressions.html#arithmetic-conversions)
  - [6.2. Atoms](https://docs.python.org/3.14/reference/expressions.html#atoms)
  - [6.3. Primaries](https://docs.python.org/3.14/reference/expressions.html#primaries)
  - [6.4. Await expression](https://docs.python.org/3.14/reference/expressions.html#await-expression)
  - [6.5. The power operator](https://docs.python.org/3.14/reference/expressions.html#the-power-operator)
  - [6.6. Unary arithmetic and bitwise operations](https://docs.python.org/3.14/reference/expressions.html#unary-arithmetic-and-bitwise-operations)
  - [6.7. Binary arithmetic operations](https://docs.python.org/3.14/reference/expressions.html#binary-arithmetic-operations)
  - [6.8. Shifting operations](https://docs.python.org/3.14/reference/expressions.html#shifting-operations)
  - [6.9. Binary bitwise operations](https://docs.python.org/3.14/reference/expressions.html#binary-bitwise-operations)
  - [6.10. Comparisons](https://docs.python.org/3.14/reference/expressions.html#comparisons)
  - [6.11. Boolean operations](https://docs.python.org/3.14/reference/expressions.html#boolean-operations)
  - [6.12. Assignment expressions](https://docs.python.org/3.14/reference/expressions.html#assignment-expressions)
  - [6.13. Conditional expressions](https://docs.python.org/3.14/reference/expressions.html#conditional-expressions)
  - [6.14. Lambdas](https://docs.python.org/3.14/reference/expressions.html#lambda)
  - [6.15. Expression lists](https://docs.python.org/3.14/reference/expressions.html#expression-lists)
  - [6.16. Evaluation order](https://docs.python.org/3.14/reference/expressions.html#evaluation-order)
  - [6.17. Operator precedence](https://docs.python.org/3.14/reference/expressions.html#operator-precedence)

- [7. Simple statements](https://docs.python.org/3.14/reference/simple_stmts.html)
  - [7.1. Expression statements](https://docs.python.org/3.14/reference/simple_stmts.html#expression-statements)
  - [7.2. Assignment statements](https://docs.python.org/3.14/reference/simple_stmts.html#assignment-statements)
  - [7.3. The `assert` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-assert-statement)
  - [7.4. The `pass` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-pass-statement)
  - [7.5. The `del` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-del-statement)
  - [7.6. The `return` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-return-statement)
  - [7.7. The `yield` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-yield-statement)
  - [7.8. The `raise` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-raise-statement)
  - [7.9. The `break` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-break-statement)
  - [7.10. The `continue` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-continue-statement)
  - [7.11. The `import` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-import-statement)
  - [7.12. The `global` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-global-statement)
  - [7.13. The `nonlocal` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement)
  - [7.14. The `type` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-type-statement)

[Subject index](INDEX.md) · [Following source section](the-python-language-reference-8.md)
