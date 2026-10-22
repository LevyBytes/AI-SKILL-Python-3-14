# Python 3.10.0 alpha 1 / library / hashlib

[bpo-40695](https://bugs.python.org/issue?@action=redirect&bpo=40695): [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) will no longer drop back to its builtin hash implementations once OpenSSL supplies a hash digest and security policy blocks the algorithm.

[bpo-9216](https://bugs.python.org/issue?@action=redirect&bpo=9216): [`hashlib.new()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.new) now forwards `usedforsecurity` to the OpenSSL EVP constructor `_hashlib.new()`. Both test_hashlib and test_smtplib cope better under a strict security policy.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
