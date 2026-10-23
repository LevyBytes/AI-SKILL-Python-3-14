# struct - Standard Formats

### Standard Formats

Whenever data leaves your process — over a network or into storage — be exact. State the byte order, size, and alignment outright. Never presume they line up with some machine’s native order; network byte order, for instance, is big-endian while plenty of common CPUs are little-endian. Spell it out and your code stops caring which platform it happens to run on. Lead off with `<` or `>` (or `!`) as a rule. Here the padding is yours to handle. A zero-repeat format character does nothing in this case; you instead have to drop in `'x'` pad bytes by hand wherever they belong. Coming back to the earlier section’s examples, we get:

```python
>>> calcsize('<qh6xq')
24
>>> pack('<qh6xq', 1, 2, 3) == pack('@lhl', 1, 2, 3)
True
>>> calcsize('@llh')
18
>>> pack('@llh', 1, 2, 3) == pack('<qqh', 1, 2, 3)
True
>>> calcsize('<qqh6x')
24
>>> calcsize('@llh0l')
24
>>> pack('@llh0l', 1, 2, 3) == pack('<qqh6x', 1, 2, 3)
True

```

Those results came from a 64-bit machine and carry no promise of holding up on other machines. As a case in point, the examples down here were run on a 32-bit machine:

```python
>>> calcsize('<qqh6x')
24
>>> calcsize('@llh0l')
12
>>> pack('@llh0l', 1, 2, 3) == pack('<qqh6x', 1, 2, 3)
False

```

[Subject index](INDEX.md) · [Previous](native-formats.md) · [Continue](struct-struct-class.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)
