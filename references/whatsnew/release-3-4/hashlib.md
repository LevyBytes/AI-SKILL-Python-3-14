# What's New In Python 3.4 / hashlib - hashlib

### hashlib

A new [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.pbkdf2_hmac) function delivers the [PKCS#5 password-based key derivation function 2](https://en.wikipedia.org/wiki/PBKDF2). (Contributed by Christian Heimes in [bpo-18582](https://bugs.python.org/issue?@action=redirect&bpo=18582).)

The [`name`](https://docs.python.org/3.14/library/hashlib.html#hashlib.hash.name) attribute on [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) hash objects is a formally supported interface now. It has always been present in CPython’s `hashlib` (though it did not hand back lower case names for every supported hash), yet it was not a public interface, so certain other Python implementations had not backed it until now. (Contributed by Jason R. Coombs in [bpo-18532](https://bugs.python.org/issue?@action=redirect&bpo=18532).)

[Subject index](INDEX.md) · [Previous source section](glob.md) · [Next source section](hmac.md) · [Release/subject declaration](release-highlights.md)
