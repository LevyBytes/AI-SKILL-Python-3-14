# 2.6.1. Integer literals

### 2.6.1. Integer literals

Whole numbers are denoted by integer literals. To illustrate:

```python
7
3
2147483647

```

Beyond whatever can be held in the memory you have available, no cap exists on how long an integer literal may be:

```python
7922816251426433759354395033679228162514264337593543950336

```

Underscores serve to cluster digits for better readability and play no part in working out the literal's numeric value. To illustrate, all the literals below are equivalent:

```python
100_000_000_000
100000000000
1_00_00_00_00_000

```

An underscore is only ever allowed between digits. To illustrate, `_123`, `321_`, and `123__321` are *not* valid literals.

You can write integers in binary (base 2), octal (base 8), or hexadecimal (base 16) by attaching the prefixes `0b`, `0o` and `0x`, in that order. The hexadecimal digits running from 10 through 15 use the letters `A`-`F`, ignoring case. To illustrate:

```python
0b100110111
0b_1110_0101
0o177
0o377
0xdeadbeef
0xDead_Beef

```

The base specifier may be trailed by an underscore. To illustrate, `0x_1f` is a valid literal, while `0_x1f` and `0x__1f` are not.

A non-zero decimal number may not carry leading zeros. To illustrate, `0123` is not a valid literal. The point of this is to keep it distinct from C-style octal literals, the form Python relied on prior to version 3.0.

The lexical definitions below give the formal description of integer literals:

```text

integer:      decinteger | bininteger | octinteger | hexinteger | zerointeger
decinteger:   nonzerodigit (["_"] digit)*
bininteger:   "0" ("b" | "B") (["_"] bindigit)+
octinteger:   "0" ("o" | "O") (["_"] octdigit)+
hexinteger:   "0" ("x" | "X") (["_"] hexdigit)+
zerointeger:  "0"+ (["_"] "0")*
nonzerodigit: "1"..."9"
digit:        "0"..."9"
bindigit:     "0" | "1"
octdigit:     "0"..."7"
hexdigit:     digit | "a"..."f" | "A"..."F"
```

Changed in version 3.6: Within literals, underscores became permitted as a way to group digits.

[Subject index](INDEX.md) · [Owning language section](lexical-analysis.md) · [Owning language section](numeric-literals.md) · [Previous source section](numeric-literals.md) · [Following source section](floating-point-literals.md)
