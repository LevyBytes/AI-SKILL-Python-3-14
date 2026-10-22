# What’s New in Python 2.4 / PEP 327: Decimal Data Type

### PEP 327: Decimal Data Type

Floating-point (FP) numbers, resting on the C double type underneath, have always been one of Python’s data types. Yet even though nearly every programming language supplies a floating-point type, plenty of people — programmers included — don’t realize that floating-point numbers fail to represent some decimal fractions exactly. Up to a precision ceiling the user picks, the new `Decimal` type can hold those fractions exactly.

[Subject index](INDEX.md) · [Previous source section](pep-324-new-subprocess-module.md) · [Next source section](why-is-decimal-needed.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
