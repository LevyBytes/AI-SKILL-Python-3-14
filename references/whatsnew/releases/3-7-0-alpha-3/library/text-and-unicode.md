# Python 3.7.0 alpha 3 / library / text and unicode

[bpo-31690](https://bugs.python.org/issue?@action=redirect&bpo=31690): Permit the re.ASCII, re.LOCALE, and re.UNICODE flags to act as group flags within regular expressions.

[bpo-30349](https://bugs.python.org/issue?@action=redirect&bpo=30349): A FutureWarning is raised from now on whenever a regular expression includes character set constructs slated for a future change in meaning (set operations and nested sets).

[bpo-23033](https://bugs.python.org/issue?@action=redirect&bpo=23033): A wildcard is now honoured in the hostname when it stands as the sole character of the leftmost segment of the hostname supplied as the second argument to `ssl.match_hostname()`. Mandeep Singh wrote the patch.

[bpo-19610](https://bugs.python.org/issue?@action=redirect&bpo=19610): `setup()` now flags invalid types in certain fields. The `distutils.dist.Distribution` class now warns whenever the `classifiers`, `keywords` and `platforms` fields aren't given as either a list or a string.

[bpo-1647489](https://bugs.python.org/issue?@action=redirect&bpo=1647489): Repairs the searching of regular-expression patterns capable of matching an empty string. A non-empty string can now be located properly after an empty string has matched.

[bpo-25054](https://bugs.python.org/issue?@action=redirect&bpo=25054): Splitting on a pattern that might match an empty string is now supported.

[bpo-31843](https://bugs.python.org/issue?@action=redirect&bpo=31843): The *database* argument to sqlite3.connect() now takes a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) and not solely a string.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
