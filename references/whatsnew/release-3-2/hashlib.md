# What's New In Python 3.2 / hashlib - hashlib

### hashlib

Two new constant attributes appear on the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module; they enumerate the hashing algorithms promised across every implementation as well as those offered by the implementation in use:

```python
>>> import hashlib

>>> hashlib.algorithms_guaranteed
{'sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'}

>>> hashlib.algorithms_available
{'md2', 'SHA256', 'SHA512', 'dsaWithSHA', 'mdc2', 'SHA224', 'MD4', 'sha256',
'sha512', 'ripemd160', 'SHA1', 'MDC2', 'SHA', 'SHA384', 'MD2',
'ecdsa-with-SHA1','md4', 'md5', 'sha1', 'DSA-SHA', 'sha224',
'dsaEncryption', 'DSA', 'RIPEMD160', 'sha', 'MD5', 'sha384'}

```

(Suggested by Carl Chenet in [bpo-7418](https://bugs.python.org/issue?@action=redirect&bpo=7418).)

[Subject index](INDEX.md) · [Previous source section](tarfile.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Next source section](ast.md)
