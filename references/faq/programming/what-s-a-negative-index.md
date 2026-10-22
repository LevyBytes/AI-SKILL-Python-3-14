# What’s a negative index?

### What’s a negative index?

Python sequences carry both positive and negative indices. Among the positive ones, 0 is the first index, 1 is the second index, and onward. Among the negative ones, -1 is the last index, -2 is the penultimate (next to last) index, and onward. Picture `seq[-n]` as equivalent to `seq[len(seq)-n]`.

Negative indices can prove quite handy. As an example, `S[:-1]` covers the whole string apart from its final character, which comes in handy for stripping the trailing newline off a string.

[Subject index](INDEX.md)
