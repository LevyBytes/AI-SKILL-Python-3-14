# secrets`secrets` - Generate secure random numbers for managing secrets

## secrets - Generate secure random numbers for managing secrets

### `secrets` - Generate secure random numbers for managing secrets

Added in version 3.6.

**Source code:** [Lib/secrets.py](https://github.com/python/cpython/tree/3.14/Lib/secrets.py)

---

The `secrets` module exists to produce cryptographically strong random numbers well suited to handling things like passwords, account authentication, security tokens, and other such secrets.

In particular, you should favor `secrets` over the default pseudo-random number generator found in the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module, which is built for modelling and simulation, not for security or cryptography.

See also

[**PEP 506**](https://peps.python.org/pep-0506/)

[Subject index](INDEX.md) · [Continue](secrets-systemrandom-class-to-secrets-randbits.md)
