# 2.6.2. Floating-point literals

### 2.6.2. Floating-point literals

Floating-point (float) literals, examples being `3.14` or `1.5`, denote [approximations of real numbers](https://docs.python.org/3.14/reference/datamodel.html#datamodel-float).

They are built from an *integer* and a *fraction* part, with each one made of decimal digits. A decimal point, `.`, divides the parts:

```python
2.71828
4.0

```

Differing from integer literals, leading zeros are permitted here. To illustrate, `077.010` is legal and stands for the very same number as `77.01`.

Just as in integer literals, single underscores are allowed between digits to aid readability:

```python
96_485.332_123
3.14_15_93

```

Either part may be empty, though not both at once. To illustrate:

```python
10.  # (equivalent to 10.0)
.001  # (equivalent to 0.001)

```

As an option, an *exponent* may trail the integer and fraction: the letter `e` or `E`, then an optional sign, `+` or `-`, then a number laid out the same way as the integer and fraction parts. What `e` or `E` conveys is “times ten raised to the power of”:

```python
1.0e3  # (represents 1.0×10³, or 1000.0)
1.166e-5  # (represents 1.166×10⁻⁵, or 0.00001166)
6.02214076e+23  # (represents 6.02214076×10²³, or 602214076000000000000000.)

```

Where a float carries only integer and exponent parts, the decimal point can be dropped:

```python
1e3  # (equivalent to 1.e3 and 1.0e3)
0e0  # (equivalent to 0.)

```

The lexical definitions below give the formal description of floating-point literals:

```text

floatnumber:
   | digitpart "." [digitpart] [exponent]
   | "." digitpart [exponent]
   | digitpart exponent
digitpart: digit (["_"] digit)*
exponent:  ("e" | "E") ["+" | "-"] digitpart
```

Changed in version 3.6: Within literals, underscores became permitted as a way to group digits.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](numeric-literals.md) · [Previous source section](integer-literals.md) · [Following source section](imaginary-literals.md)
