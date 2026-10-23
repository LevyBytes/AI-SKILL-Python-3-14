# What's New In Python 3.4 / hmac - hashlib, hmac

### hmac

[`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) will now take `bytearray` along with `bytes` for the *key* argument of the [`new()`](https://docs.python.org/3.14/library/hmac.html#hmac.new) function, while the *msg* parameter of both the `new()` function and the [`update()`](https://docs.python.org/3.14/library/hmac.html#hmac.HMAC.update) method now takes any type the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module supports. (Contributed by Jonas Borgström in [bpo-18240](https://bugs.python.org/issue?@action=redirect&bpo=18240).)

The *digestmod* argument of the [`hmac.new()`](https://docs.python.org/3.14/library/hmac.html#hmac.new) function may now be any hash digest name that [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) knows. Beyond that, the present behavior, where *digestmod* falls back to `MD5`, is deprecated: an upcoming version of Python will carry no default value. (Contributed by Christian Heimes in [bpo-17276](https://bugs.python.org/issue?@action=redirect&bpo=17276).)

Once the [`block_size`](https://docs.python.org/3.14/library/hmac.html#hmac.HMAC.block_size) and [`name`](https://docs.python.org/3.14/library/hmac.html#hmac.HMAC.name) attributes arrived (alongside the formal documentation of the [`digest_size`](https://docs.python.org/3.14/library/hmac.html#hmac.HMAC.digest_size) attribute), the [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) module came into full conformance with the [**PEP 247**](https://peps.python.org/pep-0247/) API. (Contributed by Christian Heimes in [bpo-18775](https://bugs.python.org/issue?@action=redirect&bpo=18775).)

[Subject index](INDEX.md) · [Previous source section](hashlib.md) · [Next source section](html.md) · [Release/subject declaration](release-highlights.md)
