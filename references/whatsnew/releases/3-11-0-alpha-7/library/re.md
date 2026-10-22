# Python 3.11.0 alpha 7 / library / re

[bpo-23689](https://bugs.python.org/issue?@action=redirect&bpo=23689): [`re`](https://docs.python.org/3.14/library/re.html#module-re) module: close a memory leak that occurred when a signal or a failed memory allocation ended a match. Ma Lin supplied the patch.

[bpo-47152](https://bugs.python.org/issue?@action=redirect&bpo=47152): Turn the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module into a package. The modules `sre_compile`, `sre_constants` and `sre_parse` are now deprecated.

[bpo-42885](https://bugs.python.org/issue?@action=redirect&bpo=42885): For patterns beginning with `\A` or `^`, tune [`re.search()`](https://docs.python.org/3.14/library/re.html#re.search), [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split), [`re.findall()`](https://docs.python.org/3.14/library/re.html#re.findall), [`re.finditer()`](https://docs.python.org/3.14/library/re.html#re.finditer) and [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub).

[bpo-23691](https://bugs.python.org/issue?@action=redirect&bpo=23691): Guard the [`re.finditer()`](https://docs.python.org/3.14/library/re.html#re.finditer) iterator against being re-entered.

[bpo-35859](https://bugs.python.org/issue?@action=redirect&bpo=35859): Several capturing-group bugs in the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module are fixed; on rare occasions a capturing group received the wrong string. Ma Lin authored the patch.

[bpo-433030](https://bugs.python.org/issue?@action=redirect&bpo=433030): Within [`regular expressions`](https://docs.python.org/3.14/library/re.html#module-re), atomic grouping (`(?>...)`) plus possessive quantifiers (`*+`, `++`, `?+`, `{m,n}+`) are now supported.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
