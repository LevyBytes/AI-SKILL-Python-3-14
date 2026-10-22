# How are dictionaries implemented in CPython?

### How are dictionaries implemented in CPython?

CPython's dictionaries take the form of resizable hash tables. Set against B-trees, this yields better lookup performance (lookup being by far the most frequent operation) in most situations, and the implementation is more straightforward.

Dictionaries operate by computing a hash code for each key they store, using the [`hash()`](https://docs.python.org/3.14/library/functions.html#hash) built-in function. The hash code differs greatly with the key and a per-process seed; for instance, `'Python'` might hash to `-539294296` while `'python'`, a string off by a single bit, might hash to `1142331976`. That hash code then serves to work out a slot in an internal array where the value gets stored. Provided that the keys you store all carry distinct hash values, this means dictionaries take constant time ? *O*(1), in Big-O notation ? to fetch a key.

[Subject index](INDEX.md)
