# struct - Native Formats

### Native Formats

As you build format strings that imitate native layouts, byte ordering and padding fall to the compiler and the machine architecture. For that work the `@` format character is the one to use, calling for native byte ordering and data sizes. Pad bytes inside the struct usually appear on their own. You might still need a zero-repeat format code at a format string’s tail, rounding up to the right byte boundary so successive chunks of data stay aligned.

Look at these two small examples, run on a 64-bit, little-endian machine:

```python
>>> calcsize('@lhl')
24
>>> calcsize('@llh')
18

```

Unless you supply extra padding, the second format string leaves its data short of an 8-byte boundary at the end. Adding a zero-repeat format code clears that up:

```python
>>> calcsize('@llh0l')
24

```

Although the `'x'` format code can serve to state the repeat, with native formats a zero-repeat format such as `'0l'` is the better choice.

Native byte ordering and alignment apply on their own by default, yet spelling it out with the `'@'` prefix character is the cleaner habit.

[Subject index](INDEX.md) · [Previous](applications.md) · [Continue](standard-formats.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)
