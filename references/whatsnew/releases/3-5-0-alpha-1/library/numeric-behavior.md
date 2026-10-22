# Python 3.5.0 alpha 1 / library / numeric behavior

[bpo-21513](https://bugs.python.org/issue?@action=redirect&bpo=21513): A number of IP address properties (IPv4Address, IPv6Address), such as .is_private or .is_multicast, were sped up.

[bpo-21044](https://bugs.python.org/issue?@action=redirect&bpo=21044): A fileobj carrying an integer ?name? attribute is now handled by tarfile.open(). Antoine Pietri's patch served as the basis.

[bpo-22437](https://bugs.python.org/issue?@action=redirect&bpo=22437): A regular expression's number of capturing groups is no longer held to a limit of 100.

[bpo-23363](https://bugs.python.org/issue?@action=redirect&bpo=23363): Fix possible overflow in itertools.permutations.

[bpo-23364](https://bugs.python.org/issue?@action=redirect&bpo=23364): Fix possible overflow in itertools.product.

[bpo-23366](https://bugs.python.org/issue?@action=redirect&bpo=23366): Fixed possible integer overflow in itertools.combinations.

[bpo-23369](https://bugs.python.org/issue?@action=redirect&bpo=23369): Fixed possible integer overflow in _json.encode_basestring_ascii.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
