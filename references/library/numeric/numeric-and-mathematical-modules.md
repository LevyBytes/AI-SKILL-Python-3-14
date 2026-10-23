# numbers - Numeric and Mathematical Modules

## Numeric and Mathematical Modules

### Numeric and Mathematical Modules

This chapter's modules deliver numeric and math-oriented functions along with data types. An abstract hierarchy of numeric types is laid out by the [`numbers`](https://docs.python.org/3.14/library/numbers.html#module-numbers) module. Assorted mathematical functions for floating-point and complex values live in the [`math`](https://docs.python.org/3.14/library/math.html#module-math) and [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) modules. Exact decimal-number representations, backed by arbitrary-precision arithmetic, are what the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module offers.

Documentation for the modules below appears throughout this chapter:

- [`numbers` - Numeric abstract base classes](https://docs.python.org/3.14/library/numbers.html)
  - [The numeric tower](https://docs.python.org/3.14/library/numbers.html#the-numeric-tower)
  - [Notes for type implementers](https://docs.python.org/3.14/library/numbers.html#notes-for-type-implementers)
    - [Adding More Numeric ABCs](https://docs.python.org/3.14/library/numbers.html#adding-more-numeric-abcs)
    - [Implementing the arithmetic operations](https://docs.python.org/3.14/library/numbers.html#implementing-the-arithmetic-operations)

- [`math` - Mathematical functions](https://docs.python.org/3.14/library/math.html)
  - [Number-theoretic functions](https://docs.python.org/3.14/library/math.html#number-theoretic-functions)
  - [Floating point arithmetic](https://docs.python.org/3.14/library/math.html#floating-point-arithmetic)
  - [Floating point manipulation functions](https://docs.python.org/3.14/library/math.html#floating-point-manipulation-functions)
  - [Power, exponential and logarithmic functions](https://docs.python.org/3.14/library/math.html#power-exponential-and-logarithmic-functions)
  - [Summation and product functions](https://docs.python.org/3.14/library/math.html#summation-and-product-functions)
  - [Angular conversion](https://docs.python.org/3.14/library/math.html#angular-conversion)
  - [Trigonometric functions](https://docs.python.org/3.14/library/math.html#trigonometric-functions)
  - [Hyperbolic functions](https://docs.python.org/3.14/library/math.html#hyperbolic-functions)
  - [Special functions](https://docs.python.org/3.14/library/math.html#special-functions)
  - [Constants](https://docs.python.org/3.14/library/math.html#constants)

- [`cmath` - Mathematical functions for complex numbers](https://docs.python.org/3.14/library/cmath.html)
  - [Conversions to and from polar coordinates](https://docs.python.org/3.14/library/cmath.html#conversions-to-and-from-polar-coordinates)
  - [Power and logarithmic functions](https://docs.python.org/3.14/library/cmath.html#power-and-logarithmic-functions)
  - [Trigonometric functions](https://docs.python.org/3.14/library/cmath.html#trigonometric-functions)
  - [Hyperbolic functions](https://docs.python.org/3.14/library/cmath.html#hyperbolic-functions)
  - [Classification functions](https://docs.python.org/3.14/library/cmath.html#classification-functions)
  - [Constants](https://docs.python.org/3.14/library/cmath.html#constants)

- [`decimal` - Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3.14/library/decimal.html)
  - [Quick-start tutorial](https://docs.python.org/3.14/library/decimal.html#quick-start-tutorial)
  - [Decimal objects](https://docs.python.org/3.14/library/decimal.html#decimal-objects)
    - [Logical operands](https://docs.python.org/3.14/library/decimal.html#logical-operands)

  - [Context objects](https://docs.python.org/3.14/library/decimal.html#context-objects)
  - [Constants](https://docs.python.org/3.14/library/decimal.html#constants)
  - [Rounding modes](https://docs.python.org/3.14/library/decimal.html#rounding-modes)
  - [Signals](https://docs.python.org/3.14/library/decimal.html#signals)
  - [Floating-point notes](https://docs.python.org/3.14/library/decimal.html#floating-point-notes)
    - [Mitigating round-off error with increased precision](https://docs.python.org/3.14/library/decimal.html#mitigating-round-off-error-with-increased-precision)
    - [Special values](https://docs.python.org/3.14/library/decimal.html#special-values)

  - [Working with threads](https://docs.python.org/3.14/library/decimal.html#working-with-threads)
  - [Recipes](https://docs.python.org/3.14/library/decimal.html#recipes)
  - [Decimal FAQ](https://docs.python.org/3.14/library/decimal.html#decimal-faq)

- [`fractions` - Rational numbers](https://docs.python.org/3.14/library/fractions.html)
- [`random` - Generate pseudo-random numbers](https://docs.python.org/3.14/library/random.html)
  - [Bookkeeping functions](https://docs.python.org/3.14/library/random.html#bookkeeping-functions)
  - [Functions for bytes](https://docs.python.org/3.14/library/random.html#functions-for-bytes)
  - [Functions for integers](https://docs.python.org/3.14/library/random.html#functions-for-integers)
  - [Functions for sequences](https://docs.python.org/3.14/library/random.html#functions-for-sequences)
  - [Discrete distributions](https://docs.python.org/3.14/library/random.html#discrete-distributions)
  - [Real-valued distributions](https://docs.python.org/3.14/library/random.html#real-valued-distributions)
  - [Alternative Generator](https://docs.python.org/3.14/library/random.html#alternative-generator)
  - [Notes on Reproducibility](https://docs.python.org/3.14/library/random.html#notes-on-reproducibility)
  - [Examples](https://docs.python.org/3.14/library/random.html#examples)
  - [Recipes](https://docs.python.org/3.14/library/random.html#recipes)
  - [Command-line usage](https://docs.python.org/3.14/library/random.html#command-line-usage)
  - [Command-line example](https://docs.python.org/3.14/library/random.html#command-line-example)

- [`statistics` - Mathematical statistics functions](https://docs.python.org/3.14/library/statistics.html)
  - [Averages and measures of central location](https://docs.python.org/3.14/library/statistics.html#averages-and-measures-of-central-location)
  - [Measures of spread](https://docs.python.org/3.14/library/statistics.html#measures-of-spread)
  - [Statistics for relations between two inputs](https://docs.python.org/3.14/library/statistics.html#statistics-for-relations-between-two-inputs)
  - [Function details](https://docs.python.org/3.14/library/statistics.html#function-details)
  - [Exceptions](https://docs.python.org/3.14/library/statistics.html#exceptions)
  - [`NormalDist` objects](https://docs.python.org/3.14/library/statistics.html#normaldist-objects)
  - [Examples and Recipes](https://docs.python.org/3.14/library/statistics.html#examples-and-recipes)
    - [Classic probability problems](https://docs.python.org/3.14/library/statistics.html#classic-probability-problems)
    - [Monte Carlo inputs for simulations](https://docs.python.org/3.14/library/statistics.html#monte-carlo-inputs-for-simulations)
    - [Approximating binomial distributions](https://docs.python.org/3.14/library/statistics.html#approximating-binomial-distributions)
    - [Naive bayesian classifier](https://docs.python.org/3.14/library/statistics.html#naive-bayesian-classifier)

[Subject index](INDEX.md)
