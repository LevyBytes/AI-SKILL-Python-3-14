# secrets — Other functions

### Other functions

 secrets.compare_digest(*a*, *b*)

Give back `True` when strings or [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) *a* and *b* match, and `False` otherwise, relying on a "constant-time compare" that cuts down the danger of [timing attacks](https://codahale.com/a-lesson-in-timing-attacks/). For more particulars, consult [`hmac.compare_digest()`](https://docs.python.org/3.14/library/hmac.html#hmac.compare_digest).

[Subject index](INDEX.md) · [Previous](secrets-default-entropy.md) · [Continue](recipes-and-best-practices.md) · [Owning module, declaration or section: secrets](secrets-generate-secure-random-numbers-for-managing-secrets.md)
