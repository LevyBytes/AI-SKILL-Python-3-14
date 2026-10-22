# sys.intern

sys.intern(*string*)

Place *string* into the table of "interned" strings and return the interned string — which is either *string* itself or a copy. Interning strings can buy a bit of performance on dictionary lookup: when both a dictionary's keys and the lookup key are interned, the key comparisons (following hashing) reduce to a pointer compare rather than a string compare. Ordinarily the names that appear in Python programs are interned automatically, and the dictionaries that store module, class or instance attributes have interned keys.

Interned strings are not [immortal](https://docs.python.org/3.14/glossary.html#term-immortal); to keep the benefit, you must hold on to a reference to whatever `intern()` returns.

[API family](INDEX.md) · [sys context index](../INDEX.md).
