# secrets - How many bytes should tokens use?

### How many bytes should tokens use?

To hold up against [brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack), tokens require enough randomness. Sadly, what counts as enough is bound to climb as computers grow more powerful and can run through more guesses in less time. The belief as of 2015 is that 32 bytes (256 bits) of randomness suffices for the typical use-case the `secrets` module targets.

If you would rather manage your own token length, you can spell out exactly how much randomness goes into tokens by passing an [`int`](https://docs.python.org/3.14/library/functions.html#int) argument to the various `token_*` functions. That argument counts as the number of bytes of randomness to use.

Otherwise, when no argument is given, or when the argument is `None`, the `token_*` functions fall back on `DEFAULT_ENTROPY`.

 secrets.DEFAULT_ENTROPY

Default number of bytes of randomness used by the `token_*` functions.

Its precise value may shift whenever, maintenance releases included.

[Subject index](INDEX.md) · [Previous](secrets-token-bytes-to-secrets-token-urlsafe.md) · [Continue](secrets-compare-digest.md) · [Owning module, declaration or section: secrets](secrets-generate-secure-random-numbers-for-managing-secrets.md)
