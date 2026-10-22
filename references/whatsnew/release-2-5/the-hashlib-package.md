# What's New in Python 2.5 / The hashlib package — copy, hashlib

### The hashlib package

A fresh [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module, authored by Gregory P. Smith, now stands in for the `md5` and `sha` modules. `hashlib` brings support for further secure hashes (SHA-224, SHA-256, SHA-384, and SHA-512). Where it can, the module leans on OpenSSL for fast, platform-tuned implementations of the algorithms.

The legacy `md5` and `sha` modules survive as wrappers over hashlib so that backwards compatibility holds. While the new module's interface sits very close to the old ones, it isn't a perfect match. The largest divergence is that the constructor functions used to spin up new hashing objects carry different names.

```python
# Old versions
h = md5.md5()
h = md5.new()

# New version
h = hashlib.md5()

# Old versions
h = sha.sha()
h = sha.new()

# New version
h = hashlib.sha1()

# Hash that weren't previously available
h = hashlib.sha224()
h = hashlib.sha256()
h = hashlib.sha384()
h = hashlib.sha512()

# Alternative form
h = hashlib.new('md5')          # Provide algorithm as a string

```

After a hash object exists, its methods behave as they did before: `update(string)` feeds the given string into the running digest state, `digest()` and `hexdigest()` give the digest back as a binary string or as a string of hex digits, and [`copy()`](https://docs.python.org/3.14/library/copy.html#module-copy) returns a new hashing object that shares the same digest state.

See also

The documentation for the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module.

[Subject index](INDEX.md) · [Previous source section](the-elementtree-package.md) · [Next source section](the-sqlite3-package.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
