# Descriptor Guide

### Descriptor Guide

Author:

Raymond Hettinger

Contact:

&lt;python at rcn dot com&gt;

[Descriptors](https://docs.python.org/3.14/glossary.html#term-descriptor) let objects customize attribute lookup, storage, and deletion.

This guide is divided into four main parts:

1.

The “primer” offers an introductory overview that progresses slowly through simple examples, introducing a single feature at each step. Begin here if descriptors are new to you.

2.

A fully worked, practical descriptor example appears in the second part. Jump there if the fundamentals are already familiar to you.

3.

A more technical walkthrough covering the precise internal mechanics of descriptors is the focus of the third part. This depth is unnecessary for most readers.

4.

The final part supplies pure Python equivalents of the C-coded built-in descriptors. Consult it if you wonder how functions become bound methods, or how everyday utilities are built — utilities such as [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod), [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod), [`property()`](https://docs.python.org/3.14/library/functions.html#property), and [__slots__](https://docs.python.org/3.14/glossary.html#term-__slots__).

[Subject index](INDEX.md) · [Following source context](primer.md)
