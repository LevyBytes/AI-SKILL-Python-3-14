# 2.6.3. Imaginary literals

### 2.6.3. Imaginary literals

Python provides [complex number](https://docs.python.org/3.14/library/stdtypes.html#typesnumeric) objects, yet offers no complex literals. In their place, *imaginary literals* denote complex numbers whose real part is zero.

To illustrate, in mathematics the complex number 3+4.2*i* is expressed as the real number 3 plus the imaginary number 4.2*i*. Python follows a comparable syntax, the difference being that the imaginary unit appears as `j` in place of *i*:

```python
3+4.2j

```

What you have here is an expression made of the integer literal `3`, the operator ‘`+`’, and the imaginary literal `4.2j`. Because these amount to three distinct tokens, whitespace between them is allowed:

```python
3 + 4.2j

```

*Within* any single token, whitespace is forbidden. In particular, the `j` suffix cannot be split off from the number preceding it.

The portion ahead of the `j` follows the same syntax as a floating-point literal. Hence each of the following counts as a valid imaginary literal:

```python
4.2j
3.14j
10.j
.001j
1e100j
3.14e-10j
3.14_15_93j

```

Differing from a floating-point literal, the decimal point may be dropped when the imaginary number carries only an integer part. The number is nonetheless taken as a floating-point number rather than an integer:

```python
10j
0j
1000000000000000000000000j   # equivalent to 1e+24j

```

Case has no bearing on the `j` suffix. That is to say, `J` works in its place:

```python
3.14J   # equivalent to 3.14j

```

The lexical definition below gives the formal description of imaginary literals:

```text

imagnumber: (floatnumber | digitpart) ("j" | "J")
```

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](numeric-literals.md) · [Previous source section](floating-point-literals.md) · [Following source section](operators-and-delimiters.md)
